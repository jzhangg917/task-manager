import json
from collections import deque
from datetime import datetime
import sqlite3
import hashlib

class TaskManager:
    def __init__(self, username):
        self.username = username
        self.tasks = []
        self.completed_tasks = set()
        self.task_queue = deque()
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()
        
        # Load tasks for the user
        cursor.execute("SELECT * FROM tasks WHERE username = ?", (self.username,))
        tasks = cursor.fetchall()
        for task in tasks:
            task_id, _, description, priority, due_date, completed = task
            task_dict = {
                "id": task_id,
                "description": description,
                "priority": priority,
                "due_date": due_date,
                "completed": completed
            }
            self.tasks.append(task_dict)
            if completed:
                self.completed_tasks.add(task_id)
        
        conn.close()

    # ... Other methods ...

# Initialize SQLite database and user authentication functions
def initialize_database():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        description TEXT,
                        priority INTEGER,
                        due_date DATE,
                        completed INTEGER DEFAULT 0
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password_hash TEXT
                    )''')

    conn.commit()
    conn.close()

def register_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        print("Username already exists.")
    else:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print("Registration successful.")

    conn.close()

def authenticate_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def main():
    initialize_database()

    while True:
        print("\n1. Register")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticate_user(username, password):
                task_manager = TaskManager(username)
                while True:
                    print("\n1. Add Task")
                    print("2. Complete Task")
                    print("3. View Tasks")
                    print("4. View Pending Tasks")
                    print("5. View Overdue Tasks")
                    print("6. Log Out")
                    choice = input("Enter your choice: ")

                    # ... Implement menu options for TaskManager ...

                    if choice == "6":
                        print("Logging out.")
                        break
            else:
                print("Invalid username or password.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
