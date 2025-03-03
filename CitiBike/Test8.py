import json
import random
import pandas as pd
import pytest
from homework3 import avgRiderAge

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_avgRiderAge_random(random_file):
    expected_avgRiderAge = data[random_file]["avgRiderAge"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual = avgRiderAge(2020,df)
    assert actual == expected_avgRiderAge