#Problem 7: Best Movie Genre
'''Imagine you're contributing to a move recommendation 
engine, and you're tasked with writing a function named 
most_popular_genre() that returns the genre with the highest 
average rating across all movies.

The function takes in a list of dictionaries named movies 
as a parameter. Each dictionary represents data associated 
with a movie, including its title, genre, and rating.
 The function calculates the average rating for each genre 
 and returns the genre with the highest average rating.

def most_popular_genre(movies):
    pass
Example Usage:

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))
Example Output: Science Fiction

'''

def most_popular_genre(movies):
    """
    Returns the genre with the highest average rating 
    from a list of dictionaries representing movies.
    Each dictionary contains the movie's title, genre,
      and rating.
    """
    genre_ratings = {}
    genre_counts = {}
    for movie in movies:
        curr_genre = movie['genre']
        if curr_genre not in genre_ratings:
            genre_ratings[curr_genre] = movie['rating']
            genre_counts[curr_genre] = 1
        else:
            genre_ratings[curr_genre] += movie['rating']
            genre_counts[curr_genre] += 1

    highest_avg_rating = 0
    most_popular = None
    for genre in genre_ratings:
        avg_rating = genre_ratings[genre] / genre_counts[genre]
        if avg_rating > highest_avg_rating:
            highest_avg_rating = avg_rating
            most_popular = genre

    return most_popular

# def most_popular_genre(movies):
#     high = movies[0]
#     for mov in movies[1:]:
#         if mov["rating"] > high["rating"]:
#             high = mov
#     return high["genre"]

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))