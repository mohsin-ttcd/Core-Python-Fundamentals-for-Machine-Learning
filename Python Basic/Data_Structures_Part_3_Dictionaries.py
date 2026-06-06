planet_data = {
    "name": "Mars",
    "diameter_km": 6779,
    "has_rings": False,
    "moons": ["Phobos", "Deimos"]
}

# access specific key and print it's value
print(f"Original Dictionary: {planet_data}")
print(f"Moons of {planet_data["name"]}: {", ".join(planet_data["moons"])}")

# update dictionary value
planet_data["has_rings"] = True
print(f"Updated Dictionary: {planet_data}")

# update dictionary
planet_data["orbital_period_days"] = 687
print(f"New Dictionary: {planet_data}")

# safe way use get method
mean_temp = planet_data.get("mean_temperature", "Not available")
print(f"\nMean temperature: {mean_temp}")