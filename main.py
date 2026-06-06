spacecraft_fleet = [
    {"name": "Voyager 1", "launch_year": 1977, "status": "operational"},
    {"name": "Pioneer 10", "launch_year": 1972, "status": "unknown"},
    {"name": "Cassini-Huygens", "launch_year": 1997, "status": "retired"},
    {"name": "Hubble Telescope", "launch_year": 1990, "status": "operational"},
    {"name": "Magellan", "launch_year": 1989, "status": "retired"}
]

def generate_fleet_report(fleet_list):
    report_lines = []

    for spacecraft in fleet_list:
        
        # access dictionary safely
        name = spacecraft.get("name", "N/A")
        year = spacecraft.get("launch_year", "N/A")
        status = spacecraft.get("status", "N/A")

        if status == "operational":
            line = f"[OPERATIONAL] {name} (Launched: {year})"

        elif status == "retired":
            line = f"[RETIRED] {name} (Launched: {year})"
        
        else:
            line = f"[UNKNOWN] {name} (Launched: {year})"

        report_lines.append(line)

    return report_lines


final_report = generate_fleet_report(spacecraft_fleet)

for report in  final_report:
    print(report)
