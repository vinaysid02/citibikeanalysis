import json
import random
import pandas as pd
import pytest
from homework3 import countAllStations

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_countAllStations_random(random_file):
    test_countAllStations_random = data[random_file]["countAllStations"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual = countAllStations(df)
    assert actual == test_countAllStations_random