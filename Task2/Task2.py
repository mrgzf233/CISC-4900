# Task 2 for CISC 4900

"""
This program should read in all the json files and turn it into one json file.
This is the format.

[
{
"short-ka": "short name of KA",
"long-ka": "long name of KA",
"begin-page:  a number,
"end-page": a number
},
...
]
"""

import json

# only reading in one json file, need to read in all the json files
with open("cs2013_web_final_sf.json", "r") as f:  # open as file object?
    data = json.load(f)

print(data)

# putting all the json files that were read in into one json file
with open("cs2013_web_final_sf.json", "w") as f:
    json.dump(data, f)
