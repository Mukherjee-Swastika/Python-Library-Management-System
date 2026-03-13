import json
import random
import string
from pathlib import Path
from unittest import result


class Library:
    users_db = "data.json"
    books_db = "books.json"
    borrow_db = "borrow.json"

    @classmethod
    def load(cls, file):
        if Path(file).exists():
            with open(file, "r") as f:
                return json.load(f)
        return []

    @classmethod
    def save(cls, file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def generate_id(cls):
        return ''.join(random.choices(string.digits, k=6))

    # REGISTER
    @classmethod
    def register(cls, name, age, email, pin):
        users = cls.load(cls.users_db)

        user = {
            "id": cls.generate_id(),
            "name": name,
            "age": age,
            "email": email,
            "pin": pin
        }

        users.append(user)
        cls.save(cls.users_db, users)

        return user

    # LOGIN
    @classmethod
    def login(cls, user_id, pin):
        users = cls.load(cls.users_db)

        for user in users:
            if user["id"] == user_id and user["pin"] == pin:
                return user
        return None

    # VIEW BOOKS
    @classmethod
    def view_books(cls):
        return cls.load(cls.books_db)

    # SEARCH
    @classmethod
    def search(cls, keyword):
        books = cls.load(cls.books_db)
        return [
            b for b in books
            if keyword.lower() in b["title"].lower()
            or keyword.lower() in b["author"].lower()
        ]

    # BORROW
    @classmethod
    def borrow(cls, user_id, book_id):

        borrowed = cls.load(cls.borrow_db)

        borrowed.append({
        "user_id": user_id,
        "book_id": book_id
    })

        cls.save(cls.borrow_db, borrowed)

    # RETURN
    @classmethod
    def return_book(cls, user_id, book_id):

        borrowed = cls.load(cls.borrow_db)

        new_list = []

        for record in borrowed:
            if not (record["user_id"] == user_id and record["book_id"] == book_id):
               new_list.append(record)

            cls.save(cls.borrow_db, new_list)

    # MY BOOKS
    @classmethod
    def my_books(cls, user_id):

        borrowed = cls.load(cls.borrow_db)
        books = cls.load(cls.books_db)

        my_books = []

        for b in borrowed:
             if str(b["user_id"]) == str(user_id):

                 for book in books:
                    if str(book["id"]) == str(b["book_id"]):
                        my_books.append(book)

        return my_books

            