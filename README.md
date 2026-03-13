# 📚 Library Management System (Streamlit & Console)

A simple **Library Management System** built using **Python** that allows users to register, log in, browse books, search for books, borrow books, return books, and view their borrowed books.

The project can be run in two ways:

* **Streamlit Web Application**
* **Console (Terminal) Version**

The system uses **JSON files for data storage**, making it lightweight and easy to run without a database.

---

## 🚀 Features

* 👤 **User Registration**
* 🔐 **User Login**
* 📖 **View Available Books**
* 🔎 **Search Books**
* 📚 **Borrow Books**
* 🔁 **Return Books**
* 📑 **View My Borrowed Books**
* 🚪 **Logout System**

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **JSON (for data storage)**

---

## 📂 Project Structure

```
Library-Management-project
│
├── app.py          # Streamlit user interface
├── library.py      # Core library logic
├── normal.py         # Console version of the program
│
├── data.json       # User data
├── books.json      # Books database
└── borrow.json     # Borrowed books records
```

---

## ⚙️ Running the Project

### 1️⃣ Run in Console

```
python normal.py
```

### 2️⃣ Run as a Web App (Streamlit)

Install Streamlit:

```
pip install streamlit
```

Run the app:

```
streamlit run app.py
```

---

## 🎯 Purpose of the Project

This project demonstrates:

* Basic **Python programming**
* **Object-Oriented Programming (OOP)**
* **File handling using JSON**
* Building a **simple web application using Streamlit**

---

## 👩‍💻 Author

Developed by **Swastika Mukherjee**
