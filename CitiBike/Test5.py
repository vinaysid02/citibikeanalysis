import json
import random
import pandas as pd
import pytest
from homework3 import countStartStations

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_countStartStations_random(random_file):
    expected_countStartStations = data[random_file]["countStartStations"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual = countStartStations(df)
    assert actual == expected_countStartStations