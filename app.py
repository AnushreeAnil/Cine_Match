from datetime import datetime
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

from database import create_database
from recommender import (
    add_favorite,
    add_watchlist,
    create_user,
    get_all_actors,
    get_all_movies,
    get_movie_by_id,
    get_movies_by_actor,
    get_recommendations,
    get_user_by_email,
    get_user_by_id,
    get_user_favorites,
    get_user_preferences,
    get_user_watchlist,
    recommend_for_user,
    remove_favorite,
    remove_watchlist,
    save_user_preferences,
    save_user_rating,
    search_movies,
    user_has_favorite,
    user_has_watchlist
)

app = Flask(__name__)
app.secret_key = "movierecsecret123"

MOODS = [
    "Happy",
    "Romantic",
    "Thrilling",
    "Action",
    "Emotional",
    "Motivational",
    "Family",
    "Feel Good",
    "Adventure",
    "Mystery",
    "Horror"
]

MOOD_MAPPING = {
    "Happy": ["comedy", "feel good", "family", "drama"],
    "Romantic": ["romance", "drama", "music"],
    "Thrilling": ["thriller", "mystery", "crime"],
    "Action": ["action", "adventure", "crime"],
    "Emotional": ["drama", "family", "biography"],
    "Motivational": ["sport", "biography", "drama"],
    "Family": ["family", "comedy", "drama"],
    "Feel Good": ["comedy", "family", "adventure"],
    "Adventure": ["adventure", "action", "fantasy"],
    "Mystery": ["mystery", "thriller", "crime"],
    "Horror": ["horror", "thriller", "mystery"]
}

GENRES = ["Action", "Comedy", "Drama", "Crime", "Romance", "Thriller"]
LANGUAGES = [
    "Hindi",
    "Malayalam",
    "Kannada",
    "Tamil",
    "Telugu",
    "Bengali",
    "Marathi",
    "Punjabi",
    "Gujarati",
    "Assamese",
    "Odia",
    "Tulu"
]
RELEASE_PERIODS = [
    ("latest", "Latest (2020+)"),
    ("modern", "Modern (2010-2019)"),
    ("classic", "Classic (Before 2010)")
]
PERSONALITY_TYPES = [
    "Action Explorer",
    "Romantic Dreamer",
    "Mystery Hunter",
    "Family Movie Lover",
    "Emotional Storyteller",
    "Adventure Seeker"
]

create_database()


def get_current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return get_user_by_id(user_id)


def login_user(user):
    session["user_id"] = user["id"]
    session["user_name"] = user["name"]
    session["user_email"] = user["email"]


def logout_user():
    session.clear()


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get("user_id"):
            return view(*args, **kwargs)

        if request.endpoint == "home":
            return redirect(url_for("welcome"))

        flash("Please log in to continue.")
        return redirect(url_for("login"))

    return wrapped_view


@app.route("/")
@login_required
def home():
    user = get_current_user()
    movies = get_all_movies()

    top_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)[:6]
    indian_languages = {
        "Hindi", "Malayalam", "Kannada", "Tamil",
        "Telugu", "Bengali", "Marathi", "Punjabi",
        "Gujarati", "Assamese", "Odia", "Tulu"
    }
    trending_movies = sorted(
        [m for m in movies if m.get("language") in indian_languages],
        key=lambda x: x["rating"],
        reverse=True
    )[:6]

    favorites = get_user_favorites(user["id"])
    watchlist = get_user_watchlist(user["id"])
    personalized = recommend_for_user(user["id"], top_n=6)

    stats = {
        "movies": len(movies),
        "languages": len({movie["language"] for movie in movies if movie["language"]}),
        "moods": len(MOODS),
        "released": len(RELEASE_PERIODS)
    }

    return render_template(
        "home.html",
        user=user,
        movies=top_movies,
        trending_movies=trending_movies,
        recommended_movies=personalized,
        stats=stats,
        mood_cards=[
            ("Happy", "&#128522;"),
            ("Romantic", "&#10084;"),
            ("Action", "&#128293;"),
            ("Thrilling", "&#128561;"),
            ("Family", "&#128106;"),
            ("Motivational", "&#128170;")
        ],
        favorites=favorites,
        watchlist=watchlist
    )


@app.route("/welcome")
def welcome():
    if session.get("user_id"):
        return redirect(url_for("home"))
    return render_template("welcome.html")


@app.route("/search")
@login_required
def search():
    user = get_current_user()
    query = request.args.get("q", "")
    results = []

    if query:
        results = search_movies(query)

    return render_template(
        "search.html",
        user=user,
        results=results,
        query=query
    )


@app.route("/movie/<int:movie_id>")
@login_required
def movie_detail(movie_id):
    user = get_current_user()
    movie = get_movie_by_id(movie_id)

    if not movie:
        return "Movie not found", 404

    recommendations = get_recommendations(movie["title"], top_n=5)
    favorite = user_has_favorite(user["id"], movie_id)
    watchlist = user_has_watchlist(user["id"], movie_id)

    return render_template(
        "movie_detail.html",
        user=user,
        movie=movie,
        recommendations=recommendations,
        favorite=favorite,
        watchlist=watchlist
    )


@app.route("/recommend", methods=["GET", "POST"])
@login_required
def recommend():
    user = get_current_user()
    movies = get_all_movies()
    recommendations = []
    selected_movie = None

    if request.method == "POST":
        selected_title = request.form.get("movie_title")
        selected_movie = selected_title
        recommendations = get_recommendations(selected_title, top_n=5)

    return render_template(
        "recommend.html",
        user=user,
        movies=movies,
        recommendations=recommendations,
        selected_movie=selected_movie
    )


@app.route("/rate", methods=["POST"])
@login_required
def rate_movie():
    user = get_current_user()
    movie_id = request.form.get("movie_id")
    rating = request.form.get("rating")

    if movie_id and rating:
        save_user_rating(user["name"], int(movie_id), float(rating))

    return redirect(url_for("movie_detail", movie_id=movie_id))


@app.route("/movies")
@login_required
def all_movies():
    user = get_current_user()
    movies = get_all_movies()
    genre_filter = request.args.get("genre", "")
    language_filter = request.args.get("language", "")

    if genre_filter:
        movies = [
            m for m in movies
            if genre_filter.lower() in m["genre"].lower()
        ]

    if language_filter:
        movies = [
            m for m in movies
            if language_filter.lower() == m["language"].lower()
        ]

    return render_template(
        "all_movies.html",
        user=user,
        movies=movies,
        genre_filter=genre_filter,
        language_filter=language_filter
    )


@app.route("/discover", methods=["GET", "POST"])
@app.route("/mood-match", methods=["GET", "POST"])
@login_required
def mood_match():
    user = get_current_user()
    movies = get_all_movies()
    results = []
    method_data = request.form if request.method == "POST" else request.args
    selected_filters = {
        "mood": method_data.get("mood", ""),
        "genre": method_data.get("genre", ""),
        "language": method_data.get("language", ""),
        "year": method_data.get("year", "")
    }

    stats = {
        "movies": len(movies),
        "languages": len({movie["language"] for movie in movies if movie["language"]}),
        "moods": len(MOODS),
        "released": len(RELEASE_PERIODS)
    }

    has_filters = any(selected_filters.values())

    if request.method == "POST" or has_filters:
        filtered_movies = movies

        if selected_filters["mood"] in MOOD_MAPPING:
            filtered_movies = [
                movie for movie in filtered_movies
                if any(
                    keyword.lower() in movie["genre"].lower()
                    for keyword in MOOD_MAPPING[selected_filters["mood"]]
                )
            ]

        if selected_filters["genre"]:
            filtered_movies = [
                movie for movie in filtered_movies
                if selected_filters["genre"].lower() in movie["genre"].lower()
            ]

        if selected_filters["language"]:
            filtered_movies = [
                movie for movie in filtered_movies
                if selected_filters["language"].lower() in movie["language"].lower()
                or selected_filters["language"].lower() in movie["genre"].lower()
            ]

        if selected_filters["year"] == "latest":
            filtered_movies = [movie for movie in filtered_movies if movie["year"] >= 2020]
        elif selected_filters["year"] == "modern":
            filtered_movies = [movie for movie in filtered_movies if 2010 <= movie["year"] <= 2019]
        elif selected_filters["year"] == "classic":
            filtered_movies = [movie for movie in filtered_movies if movie["year"] < 2010]

        results = sorted(filtered_movies, key=lambda x: x["rating"], reverse=True)[:12]

    return render_template(
        "mood_match.html",
        user=user,
        results=results,
        moods=MOODS,
        genres=GENRES,
        languages=LANGUAGES,
        release_periods=RELEASE_PERIODS,
        selected_filters=selected_filters,
        stats=stats,
        has_searched=request.method == "POST" or has_filters
    )


@app.route("/actor-recommendations", methods=["GET", "POST"])
@login_required
def actor_recommendations():
    user = get_current_user()
    actors = get_all_actors()
    selected_actor = request.values.get("actor", "")
    results = get_movies_by_actor(selected_actor) if selected_actor else []
    popular_actors = [
        "Shah Rukh Khan",
        "Mohanlal",
        "Dulquer Salmaan",
        "Yash",
        "Prabhas",
        "Allu Arjun",
        "Vijay",
        "Suriya",
        "Aamir Khan"
    ]

    return render_template(
        "actor_recommendations.html",
        user=user,
        actors=actors,
        popular_actors=popular_actors,
        selected_actor=selected_actor,
        results=results
    )


@app.route("/profile")
@login_required
def profile():
    user = get_current_user()
    favorites = get_user_favorites(user["id"])
    watchlist = get_user_watchlist(user["id"])
    preferences = get_user_preferences(user["id"])
    personalized = recommend_for_user(user["id"], top_n=6)

    return render_template(
        "profile.html",
        user=user,
        favorites=favorites,
        watchlist=watchlist,
        preferences=preferences,
        recommended_movies=personalized
    )


@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    user = get_current_user()
    preferences = get_user_preferences(user["id"])

    if request.method == "POST":
        personality_type = request.form.get("personality_type", "")
        favorite_genre = request.form.get("favorite_genre", "")
        favorite_language = request.form.get("favorite_language", "")

        save_user_preferences(
            user["id"],
            personality_type,
            favorite_genre,
            favorite_language,
            datetime.utcnow().isoformat()
        )
        flash("Quiz results saved. Your recommendations were updated.")
        return redirect(url_for("profile"))

    return render_template(
        "quiz.html",
        user=user,
        personality_types=PERSONALITY_TYPES,
        genres=GENRES,
        languages=LANGUAGES,
        preferences=preferences
    )


@app.route("/favorite/<int:movie_id>", methods=["POST"])
@login_required
def favorite_movie(movie_id):
    action = request.form.get("action", "add")
    if action == "remove":
        remove_favorite(session["user_id"], movie_id)
    else:
        add_favorite(session["user_id"], movie_id)

    return redirect(request.form.get("next") or url_for("movie_detail", movie_id=movie_id))


@app.route("/watchlist/<int:movie_id>", methods=["POST"])
@login_required
def watchlist_movie(movie_id):
    action = request.form.get("action", "add")
    if action == "remove":
        remove_watchlist(session["user_id"], movie_id)
    else:
        add_watchlist(session["user_id"], movie_id)

    return redirect(request.form.get("next") or url_for("movie_detail", movie_id=movie_id))


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("home"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name or not email or not password or not confirm_password:
            flash("Please fill in all registration fields.")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        if get_user_by_email(email):
            flash("This email is already registered.")
            return redirect(url_for("register"))

        password_hash = generate_password_hash(password)
        create_user(name, email, password_hash, datetime.utcnow().isoformat())
        flash("Account created successfully. Please log in.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("home"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = get_user_by_email(email)
        if not user or not check_password_hash(user["password_hash"], password):
            flash("Invalid login details.")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
