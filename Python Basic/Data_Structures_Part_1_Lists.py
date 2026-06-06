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