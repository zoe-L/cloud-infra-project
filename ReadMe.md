# Course Project
## Code Walk-through and demo
https://www.youtube.com/watch?v=0lnNO4_vp5o

## Obtaining Docker images
### Command Line App (Included)
https://hub.docker.com/repository/docker/zoexli/projectcli

### Apache Hadoop
Master: https://hub.docker.com/r/bde2020/hadoop-namenode/tags

Worker: https://hub.docker.com/r/bde2020/hadoop-datanode

### Apache Spark
https://hub.docker.com/r/bitnami/spark

### Jupyter Notebook
https://hub.docker.com/r/jupyter/base-notebook/

### SonarQube and SonarScanner
https://hub.docker.com/r/bitnami/sonarqube


## Start GKE Cluster
run the following command to create a Kubernetes cluster

```
gcloud container clusters create \
 --machine-type n1-standard-2 \
 --num-nodes 2 \
 --zone us-central1-a \
 --cluster-version latest \
nginx-1-cluster
```

![Create Cluster](screenshots/1.PNG?raw=true "create_cluster")


## Pull and retag all images
Sample commands: 
```
docker pull zoexli/projectcli
docker tag zoexli/projectcli gcr.io/cloud-infra-project/projectcli
docker push gcr.io/cloud-infra-project/projectcli
```

## Deploy projectcli and other images to GKE in container regitry
Deploy containers and services using the .yaml files provided. There are in total 3 steps for deploying each application.
1. create a local .yaml file using cloud shell and nano editor for the **main application**, and paste the content of .yaml files from this repository into the new local file.
2. deploy the container using kubectl.
3. repeat step 1 and 2 for the **load balancing service** to expose the application*

*It may be necessary to create a firewall rule, please refer to https://towardsdatascience.com/running-jupyter-notebook-in-google-cloud-platform-in-15-min-61e16da34d52 for details

Sample commands:
```
gcloud container clusters get-credentials nginx-1-cluster --zone us-central1-a --project cloud-infra-project
nano jupyter-notebook.yaml
kubectl create -f jupyter-notebook.yaml
nano jupyter-notebook-service.yaml
kubectl create -f jupyter-notebook-service.yaml
```

Outcome:
![kubectl create](screenshots/kubectl-create.PNG?raw=true "kubectl_create")


For Jupyter Notebook and Sonarqube, it is necessary to connect to the containers and do some setup work using bash.
The commands to use are noted below.


For Jupyter Notebook:
```
kubectl get pods -o name
kubectl exec -it <your-jupyter-pod-name> bash
* After exec into Jupyter pod bash
jupyter notebook password
jupyter notebook
```

For Sonarqube:
```
* cd into /opt
cd ..
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744.zip
unzip sonar-scanner-cli-4.0.0.1744.zip
export PATH="/opt/sonar-scanner-4.0.0.1744/bin:$PATH"
sonar-scanner -Dsonar.login='admin' -Dsonar.password='admin' -Dsonar.projectKey='14848project' -Dsonar.host.url='http://localhost:9000'
```
![Deployment_1](screenshots/deployment-1.PNG?raw=true "deployment1")
![Deployment_2](screenshots/deployment-2.PNG?raw=true "deployment2")
![Deployment_3](screenshots/deployment-3.PNG?raw=true "Deployment3")
![Deployment_4](screenshots/deployment-4.PNG?raw=true "Deployment_4")
![Deployment_5](screenshots/deployment-5.PNG?raw=true "Deployment_5")
![Deployment_6](screenshots/deployment-6.PNG?raw=true "Deployment_6")
![Deployment_7](screenshots/deployment-7.PNG?raw=true "Deployment_7")

Finally, after all applications have been successfully deployed, run the cli using the following command:
```
kubectl exec -it <your-cli-pod-name> -- /bin/bash ./start.sh
```

## Screenshot of all containers running


![All Pods](screenshots/6.PNG?raw=true "all_pods")

## Screenshot of CLI runing


![CLI](screenshots/5.PNG?raw=true "cli")
