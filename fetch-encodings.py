import json
import numpy as np

# read
with open('encodings.json') as f:
    knownEncodings = {k: np.array(v) for k, v in json.load(f).items()}


print(knownEncodings)