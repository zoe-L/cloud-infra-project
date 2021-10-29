# Project Checkpoint 1
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

### SonarQube and SonarScanner (Included)
https://hub.docker.com/repository/docker/zoexli/sonarkit


## Start GKE Cluster
run the following command to create a Kubernetes cluster

![Create Cluster](screenshots/1.PNG?raw=true "create_cluster")

gcloud container clusters create \
 --machine-type n1-standard-2 \
 --num-nodes 2 \
 --zone us-central1-a \
 --cluster-version latest \
cloud-infra-project-cluster


## Pull and retag all images
Sample commands: 

docker pull zoexli/projectcli

docker tag zoexli/projectcli gcr.io/cloud-infra-project/projectcli

docker push gcr.io/cloud-infra-project/projectcli

## Deploy projectcli and other images to GKE in container regitry
![Deploy Image](screenshots/2.PNG?raw=true "deploy_image")

## Screenshot of all containers running
![All Pods](screenshots/6.PNG?raw=true "all_pods")

## Screenshot of CLI runing
![CLI](screenshots/5.PNG?raw=true "cli")
