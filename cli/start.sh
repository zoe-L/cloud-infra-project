gcloud container clusters create zoe-li-cluster \
  --scopes "cloud-platform" \
  --num-nodes 2
gcloud config set container/cluster zoe-li-cluster
gcloud container clusters get-credentials zoe-li-cluster
kubectl create -f jupyter-notebook.yaml


echo 'Welcome to Big Data Processing Application'
echo 'Please type the number that corresponds to which application you would like to run:'
echo '1. Apache Hadoop'
echo '2. Apache Spark'
echo '3. Jupyter Notebook'
echo '4. SonarQube and SonnarScanner'
echo 'Type the number here >  '
read x
python start.py ${x}


