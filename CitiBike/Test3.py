import json
import random
import pandas as pd
import pytest
from homework3 import maxTripDuration

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_maxTripDuration_random(random_file):
    expected_max_trip_duration = data[random_file]["maxTripDuration"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual = maxTripDuration(2000,df)
    assert actual == expected_max_trip_duration