import json
import random
import pandas as pd
import pytest
import inspect
from homework3 import avgTripsByDayOfWeek

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)
random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_avgTripsByDayOfWeek_random(random_file):
    expected_avgTripsByDayOfWeek = data[random_file]["avgTripsByDayOfWeek"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    
    if "for" in inspect.getsource(avgTripsByDayOfWeek):
        pytest.xfail("The function contains a for looap and is expected to fail.")

    actual = avgTripsByDayOfWeek(df)
    assert actual == expected_avgTripsByDayOfWeek
