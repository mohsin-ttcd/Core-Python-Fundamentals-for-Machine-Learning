# Exercise 1: Clean and Parse a Data String


raw_data = "  mission:apollo11; mission_code:A11; status:success"

clean_raw_data = raw_data.strip().upper()

process_raw_data = clean_raw_data.split(";")

final_formated_data = process_raw_data[1].strip()

print(f"Cleaned Raw Data: {clean_raw_data}")
print(f"Formated Data: {final_formated_data}")