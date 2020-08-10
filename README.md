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
### Rota do Admin
```http://localhost:8000/admin/```
### Principais rotas de acesso

| URI                                                                                | Tipos de Requisição           |
| ---------------------------------------------------------------------------------- | ----------------------------- |
| http://localhost:8000/api/usuarios/<id>                                            | `POST` `GET` `PATCH` `DELETE` |
| http://localhost:8000/api/produtos/<id>                                            | `POST` `GET` `PATCH` `DELETE` |
| http://localhost:8000/api/usuarios/<pk>/set_password                               | `POST`                        |
| http://localhost:8000/api/usuarios/<usuario_id>/enderecos/<id>                     | `POST` `GET` `PATCH` `DELETE` |
| http://localhost:8000/api/usuarios/<usuario_id>/pedidos/<id>                       | `POST` `GET` `PATCH` `DELETE` |
| http://localhost:8000/api/usuarios/<usuario_id>/pedidos/<pedido_id>/enderecos/<id> | `POST` `GET` `PATCH` `DELETE` |

<hr />

### Request `api/usuarios/` - `POST`

```json
{
  "nome": "Arnaldo",
  "sobrenome": "Sobral",
  "email": "arnaldo@chef.com",
  "password": "123456",
  "cpf": "07240009809",
  "rg": "34043567",
  "telefone": "79998787766",
}
```

### Response `api/usuarios/`

```json
{
  "nome": "Arnaldo",
  "sobrenome": "Sobral",
  "email": "arnaldo@chef.com",
  "password": "pbkdf2_sha256$150000$HKcBhlSUbx0y$GjophIWCwyCuEGtJ8dslq1E03WHMtqsWjYuGfljj8Cs=",
  "cpf": "07240009809",
  "rg": "34043567",
  "telefone": "79998787766",
}
```
<hr />
