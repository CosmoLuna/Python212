from faker import Faker

from hwpackage.hwdatabase import create_db, Session
from hwpackage.books import Book


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    books_names = ['Волшебники', 'Программирование для начинающих', 'Математика для школьников', 'Приключения Тима', 'Кот и щенок']
    faker = Faker('ru_RU')
    session.commit()

    for i in range(5):
        book_id = i + 1
        book_author = faker.name()
        year = faker.random.randint(1990, 2023)
        book = Book(book_id, books_names, book_author, year)
        session.add(book)

    session.commit()
    session.close()
