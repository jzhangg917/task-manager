# Task Management Application

Welcome to the Task Management Application! This project demonstrates a simple task management system with user registration, authentication, and task tracking features.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Registration: New users can register with a unique username and password.
- User Authentication: Registered users can securely log in to the application.
- Task Management: Logged-in users can add, complete, and view tasks.
- Secure Data Storage: User data, tasks, and completed tasks are stored securely in an SQLite database.
- HTTPS Encryption: The application uses HTTPS for secure communication.
- Error Handling: Comprehensive error handling ensures smooth user experience and data integrity.

## Getting Started

To get started with the Task Management Application, follow these steps:

### Installation

1. Clone this repository to your local machine using:

```bash
git clone https://github.com/your-username/task-management.git
```

2. Navigate to the project directory:
```bash
cd task-management
```

3. Install the required dependencies
```bash
pip install -r requirements.txt
```

4. Intialize the SQLite database:
```bash
python initialize_database.py
```

5. Run the application:
```bash
python main.py
```
