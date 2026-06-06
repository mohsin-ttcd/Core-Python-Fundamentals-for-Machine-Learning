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