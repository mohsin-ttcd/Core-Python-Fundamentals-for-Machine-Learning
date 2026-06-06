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