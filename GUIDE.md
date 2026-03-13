README.md Or GUIDE.md
#  Movie Recommendation-System - CODSOFT AI Internship Task 3

This project implements a simple **movie recommendation system** for Indian movies using **Collaborative Filtering** and **Cosine Similarity**. Users can rate movies they have watched, and the system will recommend other movies based on the preferences of users with similar tastes.

---

## Features

- Users can rate a list of popular Indian movies (scale 1-5).  
- Identifies a user with similar movie preferences.  
- Provides top movie recommendations using collaborative filtering.  
- Displays movie genres along with recommendations.  

---

## Movies Included

| Movie           | Genre                     |
|-----------------|---------------------------|
| KGF Chapter 2   | Action / Crime / Drama    |
| Baahubali 2     | Action / Fight for the throne |
| RRR             | Action / Historical       |
| Pushpa          | Action / Thriller         |
| 3 Idiots        | Comedy / Drama            |
| Dangal          | Sports / Biography        |
| Uri             | Action / War              |
| Kabir Singh     | Romance / Drama           |
| Dilwale         | Romance / Action          |
| Sultan          | Sports / Drama            |

---

## How It Works

1. **Collect User Ratings:** The user inputs their ratings for the available movies.  
2. **Compute Similarity:** The system uses **cosine similarity** to compare the user’s ratings with other users in the dataset.  
3. **Find Similar Users:** Determines the user with the closest taste in movies.  
4. **Recommend Movies:** Generates top N movie recommendations not yet rated by the user.

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/ganesmpsmg/Recommendation-system.git
cd Recommendation-system

Install dependencies:

pip install -r requirements.txt

Run the program:

python recommendation-system.py

Follow the prompts to rate movies and get recommendations.

Example Output
Your Ratings:
KGF Chapter 2: 5/5
3 Idiots: 4/5

User with similar taste: Ganesh

Top Recommended Movies for You:
1. Baahubali 2       [Action / Fight for the throne]  (Score: 9.20)
2. RRR               [Action / Historical]           (Score: 8.50)
3. Pushpa            [Action / Thriller]             (Score: 7.80)
Requirements

Python 3.7+

Libraries:

math (built-in)

No external packages are required as this is a simple collaborative filtering implementation.

Author

Ganesh MP
CODSOFT AI Internship – Task 3
github repository: https://github.com/ganeshmpsmg/ganeshmpsmg.github.io
