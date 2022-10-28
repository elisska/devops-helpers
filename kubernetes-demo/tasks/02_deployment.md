# Working with deployments

Deployments are k8s-native way to manage containerized applications.

* Deployment specifies desired state for your application
* Deployment ensures your application is up and running as per defined configuration even if some Pod fails
* Using Deployment, you can specify required # of replicas for Pods, do rolling updated for your Pods, etc….
* Can be autoscaled with HorizontalPodAutoscaling
* In Deployment manifest, you provide Pod template as a spec for your Pods 
* Deployment manages automatically created ReplicaSet, and ReplicaSet manages Pods
* You should use Deployment for stateless applications!

## Working with deployments

```
# show available options for create
kubectl create
#Note: no pod object in available commands!! This is because: pod is the smallest unit, however, you usually DO NOT create PODS, your create DEPLOYMENTS. Deployment - abstraction over pods

# create deployment
kubectl create deployment nginx-deployment --image=nginx

# get deployment, pods, replicasets
kubectl get all
#Note: you should never create replicaset! You operate on Deployment level.
#Levels of abstraction:
#- You create deployment
#- Deployment manages ReplicaSet
#- ReplicaSet manages Pods. Pod is the abstraction on top of container

# edit deployment and set image to nginx:1.16
kubectl edit deployment nginx-deployment
#Note: this provides auto-generated config file with default values

# edit deployment and set replicas to 2
kubectl edit deployment nginx-deployment
#Note: once edited, new pod will be created

# delete one pod from deployment
kubectl delete pod <pod name>
#Note: once deleted, deployment will still add another replica
```

## Rollback the last update
```
# show help
kubectl rollout --help

# get status and history
kubectl rollout status deployment nginx-deployment
kubectl rollout history deployment nginx-deployment

# in another terminal watch rollback process
watch kubectl get all
  
# rollback
kubectl rollout undo deployment nginx-deployment
```

## Working with YAML files (manifests):
```
# get entire Deployment yaml
kubectl get deployment nginx-deployment -o yaml
#Note: this gets info from etcd and provides full manifest with status field

# get Deployment yaml to edit further
kubectl create deployment nginx-deployment1 --image=nginx --dry-run=client -o yaml > nginx-deployment1.yaml

# run apply
kubectl apply -f nginx-deployment1.yaml
#Note: this creates deployment

# save to file & edit existing deploynment
kubectl get deployment nginx-deployment -o yaml > nginx-deployment.yaml

# run apply to edit existing deployment
kubectl apply -f nginx-deployment.yaml

# delete all deployments
kubectl delete --all deployment 
```







