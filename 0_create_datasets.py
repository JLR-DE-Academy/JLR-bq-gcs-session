from google.cloud import bigquery
from google.cloud.exceptions import NotFound

client = bigquery.Client()

datasets_name = ['2022_DE_Training_raw_bikesharing','2022_DE_Training_dwh_bikesharing','2022_DE_Training_dm_bikesharing']
location = 'EU'

def create_bigquery_dataset(dataset_name):
    """Create bigquery dataset. Check first if the dataset exists
        Args:
            dataset_name: String
    """

    dataset_id = "{}.{}".format(client.project, dataset_name)
    try:
        client.get_dataset(dataset_id)
        print("Dataset {} already exists".format(dataset_id))
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location
        dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
        print("Created dataset {}.{}".format(client.project, dataset.dataset_id))


for name in datasets_name:
    create_bigquery_dataset(name)
