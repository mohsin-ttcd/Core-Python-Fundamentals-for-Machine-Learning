# Data for the exercise
spacecraft_fleet = [
    {"name": "Voyager 1", "launch_year": 1977, "status": "operational"},
    {"name": "Pioneer 10", "launch_year": 1972, "status": "unknown"},
    {"name": "Cassini-Huygens", "launch_year": 1997, "status": "retired"},
    {"name": "Hubble Telescope", "launch_year": 1990, "status": "operational"},
    {"name": "Magellan", "launch_year": 1989, "status": "retired"}
]


def generate_fleet_report (fleet_list):
    report_lines = []

    for spacecraft in fleet_list:

        spacecraft_name = spacecraft.get("name", "N/A")
        spacecraft_launch = spacecraft.get("launch_year", "N/A")
        spacecraft_status = spacecraft.get("status", "N/A")

        if spacecraft_status == "operational":
            line = f"[OPERATIONAL] {spacecraft_name} (Launched: {spacecraft_launch})"
        
        elif spacecraft_status == "retired":
            line = f"[RETIRED] {spacecraft_name} (Launched: {spacecraft_launch})"
        else:
            line = f"[UNKNOWN] {spacecraft_name} (Launched: {spacecraft_launch})"
        
        report_lines.append(line)
    
    return report_lines



reporting = generate_fleet_report(spacecraft_fleet)

for line in reporting:
    print(line)

