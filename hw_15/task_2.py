from typing import List


class Author:
    def __init__(self, name: str, country: str, birthday: int) -> None:
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = list()


    def _add_book(self, book: object) -> None:
        self.books.append(book)


    def __repr__(self):
        return f"Author(name={self.name}, country={self.country}, birthdate={self.birthday}, books={self.books})."


    def __str__(self):
        return f"{self.name} was born in {self.country} in {self.birthday}!"


class Book:
    total_book = 0


    def __init__(self, name: str, year: int, author: Author) -> None:
        self.name = name
        self.year = year
        self.author = author
        Book.total_book += 1


    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author.name}.)"


    def __str__(self):
        return f"Book {self.name} published by {self.year} by {self.author.name}."


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books = list()
        self.authors = list()


    def new_book(self, name: str, year: int, author: Author) -> object:
        book = Book(name, year, author)
        self.books.append(book)
        author._add_book(book)
        if book.author not in self.authors:
            self.authors.append(book.author)
        return book


    def group_by_author(self, author: Author) -> List:
        if not isinstance(author, Author):
            raise ValueError("There is no such author")
        result = [book for book in self.books if book.author == author]
        return result


    def group_by_year(self, year: int) -> List:
        if not isinstance(year, int):
            raise ValueError("Incorrect year format enter a whole number")
        result = [book for book in self.books if book.year == year]
        return result


    def __repr__(self):
        return f"Library name is '{self.name}'."


    def __str__(self):
        return f"Library name is '{self.name}'."


library = Library("The Vernadsky National Library of Ukraine")

jo_nesbo = Author("Jo Nesbø", "Norway", 1960)
philip_k_dick = Author("Philip K. Dick", "USA", 1928)
yuval_noah_harari = Author("Yuval Noah Harari", "Israel", 1976)

library.new_book("The Bat", 1997, jo_nesbo)
library.new_book("The Snowman", 2007, jo_nesbo)
library.new_book("Police", 2013, jo_nesbo)
library.new_book("The Thirst", 2017, jo_nesbo)
library.new_book("The Man in the High Castle", 1961, philip_k_dick)
library.new_book("Do Androids Dream of Electric Sheep?", 1966, philip_k_dick)
library.new_book("Sapiens: A Brief History of Humankind", 2017, yuval_noah_harari)