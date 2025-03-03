import pandas as pd
import random
import pytest
import json
from homework3 import countTrips

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)
random_files = random.sample(list(data.keys()), 5)

def load_csv_data(csv_filepath):
    return pd.read_csv(csv_filepath)


@pytest.mark.parametrize("random_file", random_files)
def test_countTrips_random(random_file):
    expected_count_trips = data[random_file]["countTrips"]
    csv_file = random_file.replace('.json', '.csv')
    actual_data = pd.read_csv(csv_file)
    actual_count_trips = countTrips(actual_data)
    assert actual_count_trips == expected_count_trips
