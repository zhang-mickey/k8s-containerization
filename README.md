# software_containerization_G43


# Diagram
![image](https://github.com/zhang-mickey/k8s-containerization/assets/145342600/c15b3101-c91a-414c-8839-78a60c222427)


# Application upgrade and re-deployment
re-build the application after a source code change 
```

```
upgrade the running application in two ways: deployment rollout and canary update
```
```

# PostgreSQL

use a pre-built docker image for this database

the Service exposed by the database is such that it can be accessed by the REST API, but not by users outside of the cluster 

Ensure that the configuration of the database makes use of ConfigMaps and Secrets appropriately

# RESTAPI  
create your own Dockerfile for this image

# Web front-end

# Helm Chart

# TLS
certificates signed by a self-made certificate authority
use cert-manager

# Network Policy

# RBAC
