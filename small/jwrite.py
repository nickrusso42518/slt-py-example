import json
data = {
    'bedrooms': 3,
    'bathrooms': 2,
    'color': ['blue', 'white']
}
with open('house.json', 'w') as handle:
    json.dump(data, handle, indent=4)
