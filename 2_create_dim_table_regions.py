from google.cloud import bigquery


# TODO : Change to your name
DATASET_NAME_PREFIX = '2022_temp_<your-name>'

PROJECT_ID = "jlr-dl-cat-training"
TARGET_TABLE_ID = f"{PROJECT_ID}.{DATASET_NAME_PREFIX}_dwh_bikesharing.dim_regions"


def create_dim_table(PROJECT_ID, TARGET_TABLE_ID):
    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
    destination=TARGET_TABLE_ID,
    write_disposition='WRITE_TRUNCATE')

    sql = f"""SELECT CAST(region_id AS STRING) as region_id, name
          FROM `{PROJECT_ID}.{DATASET_NAME_PREFIX}_raw_bikesharing.regions` regions
          ;"""

    query_job = client.query(sql, job_config=job_config)

    try:
        query_job.result()
        print("Query success")
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    create_dim_table(PROJECT_ID, TARGET_TABLE_ID)

