#!/bin/bash
kubectl apply --validate=false -f data-analyzer-service.yaml
kubectl apply --validate=false -f data-updater-service.yaml
kubectl apply --validate=false -f data-base-volume.yaml
kubectl apply --validate=false -f data-base-claim.yaml