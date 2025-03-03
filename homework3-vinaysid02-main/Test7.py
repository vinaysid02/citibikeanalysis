import json
import random
import pandas as pd
import pytest
from homework3 import avgTripsPerBike

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_avgTripsPerBike_random(random_file):
    expected_avgTripsPerBike = data[random_file]["avgTripsPerBike"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual = avgTripsPerBike(df)
    assert actual == expected_avgTripsPerBike