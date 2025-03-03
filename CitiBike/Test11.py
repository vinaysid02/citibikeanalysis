import json
import random
import pandas as pd
import pytest
from homework3 import numEarlyTrips

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_numEarlyTrips_random(random_file):
    expected_numEarlyTrips = data[random_file]["numEarlyTrips"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual = numEarlyTrips(df)
    assert actual == expected_numEarlyTrips