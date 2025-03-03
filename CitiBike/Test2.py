import json
import random
import pandas as pd
import pytest
from homework3 import avgTripDuration

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_avgTripDuration_random(random_file):
    expected_avg_trip_duration = data[random_file]["avgTripDuration"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual_avg_trip_duration = avgTripDuration(df)
    assert abs(actual_avg_trip_duration - expected_avg_trip_duration) < 0.001
