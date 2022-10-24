#!/bin/bash
set -eu


echo $(which python)

python 0_create_datasets.py

python 1_load_regions_data.py
python 1_load_stations_data.py
python 1_load_trips_data.py

python 2_create_dim_table_regions.py
python 2_create_dim_table_stations.py
python 2_create_fact_table_daily_by_gender_region.py 2018-01-01
python 2_create_fact_table_daily_trips.py 2018-01-01
