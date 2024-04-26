#!/bin/bash

image_name="ofek18100/financialproject"

# Delete existing images with the same name
docker rmi $(docker images "$image_name" -q)

docker build -t "ofek18100/financialproject" .

docker push ofek18100/financialproject
kubectl apply --validate=false -f data-updater-deployment.yaml
