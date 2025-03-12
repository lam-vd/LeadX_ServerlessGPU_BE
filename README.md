# Serverless-GPU-API

Django

- Django v5
- Django Rest Framework
- Django Rest Framework Simple JWT
- PyTest

Postgress

- Docker v16.1 alpine image



### Useful Commands

Edit And Rename .env-example

```sh

cp .env-example .env.dev

```

Build containers. Add -up flag to bring services up after build.

```sh

docker compose build

```

Bring containers up. Add -d flag to run output detached from current shell.

```sh

docker compose up 

```

Bring containers down. Add -v flag to also delete named volumes

```sh

docker compose down

```

View logs by service name.

```sh

docker compose logs <service-name>

```

Enter shell for specified container (must be running)

```sh

docker exec -it <container-name> sh

```

### Containers, Services and Ports

| Container  | Service | Host Port | Docker Port |
| ---------- | ------- | --------- | ----------- |
| dev-django | django  | 8001      | 8000        |
| dev-db     | db      | 5432      | 5432        |
