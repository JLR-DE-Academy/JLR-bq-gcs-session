from google.cloud import bigquery
from google.cloud.exceptions import NotFound


# TODO : Change to your name
DATASET_NAME_PREFIX = '2022_temp_<your-name>'

datasets_name = [DATASET_NAME_PREFIX + d for d in ['_raw_bikesharing','_dwh_bikesharing','_dm_bikesharing']]
# datasets_name = ['2022_DE_Training_raw_bikesharing','2022_DE_Training_dwh_bikesharing','2022_DE_Training_dm_bikesharing']
location = 'EU'

client = bigquery.Client()


def create_bigquery_dataset(dataset_name):
    """Create bigquery dataset. Check first if the dataset exists
        Args:
            dataset_name: String
    """

    dataset_id = f"{client.project}.{dataset_name}"
    try:
        client.get_dataset(dataset_id)
        print(f"Dataset {dataset_id} already exists")
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
        print(f"Created dataset {client.project}.{dataset.dataset_id}")


for name in datasets_name:
    create_bigquery_dataset(name)
