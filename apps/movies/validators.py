from .constants import Genres


def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Invalid name")
    name = name.strip()
    if name == "":
        raise ValueError("Invalid name")
    return name


def validate_99popularity(score):
    """
    In this function I have assumed 99 popularity has the range
    of 1-99
    """
    if not isinstance(score, (float, int)):
        raise ValueError("Invalid 99popularity")
    score = float(score)
    if not 1 <= score <= 99:
        raise ValueError("Invalid 99popularity")   
    return score


def validate_genre(genres):
    if not isinstance(genres, list):
        raise ValueError("Invalid genres")
    genre_set = set(genres)
    if not genre_set.issubset(Genres.set_of_genere):
        raise ValueError("Invalid genres")
    return genres


def validate_imdb_score(score):
    if not isinstance(score, (float, int)):
        raise ValueError("Invalid Imdb rating")
    score = float(score)
    if not 0 <= score <= 10:
        raise ValueError("Invalid Imdb rating")
    return score
