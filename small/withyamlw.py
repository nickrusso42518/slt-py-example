import yaml
data = {
    "bedrooms": 3,
    "bathrooms": 2,
    "color": ["blue", "white"]
}
with open("house.yml", "w") as handle:
    yaml.dump(data, handle, default_flow_style = False)
