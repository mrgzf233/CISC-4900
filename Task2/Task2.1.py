import json

# option command l for reformat


# Input list for the json files
ka_list = [
    "cs2013_web_final_sf.json",
    "cs2013_web_final_pl.json",
    # manually add the rest of the json files here
]

all_dict = {
    "curriculum": "cs2013",
    "knowledge-areas": []
}

for json_file in ka_list:
    with open(json_file, "r") as f:
        data = json.load(f)
    all_dict["knowledge-areas"].append(data)  # Should I use extend instead of append?

    # Dictionary and List, dumps everything into the new JSON file.
with open("combined_ka.json", "w") as f:
    json.dump(all_dict, f, indent=2)

