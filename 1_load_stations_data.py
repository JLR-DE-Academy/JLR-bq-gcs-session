from google.cloud import bigquery


PROJECT_ID = "jlr-dl-cat-training"
BUCKET_NAME = "2022-jlr-de-training"
TABLE_ID = "{}.2022_DE_Training_raw_bikesharing.stations".format(PROJECT_ID)
GCS_URI = "gs://{}/dataset/stations/stations.csv".format(BUCKET_NAME)

def load_gcs_to_bigquery_snapshot_data(GCS_URI, TABLE_ID, table_schema):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        schema = table_schema,
        source_format = bigquery.SourceFormat.CSV,
        write_disposition = 'WRITE_TRUNCATE'
        )

    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config
    )
    load_job.result()
    table = client.get_table(TABLE_ID)

    print("Loaded {} rows to table {}".format(table.num_rows, TABLE_ID))

bigquery_table_schema = [
    bigquery.SchemaField("station_id", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("region_id", "STRING"),
    bigquery.SchemaField("capacity", "INTEGER")
]

if __name__ == '__main__':
    load_gcs_to_bigquery_snapshot_data(GCS_URI, TABLE_ID, bigquery_table_schema)
