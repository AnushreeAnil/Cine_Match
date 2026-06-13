import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MOVIE_SELECT = """
    SELECT id, title, genre, director, "cast", description, rating, year,
           COALESCE(language, '') AS language,
           COALESCE(imdb_link, '') AS imdb_link
    FROM movies
"""


def row_to_movie(row):
    return {
        "id": row[0],
        "title": row[1],
        "genre": row[2],
        "director": row[3],
        "cast": row[4],
        "description": row[5],
        "rating": row[6],
        "year": row[7],
        "language": row[8],
        "imdb_link": row[9]
    }


def get_all_movies():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(MOVIE_SELECT)
    rows = cursor.fetchall()
    conn.close()

    return [row_to_movie(row) for row in rows]


def build_content_string(movie):
    content = " ".join([
        movie.get("genre", ""),
        movie.get("director", ""),
        movie.get("cast", ""),
        movie.get("language", "")
    ])
    return content.replace(",", " ").lower()


def split_genres(value):
    return {
        term.strip().lower()
        for term in value.replace("|", " ").replace(",", " ").split()
        if term.strip()
    }


def split_people(value):
    return {
        term.strip().lower()
        for term in value.split(",")
        if term.strip()
    }


def get_recommendation_reasons(selected_movie, recommended_movie):
    reasons = []
    selected_genres = split_genres(selected_movie.get("genre", ""))
    recommended_genres = split_genres(recommended_movie.get("genre", ""))
    selected_cast = split_people(selected_movie.get("cast", ""))
    recommended_cast = split_people(recommended_movie.get("cast", ""))

    if selected_genres.intersection(recommended_genres):
        reasons.append("Same Genre")

    if (
        selected_movie.get("language")
        and selected_movie.get("language") == recommended_movie.get("language")
    ):
        reasons.append("Same Language")

    if selected_cast.intersection(recommended_cast):
        reasons.append("Similar Cast")

    if not reasons:
        reasons.append("Similar Story Profile")

    return reasons


def get_recommendations(movie_title, top_n=5):
    movies = get_all_movies()

    if len(movies) == 0:
        return []

    content_list = [build_content_string(movie) for movie in movies]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(content_list)
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    selected_index = -1
    for i, movie in enumerate(movies):
        if movie["title"].lower() == movie_title.lower():
            selected_index = i
            break

    if selected_index == -1:
        return []

    similarity_scores = list(enumerate(similarity_matrix[selected_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for index, score in similarity_scores[1:top_n + 1]:
        rec_movie = movies[index]
        rec_movie["similarity_score"] = round(score * 100, 1)
        rec_movie["reasons"] = get_recommendation_reasons(
            movies[selected_index],
            rec_movie
        )
        recommendations.append(rec_movie)

    return recommendations


def search_movies(query):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    search_term = "%" + query.lower() + "%"
    cursor.execute(MOVIE_SELECT + """
        WHERE LOWER(title) LIKE ?
           OR LOWER(genre) LIKE ?
           OR LOWER("cast") LIKE ?
           OR LOWER(language) LIKE ?
    """, (search_term, search_term, search_term, search_term))
    rows = cursor.fetchall()
    conn.close()

    return [row_to_movie(row) for row in rows]


def get_all_actors():
    actors = set()
    for movie in get_all_movies():
        for actor in movie["cast"].split(","):
            actor = actor.strip()
            if actor:
                actors.add(actor)

    return sorted(actors, key=lambda name: name.lower())


def normalize_actor_name(actor):
    return " ".join(part.strip().lower() for part in actor.split(" ") if part.strip())


def get_movies_by_actor(actor):
    if not actor:
        return []

    normalized_search = normalize_actor_name(actor)
    movies = [
        movie for movie in get_all_movies()
        if normalized_search in normalize_actor_name(movie["cast"])
    ]
    return sorted(movies, key=lambda x: x["rating"], reverse=True)


def get_user_preferences(user_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT personality_type, favorite_genre, favorite_language FROM user_preferences WHERE user_id = ?",
        (user_id,)
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "personality_type": row[0],
            "favorite_genre": row[1],
            "favorite_language": row[2]
        }
    return None


def get_user_collection(user_id, table_name):
    if table_name not in {"favorites", "watchlist"}:
        return []

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT movies.id, movies.title, movies.genre, movies.director, movies."cast", 
               movies.description, movies.rating, movies.year,
               COALESCE(movies.language, '') AS language,
               COALESCE(movies.imdb_link, '') AS imdb_link
        FROM movies
        JOIN {table_name} ON {table_name}.movie_id = movies.id
        WHERE {table_name}.user_id = ?
        """,
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    return [row_to_movie(row) for row in rows]


def get_user_favorites(user_id):
    return get_user_collection(user_id, "favorites")


def get_user_watchlist(user_id):
    return get_user_collection(user_id, "watchlist")


def get_user_by_email(email):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, email, password_hash FROM users WHERE LOWER(email) = ?",
        (email.strip().lower(),)
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "password_hash": row[3]
        }
    return None


def get_user_by_id(user_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, email, created_at FROM users WHERE id = ?",
        (user_id,)
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"id": row[0], "name": row[1], "email": row[2], "created_at": row[3]}
    return None


def create_user(name, email, password_hash, created_at):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
        (name.strip(), email.strip().lower(), password_hash, created_at)
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id


def save_user_preferences(user_id, personality_type, favorite_genre, favorite_language, updated_at):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM user_preferences WHERE user_id = ?",
        (user_id,)
    )
    existing = cursor.fetchone()

    if existing:
        cursor.execute(
            "UPDATE user_preferences SET personality_type = ?, favorite_genre = ?, favorite_language = ?, updated_at = ? WHERE user_id = ?",
            (personality_type, favorite_genre, favorite_language, updated_at, user_id)
        )
    else:
        cursor.execute(
            "INSERT INTO user_preferences (user_id, personality_type, favorite_genre, favorite_language, updated_at) VALUES (?, ?, ?, ?, ?)",
            (user_id, personality_type, favorite_genre, favorite_language, updated_at)
        )

    conn.commit()
    conn.close()


def add_favorite(user_id, movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM favorites WHERE user_id = ? AND movie_id = ?",
        (user_id, movie_id)
    )
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO favorites (user_id, movie_id) VALUES (?, ?)",
            (user_id, movie_id)
        )
        conn.commit()
    conn.close()


def remove_favorite(user_id, movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM favorites WHERE user_id = ? AND movie_id = ?",
        (user_id, movie_id)
    )
    conn.commit()
    conn.close()


def add_watchlist(user_id, movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM watchlist WHERE user_id = ? AND movie_id = ?",
        (user_id, movie_id)
    )
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO watchlist (user_id, movie_id) VALUES (?, ?)",
            (user_id, movie_id)
        )
        conn.commit()
    conn.close()


def remove_watchlist(user_id, movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM watchlist WHERE user_id = ? AND movie_id = ?",
        (user_id, movie_id)
    )
    conn.commit()
    conn.close()


def user_has_favorite(user_id, movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM favorites WHERE user_id = ? AND movie_id = ?",
        (user_id, movie_id)
    )
    found = cursor.fetchone() is not None
    conn.close()
    return found


def user_has_watchlist(user_id, movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM watchlist WHERE user_id = ? AND movie_id = ?",
        (user_id, movie_id)
    )
    found = cursor.fetchone() is not None
    conn.close()
    return found


def recommend_for_user(user_id, top_n=6):
    prefs = get_user_preferences(user_id)
    movies = get_all_movies()

    if not movies:
        return []

    if not prefs:
        return sorted(movies, key=lambda x: x["rating"], reverse=True)[:top_n]

    preference_string = " ".join([
        prefs.get("favorite_genre", ""),
        prefs.get("favorite_language", ""),
        prefs.get("personality_type", "")
    ])
    content_list = [build_content_string(movie) for movie in movies]
    content_list.append(preference_string)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(content_list)
    user_vector = tfidf_matrix[-1]
    movie_vectors = tfidf_matrix[:-1]
    similarity_scores = cosine_similarity(movie_vectors, user_vector).reshape(-1)

    scored_movies = []
    for index, movie in enumerate(movies):
        score = similarity_scores[index]
        if prefs.get("favorite_genre") and prefs["favorite_genre"].lower() in movie["genre"].lower():
            score += 0.18
        if prefs.get("favorite_language") and prefs["favorite_language"].lower() == movie["language"].lower():
            score += 0.16

        personality = prefs.get("personality_type", "")
        if personality == "Action Explorer" and "action" in movie["genre"].lower():
            score += 0.14
        elif personality == "Mystery Hunter" and "mystery" in movie["genre"].lower():
            score += 0.14
        elif personality == "Romantic Dreamer" and "romance" in movie["genre"].lower():
            score += 0.14
        elif personality == "Family Movie Lover" and "family" in movie["genre"].lower():
            score += 0.14
        elif personality == "Emotional Storyteller" and "drama" in movie["genre"].lower():
            score += 0.14
        elif personality == "Adventure Seeker" and "adventure" in movie["genre"].lower():
            score += 0.14

        scored_movies.append((movie, score))

    scored_movies = sorted(scored_movies, key=lambda item: (item[1], item[0]["rating"]), reverse=True)

    recommendations = []
    for movie, score in scored_movies[:top_n]:
        movie["score"] = round(score * 100, 1)
        movie["recommendation_note"] = "Recommended For You"
        recommendations.append(movie)

    return recommendations


def save_user_rating(username, movie_id, rating):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM user_ratings WHERE username = ? AND movie_id = ?
    """, (username, movie_id))
    existing = cursor.fetchone()

    if existing:
        cursor.execute("""
            UPDATE user_ratings SET rating = ? WHERE username = ? AND movie_id = ?
        """, (rating, username, movie_id))
    else:
        cursor.execute("""
            INSERT INTO user_ratings (username, movie_id, rating) VALUES (?, ?, ?)
        """, (username, movie_id, rating))

    conn.commit()
    conn.close()


def get_movie_by_id(movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(MOVIE_SELECT + " WHERE id = ?", (movie_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return row_to_movie(row)
    return None
