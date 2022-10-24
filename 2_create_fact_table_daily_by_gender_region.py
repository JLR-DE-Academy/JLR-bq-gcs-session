import sys
from google.cloud import bigquery


# TODO : Change to your name
DATASET_NAME_PREFIX = '2022_temp_<your-name>'

PROJECT_ID = "jlr-dl-cat-training"
target_table_id = f"{PROJECT_ID}.{DATASET_NAME_PREFIX}_dwh_bikesharing.fact_region_gender_daily"


def create_fact_table(PROJECT_ID, target_table_id):
    load_date = sys.argv[1] # date format : yyyy-mm-dd
    print("\nLoad date:", load_date)

    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
    destination=target_table_id,
    write_disposition='WRITE_APPEND')

    sql = f"""SELECT DATE(start_date) as trip_date,
                region_id,
                member_gender,
                COUNT(trip_id) as total_trips
                FROM `{PROJECT_ID}.{DATASET_NAME_PREFIX}_raw_bikesharing.trips` trips
                JOIN `{PROJECT_ID}.{DATASET_NAME_PREFIX}_raw_bikesharing.stations` stations
                ON trips.start_station_id = stations.station_id
                WHERE DATE(start_date) = DATE('{load_date}') AND member_gender IS NOT NULL
                GROUP BY trip_date, region_id, member_gender
                ;"""

    query_job = client.query(sql, job_config=job_config)

    try:
        query_job.result()
        print("Query success")
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    create_fact_table(PROJECT_ID, target_table_id)

