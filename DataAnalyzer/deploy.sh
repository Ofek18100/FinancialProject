#!/bin/bash
docker build -t "ofek18100/dataanalyzer" .
docker push ofek18100/dataanalyzer
kubectl apply --validate=false -f data-analyzer-deployment.yaml
