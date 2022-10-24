DESTINATION_BUCKET_NAME=packt-data-eng-on-gcp-data-bucket
gsutil cp ./dataset/* gs://{$DESTINATION_BUCKET_NAME}/dataset/
