#Control Flow Part 2: for Loops

planet_data = {
    "name": "Mars",
    "diameter_km": 6779,
    "has_rings": False,
}


for keys, value in planet_data.items():
    print(keys, ":", value)

for key in planet_data:
    value = planet_data[key]
    print(key, ":", value)