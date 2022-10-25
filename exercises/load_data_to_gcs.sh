#!/bin/bash
set -eu

# TODO: change it to your name
DESTINATION_BUCKET_NAME=2022-jlr-temp-<your-name>

gsutil mb -c standard -l EU gs://$DESTINATION_BUCKET_NAME

gsutil cp -r ./dataset/* gs://$DESTINATION_BUCKET_NAME/dataset/
