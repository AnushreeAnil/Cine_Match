# 🎬 CineMatch - Movie Recommendation System

## BCA Final Year Project | Anushree Anil | U03AI23S0011

---

## Project Summary

CineMatch is a dark-themed web application that helps users discover Indian movies through intelligent recommendations. It combines a curated SQLite movie catalogue with a content-based recommendation engine built using TF-IDF and cosine similarity.

This project is suitable as a BCA final year submission because it includes:

- a full-stack Python/Flask web app
- database integration with SQLite
- a recommendation algorithm built from first principles
- search, filtering, actor-based discovery, and analytics
- clean UI enhancements and responsive design

## My Role

I designed and developed this project myself, including the Flask backend, SQLite database seeding, recommendation logic, and frontend templates. I also personally tested the app by running it locally and verifying the main flows.

---

## Quick Start

### 1. Install dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### 2. Start the application

```bash
python app.py
```

### 3. Open in browser

Visit:

```
http://127.0.0.1:5000
```

---

## Features

- Home page with top-rated and trending Indian movies
- Discover movies by mood, genre, language, and release period
- Actor-based recommendations using popular actor cards and search suggestions
- Search movies by title, genre, cast, or language
- Movie details with IMDb links and personalized recommendations
- Similar movie recommendations with match score and reason tags
- Real database-driven statistics and content
- Dark theme with improved hover effects and badges

---

## Application Structure

```
movie_recommender/
├── app.py                # Flask application and routing
├── database.py           # SQLite schema creation and seeding
├── recommender.py        # Content-based recommendation engine
├── movies.db             # SQLite database (created automatically)
├── requirements.txt      # Python dependency manifest
├── README.md             # Project documentation
├── PROJECT_REPORT.md     # Project report for submission
└── templates/            # HTML templates
    ├── base.html
    ├── home.html
    ├── recommend.html
    ├── movie_detail.html
    ├── all_movies.html
    ├── search.html
    ├── actor_recommendations.html
    ├── mood_match.html
    ├── login.html
    ├── register.html
    ├── profile.html
    └── quiz.html
```

---

## System Design

### Database

- SQLite database stored in `movies.db`
- `movies` table stores movie metadata, language, and IMDb links
- `user_ratings` table stores ratings submitted by users

### Recommendation Engine

1. Builds a combined text string for each movie from genre, director, cast, and language.
2. Converts movie text into numeric vectors using TF-IDF.
3. Calculates cosine similarity between the selected movie and all others.
4. Returns the top 5 most similar movies with match percentage and reasons.

### Why it works

- TF-IDF helps identify the most descriptive movie attributes.
- Cosine similarity measures how similar two movies are in vector space.
- Reason tags such as **Same Genre**, **Same Language**, and **Similar Cast** make recommendations explainable.

---

## Project Report

A detailed project report is available in `PROJECT_REPORT.md`, including:

- objective and scope
- technology stack
- architecture diagram
- database schema
- algorithm explanation
- features and demo scenarios
- future enhancements

---

## Evaluation Checklist

- [x] Functional Flask web application
- [x] SQLite database with seeded movie data
- [x] Recommendation algorithm implemented using scikit-learn
- [x] Search, filter, and recommendation workflows
- [x] Clean and consistent dark UI theme
- [x] Documentation for setup and project details
- [x] Submission-ready report

---

## Future Enhancements

- Add user authentication and personalized watchlists
- Improve actor search with live autocomplete
- Add quiz-driven and profile-based recommendations

- Add user reviews and comment sections
- Add more advanced recommendation logic such as collaborative filtering
