# software_containerization_G43


# Diagram

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
