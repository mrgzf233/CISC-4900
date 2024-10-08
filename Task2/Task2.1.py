import json

# List to combine all the knowledge areas
combined_ka_list = []

# Input list for the json files
ka_list = [
    "cs2013_web_final_sf.json",
    "cs2013_web_final_pl.json",
    # manually add the rest of the json files here then use a for loop??
]

all_dict = {}
all_dict = {"list_kas": []}
for json_file in ka_list:
    with open(json_file, "r") as f:
        data = json.load(f)
    all_dict["list_ka"].append(data)

#dictionary and list
# need to add code here to format the output


with open("combined_ka.json", "w") as f:
    json.dump(combined_ka_list, f, indent=2)
