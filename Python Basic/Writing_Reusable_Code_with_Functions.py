earth_data = {
    "name": "Earth",
    "diameter_km": 12742,
    "moons": ["Moon"]
}

# Another dictionary with different data
jupiter_data = {
    "name": "Jupiter",
    "diameter_km": 139820,
    "moons": ["Io", "Europa", "Ganymede", "Callisto"] # and many more!
}


def planet_summery(planet_dict):
    planet_name = planet_dict.get("name", "N/A")
    planet_diameter_km = planet_dict.get("diameter_km", "N/A")
    planet_moons = len(planet_dict.get(("moons"), []))

    return f"{planet_name} has a diameter of {planet_diameter_km} km and {planet_moons} main moon(s)."

print(planet_summery(jupiter_data))
print(planet_summery(earth_data))