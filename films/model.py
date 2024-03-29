import pickle
import os.path


class Film:
    def __init__(self, title, genre, director, year, duration, studio, cast):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.cast = cast

    def __str__(self):
        return f"{self.title} ({self.year})"


class FilmModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.films = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            'название фильма': film.title,
            'жанр': film.genre,
            'режиссер': film.director,
            'год выпуска': film.year,
            'длительность': film.duration,
            'студия': film.studio,
            'актеры': film.cast
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.films, f)
