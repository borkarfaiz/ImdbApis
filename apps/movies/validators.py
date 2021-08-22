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


def validate_genre_list(genres):
    if ',' in genres:
        genres = {genre.strip() for genre in genres.split(',')}
    else:
        genres = {genres.strip()}
    if not genres.issubset(Genres.set_of_genere):
        raise ValueError("Invalid genres")
    return list(genres)


def validate_imdb_score(score):
    if not isinstance(score, (float, int)):
        raise ValueError("Invalid Imdb rating")
    score = float(score)
    if not 0 <= score <= 10:
        raise ValueError("Invalid Imdb rating")
    return score


def validate_99popularity_range(values):
    try:
        from_, to_ = list(map(float, values.split(',')))
    except ValueError:
        raise ValueError("Invalid Range")
    if from_ > to_:
        raise ValueError("Invalid Range")
    if not 1 <= from_ <= 99 or not 1 <= to_ <= 99:
        raise ValueError("Invalid Range")
    return from_, to_


def validate_imdb_score_range(values):
    try:
        from_, to_ = list(map(float, values.split(',')))
    except ValueError:
        raise ValueError("Invalid Range")
    if from_ > to_:
        raise ValueError("Invalid Range")
    if not 0 <= from_ <= 10 or not 0 <= to_ <= 10:
        raise ValueError("Invalid Range")
    return from_, to_

