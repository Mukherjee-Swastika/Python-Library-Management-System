import json
import random
import string
from pathlib import Path


class Library:
    database = 'data.json'
    books_db = 'books.json'
    borrow_db = 'borrow.json'


    # -------- FILE HANDLING --------
    @classmethod
    def load_data(cls):
        if Path(cls.database).exists():
            with open(cls.database, 'r') as f:
                return json.load(f)
        return []

    @classmethod
    def save_data(cls, data):
        with open(cls.database, 'w') as f:
            json.dump(data, f, indent=4)


    # -------- GENERATE USER ID --------
    def user_id(cls):
        chars = random.choices(string.ascii_letters, k=3) + \
                random.choices(string.digits, k=3) + \
                random.choices("!@#$%^&*", k=1)
        random.shuffle(chars)
        return ''.join(chars)



    # -------- REGISTER --------
    @classmethod
    def register_id(cls, name, age, email, pin):
        data = cls.load_data()

        acc_no = cls.user_id()

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": acc_no
        }

        data.append(user)
        cls.save_data(data)

        return user, "registered successfully"


    # -------- LOGIN --------
    @classmethod
    def find_user(cls, reg_id, pin):
        data = cls.load_data()

        for user in data:
            if user['accountNo.'] == reg_id and user['pin'] == pin:
                return user

        return None


    # -------- VIEW BOOKS --------
    @classmethod
    def view_books(cls):
        if Path(cls.books_db).exists():
            with open(cls.books_db, 'r') as f:
                return json.load(f)
        return []


    # -------- SEARCH BOOK --------
    @classmethod
    def search_book(cls, keyword):
        books = cls.view_books()

        results = []

        for book in books:
            if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
                results.append(book)

        return results


    # -------- BORROW BOOK --------
    @classmethod
    def borrow_book(cls, user_id, book_id):

        if Path(cls.borrow_db).exists():
            with open(cls.borrow_db, 'r') as f:
                borrowed = json.load(f)
        else:
            borrowed = []

        borrowed.append({
            "user_id": user_id,
            "book_id": book_id
        })

        with open(cls.borrow_db, 'w') as f:
            json.dump(borrowed, f, indent=4)

        return "Book borrowed successfully"


    # -------- RETURN BOOK --------
    @classmethod
    def return_book(cls, user_id, book_id):

        if not Path(cls.borrow_db).exists():
            return "No borrowed books"

        with open(cls.borrow_db, 'r') as f:
            borrowed = json.load(f)

        borrowed = [b for b in borrowed if not (b["user_id"] == user_id and b["book_id"] == book_id)]

        with open(cls.borrow_db, 'w') as f:
            json.dump(borrowed, f, indent=4)

        return "Book returned successfully"


    # -------- VIEW MY BOOKS --------
    @classmethod
    def my_books(cls, user_id):

        if not Path(cls.borrow_db).exists():
            return []

        with open(cls.borrow_db, 'r') as f:
            borrowed = json.load(f)

        my = [b for b in borrowed if b["user_id"] == user_id]

        return my