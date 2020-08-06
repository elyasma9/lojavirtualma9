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

## Rotas

```
api/ ^usuarios/
api/ ^usuarios/<pk>
api/ ^usuarios/<usuario_pk>/enderecos/
api/ ^usuarios/<usuario_pk>/enderecos/<pk>/
api/ ^usuarios/<usuario_pk>/pedidos/
api/ ^usuarios/<usuario_pk>/pedidos/<pk>/
api/ ^usuarios/<usuario_pk>/pedidos/<pedido_pk>)/enderecos/
api/ ^usuarios/<usuario_pk>/pedidos/<pedido_pk>/enderecos/<pk>/
admin/
```
