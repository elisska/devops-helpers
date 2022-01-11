# Sample application

This is a sample TODO application from [Docker Getting Started Tutorial](https://docs.docker.com/get-started/02_our_app/)

It uses MySQL database on the backend.

NodeJS application image exists in my personal [repository](https://hub.docker.com/repository/docker/elisska/devops-helpers) as a separate tag. 

It has been built by these commands:

```
docker build -f Dockerfile -t elisska/devops-helpers:nodejs-mysql-demo-app .
docker push elisska/devops-helpers:nodejs-mysql-demo-app
```

Run application via `docker compose`:

```
docker-compose up -d
```

Access application at `http://localhost:3000`


