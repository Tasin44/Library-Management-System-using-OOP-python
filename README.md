# 📚 Terminal-Based Library Management System

This is a **Python-based terminal application** designed to simulate a basic Library Management System using **Object-Oriented Programming (OOP)**. It supports core library operations such as book management, user interactions, and real-time book borrowing and returning.

---

## 🚀 Features

### ✅ Book Management (Librarian Access)
- **Add a Book**
  - Input book title and author
  - Stored as a `Book` object in the library system
- **Remove a Book**
  - Remove book by title
  - Only if it exists in the available books list
- **Display Available Books**
  - Lists all books currently available for borrowing

### 👤 Member Operations
- **Borrow a Book**
  - Members provide name, ID, and book title
  - Book must exist in the library
  - Automatically moves the book to the member's borrowed list
- **Return a Book**
  - Members return a previously borrowed book
  - Returned books are added back to the library's available list

---

## 🧱 Project Structure

```
Library Management System/
│
├── main.py             # Entry point of the application
├── library.py          # Contains the Library class and all book tracking logic
├── book.py             # Defines the Book class
├── person.py           # Base class for Librarian and Member
├── librarian.py        # Librarian class to manage books
└── member.py           # Member class to borrow/return books
```

---

## 💡 Technologies Used

- **Python 3**
- Object-Oriented Programming (OOP)
- Command-line interface (CLI)

---

## 📝 How to Run

1. Clone or download this repository.
2. Open your terminal and navigate to the project directory.
3. Run the program using:
   ```bash
   python main.py
   ```
4. Follow the prompts to interact with the system.

---

## ⚠️ Notes

- Book titles are case-sensitive when borrowing/returning.
- Each session starts with an empty library (no persistent storage yet).
- Member borrowing history is stored only during the session runtime.

---

## 📈 Future Enhancements

- Add file-based or database storage to preserve data across sessions
- Improve input validation and error handling
- Add login system for members and librarians
- GUI integration using `Tkinter` or `PyQt`

---

## 🤝 Author

Developed by **Tasin Mahmud**  
Feel free to fork, improve, and use this project in your own way!
