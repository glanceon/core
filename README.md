# Core

A project to showcase my knowledge of django so far..

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```
Setup your os variables in .env file and PostgreSQL database with user

Install redis on Linux
```bash
sudo apt-get install redis
```
or Windows https://github.com/tporadowski/redis/releases

Install Java 8+, Elasticsearch & create superuser like so
```bash
elasticsearch-users useradd user -p password -r superuser
```

## Running the App

Run Redis
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

Run ES Server
```bash
elasticsearch
```

Rebuild ES index
```bash
python manage.py search_index --rebuild
```

Run the app
```bash
python manage.py runserver
```

## Postman

https://www.getpostman.com/collections/eedd91e8f9e4217f1bae
