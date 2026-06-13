# CineMatch Project Report

## 1. Project Title

CineMatch - Intelligent Movie Recommendation System

## 2. Student Details

- Name: Anushree Anil
- Course: BCA Final Year
- Roll/ID: U03AI23S0011

## 2.1 My Role

I personally implemented the whole project. I wrote the backend routes in `app.py`, created the database and data seeding logic in `database.py`, developed the recommendation algorithm in `recommender.py`, and styled the templates to match the dark theme.

## 3. Introduction

CineMatch is a recommendation web application designed to help users discover Indian movies through an enriched, mood-driven experience. The system uses a curated movie catalogue, a SQLite database, and a content-based recommendation engine to deliver relevant movie suggestions.

## 4. Objective

The primary objective is to create a complete, user-friendly movie discovery platform that:

- helps users find films matching their mood or favorite actor,
- provides movie details and related recommendations,
- uses a database-backed architecture and machine learning techniques,
- is suitable for a BCA final-year project submission.

## 5. Problem Statement

Many users spend too much time browsing and still cannot decide which movie to watch. In particular, audiences want recommendations that match:

- their current mood,
- preferred language,
- favorite actors,
- regional language and content preferences.

CineMatch solves this by offering multiple discovery methods and intelligent recommendations in a single application.

## 6. Scope of the Project

This project covers the following scope:

- Web application development with Python Flask.
- SQLite database creation and seeding with movie data.
- Content-based recommendation engine using TF-IDF and cosine similarity.
- UI/UX improvements such as dark theme, cards, badges, and buttons.
- Search and filtering features across movies, actors, moods, and language.

## 7. Technologies Used

- Python 3
- Flask
- SQLite
- scikit-learn
- HTML/CSS
- Jinja2 templating

## 8. System Architecture

The application consists of three main layers:

1. **Frontend**
   - HTML templates in `templates/`
   - Dark theme UI with cards, badges, and hover effects
   - Pages for home, search, discovery, actor recommendations, and movie details

2. **Backend**
   - `app.py` provides route handling, user interaction logic, and page rendering
   - `database.py` initializes SQLite schema, seeds movie data, and maintains columns
   - `recommender.py` performs movie search and recommendation calculations

3. **Database**
   - `movies.db` stores movie metadata, language, IMDb links, and ratings
   - `user_ratings` table stores ratings submitted by end users

## 9. Database Design

### `movies` table

The `movies` table stores all movie-related attributes required for discovery:

- `id` INTEGER PRIMARY KEY
- `title` TEXT
- `genre` TEXT
- `language` TEXT
- `director` TEXT
- `cast` TEXT
- `description` TEXT
- `rating` REAL
- `year` INTEGER
- `imdb_link` TEXT

### `user_ratings` table

The `user_ratings` table enables users to submit ratings:

- `id` INTEGER PRIMARY KEY
- `username` TEXT
- `movie_id` INTEGER
- `rating` REAL

## 10. Data Preparation and Seeding

The `database.py` file contains a curated list of Indian movies spanning multiple languages and genres. It automatically:

- creates the SQLite database if missing,
- adds required columns for language and IMDb link,
- backfills older rows if data already existed,
- inserts or updates movie records without duplicates.

## 11. Recommendation Engine

### 11.1. Approach

CineMatch uses a **content-based recommendation algorithm**. This is ideal for a project because it is explainable and easy to demonstrate.

### 11.2. Implementation Details

The recommendation logic is implemented in `recommender.py` with the following steps:

1. Build a combined movie content string from:
   - genre,
   - director,
   - cast,
   - language.

2. Convert text data into numerical vectors using **TF-IDF** (Term Frequency-Inverse Document Frequency).

3. Compute **cosine similarity** across all movie vectors.

4. For a selected movie, sort other movies by similarity and select the top N.

5. Add recommendation metadata:
   - similarity percentage,
   - reason tags such as **Same Genre**, **Same Language**, and **Similar Cast**.

### 11.3. Similarity Reasons

The system identifies reasons that make a recommendation feel intelligent:

- **Same Genre**: shared movie categories like action, drama, or romance.
- **Same Language**: movies in the same spoken language.
- **Similar Cast**: overlapping actors between movies.

If no strong overlap exists, the system still shows a fallback explanation like **Similar Story Profile**.

## 12. Key Features

### 12.1 Home Page

- Dark-themed homepage with a heading and summary.
- Real database statistics for:
  - available movies,
  - supported languages.
- Trending Indian movies chosen dynamically from the dataset.
- Top rated movie cards with language and rating badges.

### 12.2 Discover By Mood

- Mood-based discovery section.
- Filters for mood, genre, language, and release period.
- Search results presented as movie cards.

### 12.3 Recommend By Actor

- Popular actor cards for quick access.
- Searchable actor input with suggestions from the full actor list.
- Movies shown for the selected actor.

### 12.4 Movie Detail Page

- Detailed movie information, including title, year, genre, language, director, cast, description, rating, and IMDb link.
- Similar movie recommendations with match percentage and reason labels.

### 12.5 Search

- Search by title, genre, cast, or language.
- Results rendered in consistent movie card format.

## 13. User Interaction Flow

1. User opens the home page.
2. They can browse trending movies or use the search bar.
3. They may select a mood or filter under Discover.
4. They may choose a favorite actor from actor cards.
5. On a movie detail page, they can view similar recommendations and IMDb information.

## 14. File-Level Breakdown

- `app.py`: Main application logic, routes, filtering, and page rendering.
- `database.py`: Database initialization, schema updates, movie seeding, IMDb links.
- `recommender.py`: Movie retrieval, search, and recommendation formulas.
- `templates/base.html`: Global site layout, navigation, styling, and dark theme.
- `templates/home.html`: Home page content and homepage movie cards.
- `templates/recommend.html`: Movie similarity recommendation page.
- `templates/movie_detail.html`: Single movie details and similar recommendations.
- `templates/actor_recommendations.html`: Actor-based recommendation page.
- `templates/mood_match.html`: Discover page with filters and mood-driven search.
- `templates/all_movies.html`: Browse all movies and filters.
- `templates/search.html`: Search result page.

## 15. Implementation Challenges

- Ensuring the movie database seeded consistently without duplicates.
- Making recommendations explainable rather than just returning similar titles.
- Designing a UI that felt polished in a dark theme while preserving accessibility.

## 16. Advantages of the Project

- Demonstrates full-stack development with backend, database, and frontend.
- Uses a machine learning approach that can be explained easily in a viva.
- Offers multiple movie discovery paths, improving user experience.
- Provides real-looking statistics and a curated movie catalogue.

## 17. Limitations

- No user authentication or personalized profile.
- Content metadata is curated from the movie catalogue and not fetched from external APIs.
- The recommendation engine is metadata-based and does not use user behavior.
- No mobile app or native client is included.

## 18. Testing and Verification

The project has been verified by:

- compiling the Python files to ensure there are no syntax errors,
- running the Flask application so it starts correctly,
- loading the home, search, actor recommendations, discover, and movie details pages,
- checking that the SQLite database is created and populated automatically.

## 19. Future Enhancements

- Add user login, favorites, and watchlist functionality.
- Integrate live availability data for regional movies.
- Add user reviews and rating aggregation.
- Add collaborative filtering for personalized recommendations.
- Add a richer actor autocomplete using JavaScript.

## 20. Conclusion

CineMatch is a complete BCA final-year project that combines real database work, web development, and a recommendation algorithm. It is easy to demonstrate, easy to explain, and built to be extended with future features.

## 20. How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python app.py
   ```
3. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

## 21. Project Demo Checklist

- [x] Home page and trending movie cards
- [x] Mood-based movie discovery
- [x] Actor-based recommendation cards
- [x] Search results by keyword
- [x] Movie detail page with IMDb links and user actions
- [x] Similar movie recommendations with match scores
- [x] Database-driven statistics and content
- [x] Dark theme UI
