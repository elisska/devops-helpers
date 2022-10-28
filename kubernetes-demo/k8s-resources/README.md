# NodeJS + MySQL Demo application deployment to Kubernetes

This directory contains set of Kubernetes object/resources definitions to deploy [Sample NodeJS+MySQL Application](https://github.com/elisska/devops-helpers/tree/main/nodejs-mysql-demo-app) to Kubernetes.

These resources will be created:
* MySQL deployment
* MySQL internal service
* NodeJS application deployment
* NodeJS application service (external LoadBalancer)
* Secret to store MySQL credentials
* ConfigMap to store application configuration, i.e. MySQL connection details
* Persistent Volume Claim to be used in MySQL deployment

Deploy this application to Minikube or any other cluster:
```
kubectl apply -f .
```

Serve proxy to external NodeJS service (minikube example):
```
minikube tunnel
```

Open on `http://localhost:3000/`
