import streamlit as st
from library import Library

st.title("📚 Library Management System")

menu = ["Register", "Login"]

if "user" not in st.session_state:
    choice = st.sidebar.selectbox("Menu", menu)

    # ---------------- REGISTER ----------------
    if choice == "Register":

        st.subheader("User Registration")

        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1)
        email = st.text_input("Email")
        pin = st.text_input("PIN", type="password")

        if st.button("Register"):

            user, msg = Library.register(name, age, email, pin)
            st.success(msg)
            st.write("Your ID:", user["id"])

    # ---------------- LOGIN ----------------
    elif choice == "Login":

        st.subheader("Login")

        user_id = st.text_input("User ID")
        pin = st.text_input("PIN", type="password")

        if st.button("Login"):

            user = Library.login(user_id, pin)

            if user:
                st.session_state.user = user
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid ID or PIN")

# ---------------- AFTER LOGIN ----------------
else:

    user = st.session_state.user

    st.sidebar.write(f"Welcome {user['name']}")

    menu = [
        "View Books",
        "Search Books",
        "Borrow Book",
        "Return Book",
        "My Books",
        "Logout"
    ]

    choice = st.sidebar.selectbox("Menu", menu)

    # ---------------- VIEW BOOKS ----------------
    if choice == "View Books":

        st.subheader("All Books")

        books = Library.view_books()

        if books:
            st.table(books)
        else:
            st.info("No books available")

    # ---------------- SEARCH BOOKS ----------------
    elif choice == "Search Books":

        st.subheader("Search Book")

        keyword = st.text_input("Enter title or author")

        if st.button("Search"):

            results = Library.search(keyword)

            if results:
                st.table(results)
            else:
                st.warning("No books found")

    # ---------------- BORROW BOOK ----------------
    elif choice == "Borrow Book":

        st.subheader("Borrow Book")

        book_id = st.text_input("Enter Book ID")

        if st.button("Borrow"):

            Library.borrow(user["id"], book_id)

            st.success("Book borrowed successfully")

    # ---------------- RETURN BOOK ----------------
    elif choice == "Return Book":

        st.subheader("Return Book")

        book_id = st.text_input("Enter Book ID")

        if st.button("Return"):

            Library.return_book(user["id"], book_id)

            st.success("Book returned successfully")

    # ---------------- MY BOOKS ----------------
    elif choice == "My Books":

        st.subheader("My Borrowed Books")

        books = Library.my_books(user["id"])

        if books:
            st.table(books)
        else:
            st.info("You have not borrowed any books")

    # ---------------- LOGOUT ----------------
    elif choice == "Logout":

        del st.session_state.user
        st.success("Logged out")
        st.rerun()