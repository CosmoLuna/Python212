from sqlalchemy import Column, Integer, String

from hwpackage.hwdatabase import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_name = Column(String(250), nullable=False)
    book_author = Column(String(250), nullable=False)
    year = Column(Integer)

    def __repr__(self):
        return f"Книга: (ID: {self.id}, Название: {self.book_name}, Автор: {self.book_author})"