raw_data = "  mission:apollo11; mission_code:A11; status:success"

clean_raw_data = raw_data.strip().upper()

process_raw_data = clean_raw_data.split(";")

final_formated_data = process_raw_data[1].strip()

print(f"Cleaned Raw Data: {clean_raw_data}")
print(f"Formated Data: {final_formated_data}")


missions = [2026, "Artemis III", "Moon", 2027, "Europa Clipper", "Jupiter"]

first_mission_year = missions[0]
last_item = missions[-1]

# Let's say the Artemis III mission is delayed to 2028
missions[0] = 2028
#adding elements
missions.append(False)

print(f"First mission year: {first_mission_year}")
print(f"Last item: {last_item}")
print(f"Delayed Mission: {missions}")


tuple_config = ("v1.2.5", "production", 4096, True)
print(tuple_config)
print(type(tuple_config))

print(f"First iteam: {tuple_config[0]}")
print(f"Last iteam: {tuple_config[-1]}")


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

apollo_11 = {
    "mission_name": "Apollo 11",
    "launch_year": 1968, # Incorrect year
    "destination": "Moon",
    "crew": ["Neil Armstrong", "Buzz Aldrin"] # Missing a crew member
}


apollo_11["launch_year"] = 1969
crew_list = apollo_11["crew"]
crew_list.append("Michael Collins")

print(apollo_11 )


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


mission_logs = [
    {"name": "Mariner 4", "year": 1964, "status": "successful"},
    {"name": "Zond 2", "year": 1964, "status": "failed"},
    {"name": "Venera 7", "year": 1970, "status": "successful"},
    {"name": "Phobos 1", "year": 1988, "status": "failed"},
    {"name": "Viking 1", "year": 1975, "status": "successful"}
]

print("--- Successful Mission Report ---")

for mission in  mission_logs:
    
    if mission['status'] == "successful":
        print(f"Mission: {mission["name"]}, Year: {mission["year"]}")


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