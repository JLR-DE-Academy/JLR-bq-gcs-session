#!/bin/bash
set -eu


DESTINATION_BUCKET_NAME=<my-bucket-name>

gsutil mb gs://$DESTINATION_BUCKET_NAME

gsutil cp -r ./dataset/* gs://$DESTINATION_BUCKET_NAME/dataset/
