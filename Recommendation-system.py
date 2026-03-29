"""
CODSOFT AI Intern- Task 4
Indian Movie Recommendation System using Collaborative Filtering
Run: python recommendation.py
"""

from math import sqrt

# Indian users and their movie ratings (1-5 scale)
ratings = {
    "Ganesh":   {"KGF Chapter 2": 5, "Baahubali 2": 5, "RRR": 4, "Pushpa": 3, "3 Idiots": 2, "Dangal": 2, "Uri": 4, "Kabir Singh": 1, "Dilwale": 2, "Sultan": 3},
    "Akash":    {"KGF Chapter 2": 2, "Baahubali 2": 3, "RRR": 2, "Pushpa": 1, "3 Idiots": 5, "Dangal": 5, "Uri": 3, "Kabir Singh": 4, "Dilwale": 5, "Sultan": 4},
    "Praveen":  {"KGF Chapter 2": 5, "Baahubali 2": 4, "RRR": 5, "Pushpa": 4, "3 Idiots": 3, "Dangal": 2, "Uri": 5, "Kabir Singh": 2, "Dilwale": 1, "Sultan": 3},
    "Shobha":   {"KGF Chapter 2": 1, "Baahubali 2": 2, "RRR": 2, "Pushpa": 2, "3 Idiots": 5, "Dangal": 4, "Uri": 2, "Kabir Singh": 5, "Dilwale": 5, "Sultan": 4},
    "Parinitha":{"KGF Chapter 2": 5, "Baahubali 2": 5, "RRR": 5, "Pushpa": 5, "3 Idiots": 2, "Dangal": 1, "Uri": 4, "Kabir Singh": 1, "Dilwale": 2, "Sultan": 2},
    "Manjunath":{"KGF Chapter 2": 2, "Baahubali 2": 1, "RRR": 2, "Pushpa": 2, "3 Idiots": 4, "Dangal": 5, "Uri": 2, "Kabir Singh": 5, "Dilwale": 4, "Sultan": 5},
    "PremRaj":  {"KGF Chapter 2": 4, "Baahubali 2": 5, "RRR": 4, "Pushpa": 3, "3 Idiots": 3, "Dangal": 3, "Uri": 5, "Kabir Singh": 2, "Dilwale": 2, "Sultan": 4},
    "Veena":    {"KGF Chapter 2": 1, "Baahubali 2": 2, "RRR": 1, "Pushpa": 2, "3 Idiots": 5, "Dangal": 5, "Uri": 1, "Kabir Singh": 4, "Dilwale": 5, "Sultan": 3},
}

# Movie genres for display
genres = {
    "KGF Chapter 2":  "Action / Crime / Drama",
    "Baahubali 2":    "Action / Fight for the throne",
    "RRR":            "Action / Historical",
    "Pushpa":         "Action / Thriller",
    "3 Idiots":       "Comedy / Drama",
    "Dangal":         "Sports / Biography",
    "Uri":            "Action / War",
    "Kabir Singh":    "Romance / Drama",
    "Dilwale":        "Romance / Action",
    "Sultan":         "Sports / Drama",
}

all_movies = list(genres.keys())

# --- Cosine Similarity ---
def similarity(user_ratings, target):
    common = {m for m in user_ratings if m in target}

    if not common:
        return 0

    sum_sq1 = sum(user_ratings[m]**2 for m in common)
    sum_sq2 = sum(target[m]**2 for m in common)

    dot = sum(user_ratings[m] * target[m] for m in common)

    denom = sqrt(sum_sq1) * sqrt(sum_sq2)

    return dot / denom if denom else 0


# --- Recommendation Function ---
def recommend(user_ratings, top_n=3):
    scores = {}

    for name, rated in ratings.items():

        sim = similarity(rated, user_ratings)

        for movie, rating in rated.items():

            if movie not in user_ratings:
                scores[movie] = scores.get(movie, 0) + sim * rating

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked[:top_n]


# --- Find similar user ---
def find_similar_user(user_ratings):

    best_name = ""
    best_score = 0

    for name, rated in ratings.items():

        sim = similarity(rated, user_ratings)

        if sim > best_score:
            best_score = sim
            best_name = name

    return best_name


# --- Header ---
print("=" * 50)
print("  Recommendation System - CodSoft Task 3")
print("=" * 50)

print("\nAvailable Movies:\n")

for i, movie in enumerate(all_movies, 1):
    print(f"{i:>2}. {movie:<20} [{genres[movie]}]")


# --- User Ratings Input ---
print("\n" + "-" * 50)
print("Rate movies you have watched (1-5)")
print("Press Enter to skip a movie")
print("-" * 50 + "\n")

user_ratings = {}

for movie in all_movies:

    try:

        val = input(f"{movie} (1-5 or Enter to skip): ").strip()

        if val == "":
            continue

        rate = int(val)

        if 1 <= rate <= 5:
            user_ratings[movie] = rate

        else:
            print("Skipping — rating must be between 1 and 5")

    except ValueError:
        print("Skipping — invalid input")


# --- Show Results ---
print("\n" + "=" * 50)

if not user_ratings:

    print("No ratings given. Please rate at least one movie.")

else:

    print("\nYour Ratings:")

    for movie, rate in user_ratings.items():
        print(f"{movie}: {rate}/5")

    similar = find_similar_user(user_ratings)

    print(f"\nUser with similar taste: {similar}")

    results = recommend(user_ratings)

    print("\nTop Recommended Movies for You:\n")

    for i, (movie, score) in enumerate(results, 1):
        print(f"{i}. {movie:<20} [{genres[movie]}]  (Score: {score:.2f})")

print("\n" + "=" * 50)
print("Thank you for using the Movie Recommendation System!")
print("=" * 50)
