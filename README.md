# Loja Virtual
Treinamento de nivelamento ma9.

## Setup

build and up containers

```
docker-compose up --build -d
```

run migrations

```
docker-compose run web python manage.py migrate
```

create a user for admin

```
docker-compose run web python manage.py createsuperuser
```
