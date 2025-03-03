import json
import random
import pandas as pd
import pytest
from homework3 import topXdepartures

with open('keys.json', 'r') as json_file:
    data = json.load(json_file)

random_files = random.sample(list(data.keys()), 5)

@pytest.mark.parametrize("random_file", random_files)
def test_topXdepartures_random(random_file):
    expected_topXdepartures = data[random_file]["topXdepartures"]
    csv_filename = f"{random_file}"
    df = pd.read_csv(csv_filename)
    actual = topXdepartures(5, df)
    expected_topXdepartures = pd.DataFrame(expected_topXdepartures)

    actual = actual.reset_index(drop=True)
    expected_topXdepartures = expected_topXdepartures.reset_index(drop=True)

    pd.testing.assert_frame_equal(expected_topXdepartures, actual)
