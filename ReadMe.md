# Project Checkpoint 1
## Obtaining Docker images
### Command Line App (Included)
https://hub.docker.com/repository/docker/zoexli/projectcli

### Apache Hadoop
Master: https://hub.docker.com/r/bde2020/hadoop-namenode/tags
Worker: https://hub.docker.com/r/bde2020/hadoop-datanode

### Apache Spark
https://hub.docker.com/r/bitnami/jupyterhub

### Jupyter Notebook
https://hub.docker.com/r/bitnami/jupyterhub

### SonarQube and SonarScanner (Included)
https://hub.docker.com/repository/docker/zoexli/sonarkit


## Start GKE Cluster
run the following command to create a Kubernetes cluster
(Screeshot 1)
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

## Deploy projectcli to GKE in container regitry
(Screeshot 2)
