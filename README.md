# Library Management System

A simple Library Management System built with Django.

## Features

* Display list of all books
* Display details of a specific book
* Add new books
* Edit existing books
* Store book information including:

  * Title
  * Author
  * Publication Date
  * ISBN
* Author management (Bonus Section)

## Technologies Used

* Python
* Django
* SQLite

## Project Structure

```
library_project/
│
├── library_project/
│
├── books/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       ├── book_list.html
│       ├── book_detail.html
│       ├── book_form.html
│       └── author_add.html
│
└── db.sqlite3
```

## Models

### Book

| Field          | Type                   |
| -------------- | ---------------------- |
| title          | CharField              |
| author         | CharField / ForeignKey |
| date_published | DateField              |
| isbn           | CharField              |

### Author (Bonus)

| Field       | Type         |
| ----------- | ------------ |
| first_name  | CharField    |
| last_name   | CharField    |
| age         | IntegerField |
| books_count | IntegerField |

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project directory:

```bash
cd library_project
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install django
```

Apply migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

## Available Pages

| URL              | Description  |
| ---------------- | ------------ |
| /                | Book List    |
| /book/add/       | Add Book     |
| /book/<id>/      | Book Details |
| /book/edit/<id>/ | Edit Book    |
| /author/add/     | Add Author   |

## Author

Developed as a Django educational project.
