# software_containerization_G43


## Diagram


* Sequence Diagram
<img width="954" alt="image" src="https://github.com/calvinhaooo/software_containerization_G43/assets/145342600/fee6a71f-241b-4698-a1ec-4684b3217f14">

* Class Diagram

![image](https://github.com/calvinhaooo/software_containerization_G43/assets/145265103/f0b18a42-fbe1-454b-99cc-9b4939e89cff)

* Kubenetes Diagram

![image](https://github.com/calvinhaooo/software_containerization_G43/assets/145342600/2f2b039d-5b5f-4c67-b705-6ac09d8cb16e)


## Prequisites

For installation, Docker and microk8s should be installed for our project.
we also need to create a private repository  (like us-east1-docker.pkg.dev/poised-rock-413209/grocery) so we can push our docker image into it if using Google cloud 
```
microk8s install
Docker install
```
in the grocery directory,run the command
```
docker build .
docker tag dockerID us-east1-docker.pkg.dev/poised-rock-413209/grocery/123
docker push us-east1-docker.pkg.dev/poised-rock-413209/grocery/123
```
in the postgres dicretory,run the command
```
docker build .
docker tag dockerID us-east1-docker.pkg.dev/poised-rock-413209/grocery/zhang
docker push us-east1-docker.pkg.dev/poised-rock-413209/grocery/zhang
```

## Implement the dockerfile for configuration
* Frontend --> css, js
* Backend --> python flask
* Database --> postgresql

## Repository Structure
*`grocery`
* * `*.yaml`: kubenetes configuration files
  * `Dockerfile`:  containerize the REST API and the Web front end
  * `static` : rendering
  * `temlates`: HTML
* `helm/grocery-test`: helm char for the whole application
* `postgres`
* * `*.yaml`: kubenetes configuration files
* `security`
* * `RBAC`: Configure Role Based Access Control for the application
  * `TLS`: Configure TLS for the web application 
  * `policy`: Network policy control


## Application upgrade and re-deployment
re-build the application after a source code change 
```

```
upgrade the running application in two ways: deployment rollout and canary update
```
```

## PostgreSQL

we use a pre-built docker image and create our own Dockerfile for the database,because we want the docker to run the sql file to create the database in the beginning


the Service exposed by the database is such that it can be accessed by the REST API, but not by users outside of the cluster 

Ensure that the configuration of the database makes use of ConfigMaps and Secrets appropriately

## RESTAPI  
we create your own Dockerfile for this image

can read and write to the database
when in cloud:
ip changes

## Web front-end
we build the frontend files into flask application image. 
## Helm Chart
```

```
## TLS
use **cert-manager** 
We use a **self-signed ClusterIssuer** to create a self-signed certificates cluster-wide.certificates(signed by a self-made certificate authority). 
Then, use it to bootstrap a **root certificate** which is stored in a secret(root-secret)
Next, we can configure ingress with a certificate signed by CA Issuer. 
Once we have built the TLS connection,we can check whether the application is accessible via https:
```
https://
```
![https](https://github.com/calvinhaooo/software_containerization_G43/assets/145265103/1de732b4-e269-42dc-a3b5-08a21a39e323)
check if http request can be directed to https:
```
http://
```

## Network Policy
For the database, we define a policy which only allows ingress from the flask API.
For the backend, we define a policy which only allows egress to the PostgreSQL.

To test the network policy we have defined:
```

```



## RBAC
we define and create three roles(admin,secret-watch,pod-watch) and bind them to the user calvin
check user permissions as follows


```
sudo microk8s kubectl auth can-i list pod --namespace default --as calvin
sudo microk8s kubectl auth can-i get pod --namespace default --as calvin
sudo microk8s kubectl auth can-i create pod --namespace default --as calvin
```

## google cloud
enable calico k8s network policy

```
```

upload the file to the cluster through cloudshell
```
docker build .
```

push the image to the repository, tag it with the repository name and then push the image‘
```
docker tag dockerID us-east1-docker.pkg.dev/poised-rock-413209/grocery/zhang
docker push us-east1-docker.pkg.dev/poised-rock-413209/grocery/zhang
```

```
helm install ./grocery-test --generate-name


```
/etc/hosts
 mygrocery-g43.com
```
SELECT * FROM <table_name>;

```
## commands on Microk8s

```
microk8s enable cert-manager
/etc/hosts
127.0.0.1 mygrocery-g43.com
```
