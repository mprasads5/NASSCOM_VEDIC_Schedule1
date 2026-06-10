import os
import datetime
import random

print("--- Intermediate Python Core Exercise ---")

# ============================================================
# Global Configuration Data
# These collections simulate available sensors, locations,
# and valid operating ranges for each sensor type.
# ============================================================

DEVICE_TYPES = [
    'Temperature_Sensor',
    'Humidity_Sensor',
    'Pressure_Sensor',
    'Light_Sensor'
]

LOCATIONS = [
    'Lab1',
    'Lab2',
    'OfficeA',
    'OfficeB',
    'Warehouse'
]

READING_RANGES = {
    'Temperature_Sensor': (18.0, 30.0),
    'Humidity_Sensor': (30.0, 80.0),
    'Pressure_Sensor': (980.0, 1030.0),
    'Light_Sensor': (100.0, 1000.0)
}

# ============================================================
# Task 1.1
# Generate 100 simulated sensor readings
# Each reading is stored as:
# (timestamp, device_id, device_type, location, value)
# ============================================================

raw_sensor_data = []

for i in range(1, 101):

    # Create a realistic timestamp by subtracting
    # a random number of minutes from the current time.
    timestamp = datetime.datetime.now() - datetime.timedelta(
        minutes=random.randint(0, 10000)
    )

    timestamp_str = timestamp.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # DEV001, DEV002 ... DEV100
    device_id = f"DEV{i:03d}"

    device_type = random.choice(DEVICE_TYPES)
    location = random.choice(LOCATIONS)

    # Generate a sensor value within the valid range
    min_val, max_val = READING_RANGES[device_type]

    value = round(
        random.uniform(min_val, max_val),
        2
    )

    raw_sensor_data.append(
        (
            timestamp_str,
            device_id,
            device_type,
            location,
            value
        )
    )

print(f"Generated {len(raw_sensor_data)} readings")

# ============================================================
# Task 1.2
# Extract only temperature sensor readings and
# convert them into dictionary format.
# ============================================================

temperature_readings = []

for reading in raw_sensor_data:

    timestamp, device_id, device_type, location, value = reading

    if device_type == "Temperature_Sensor":

        temperature_readings.append({
            "timestamp": timestamp,
            "device_id": device_id,
            "location": location,
            "temperature_celsius": value
        })

# ============================================================
# Task 1.3
# Create a set to identify all distinct locations.
# Sets automatically remove duplicate values.
# ============================================================

unique_locations = {
    reading[3]
    for reading in raw_sensor_data
}

# ============================================================
# Task 1.4
# Determine minimum and maximum values observed
# for each sensor type.
# ============================================================

device_stats = {}

for device in DEVICE_TYPES:

    device_stats[device] = (
        float('inf'),
        float('-inf')
    )

for reading in raw_sensor_data:

    device_type = reading[2]
    value = reading[4]

    current_min, current_max = device_stats[device_type]

    device_stats[device_type] = (
        min(current_min, value),
        max(current_max, value)
    )

# ============================================================
# Task 2.1
# Return all readings collected from a specific location.
# ============================================================

def get_readings_by_location(
        readings_list,
        target_location):

    return [
        reading
        for reading in readings_list
        if reading[3] == target_location
    ]

# ============================================================
# Task 2.2
# Calculate average temperature from a list of
# temperature sensor dictionaries.
# ============================================================

def calculate_average_temperature(temp_data_list):

    if not temp_data_list:
        return 0.0

    total = sum(
        reading["temperature_celsius"]
        for reading in temp_data_list
    )

    return total / len(temp_data_list)

# ============================================================
# Task 2.3
# Generate a human-readable report line.
# Example:
# [2025-06-10 09:30:00] Device DEV001 at Lab1: 25.6°C
# ============================================================

def generate_report_line(reading_dict):

    return (
        f"[{reading_dict['timestamp']}] "
        f"Device {reading_dict['device_id']} "
        f"at {reading_dict['location']}: "
        f"{reading_dict['temperature_celsius']}°C"
    )

# ============================================================
# Task 3.1
# Create a directory to store generated reports.
# ============================================================

reports_dir = "sensor_reports"

if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)

# ============================================================
# Task 3.2
# Convert string timestamps into datetime objects
# and calculate the duration between first and last record.
# ============================================================

date_format = "%Y-%m-%d %H:%M:%S"

first_dt = datetime.datetime.strptime(
    raw_sensor_data[0][0],
    date_format
)

last_dt = datetime.datetime.strptime(
    raw_sensor_data[-1][0],
    date_format
)

duration = last_dt - first_dt

# ============================================================
# Task 3.3
# Generate 5 random integers between 100 and 200.
# ============================================================

random_values = [
    random.randint(100, 200)
    for _ in range(5)
]

# ============================================================
# Task 4.1
# Write temperature report to a text file.
# ============================================================

report_filename = os.path.join(
    reports_dir,
    "temperature_report.txt"
)

try:

    with open(report_filename, "w") as file:

        for reading in temperature_readings:

            file.write(
                generate_report_line(reading)
                + "\n"
            )

except IOError as e:

    print("File Write Error:", e)

# ============================================================
# Task 4.2
# Read the generated report file and display
# the first three lines.
# ============================================================

try:

    with open(report_filename, "r") as file:

        read_report_lines = file.readlines()

    for line in read_report_lines[:3]:

        print(line.strip())

except IOError as e:

    print("File Read Error:", e)

print("\n--- Exercise Complete! ---")
print("Great job completing the intermediate Python exercise.")
print("Review your code and outputs to ensure correctness and understanding of all concepts.")
print("Consider adding more complex scenarios or user inputs for further practice.")
     