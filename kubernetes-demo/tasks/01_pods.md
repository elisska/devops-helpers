# Working with pods

Pod is:
* a core object of Kubernetes
* smallest deployable unit
* abstraction on top of containers

## Some theory
* There is usually 1 container per Pod
* Each Pod has its own IP address
* Pod is ephemeral and can die at any time
* Not restarted automatically if killed
* _You should NOT deploy Pods directly, do this for test only!_
* K8s network does magic around pod-to-pod communication

## Working with pods

```
# create nginx pod from nginx:latest image
kubectl run nginx --image=nginx
# check pod is creating
kubectl get pods
# check extended information about the pod
kubectl get pods -o wide
# check pod object definition
kubectl get pods nginx -o yaml
# describe nginx pod and check events for the pod 
kubectl describe pods nginx
# edit nginx pod and change image version to 1.16
kubectl edit pods nginx
# describe nginx pod and check events for the pod 
kubectl describe pods nginx
```

## Troubleshoot pods

```
# create mysql pod from mysql image
kubectl run mysql --image=mysql
# describe mysql pod and check events for the pod 
kubectl describe pods mysql
# get pod logs
kubectl logs mysql
# Log in to container in pod
kubectl exec -it mysql -- bash
# Starting new pod with interactive shell
kubectl run -it mysql1 --image=mysql -- bash
```

## Deleting pods

```
# delete pod nginx and mysql
kubectl delete pods nginx
kubectl delete pods mysql
# delete all pods
kubectl delete --all pods
# check pods were not recreated
kubectl get pods
```

