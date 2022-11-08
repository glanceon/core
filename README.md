# Core

A project to showcase my knowledge of django so far..

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```
Setup your os variables and PostgreSQL database with user

Install redis on Linux
```bash
sudo apt-get install redis
```
or Windows https://github.com/tporadowski/redis/releases

## Running the App

Run Redis on linux
```bash
redis-server
```

Run celery
```bash
celery -A core.celery worker --pool=solo -l info
```
Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

Run the app
```bash
python manage.py runserver
```
