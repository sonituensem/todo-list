# Todo List

A simple Todo List application built with Django.

## Features

* Create, update and delete tasks
* Mark tasks as completed
* Add deadlines
* Create and manage tags
* Assign multiple tags to tasks
* Sort tasks by status and creation date

## Technologies

* Python
* Django
* SQLite
* Bootstrap 5

## Run locally

```bash
git clone https://github.com/sonituensem/todo-list.git
cd todo-list

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Tests

```bash
python manage.py test
```
