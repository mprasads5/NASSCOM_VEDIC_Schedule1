import os
import datetime
import random

print("--- Intermediate Python Core Exercise ---")

# ============================================================
# Global Configuration Data
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

# Generate sensor readings
raw_sensor_data = []

for i in range(1, 101):
    timestamp = datetime.datetime.now() - datetime.timedelta(
        minutes=random.randint(0, 10000)
    )

    timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    device_id = f"DEV{i:03d}"
    device_type = random.choice(DEVICE_TYPES)
    location = random.choice(LOCATIONS)

    min_val, max_val = READING_RANGES[device_type]
    value = round(random.uniform(min_val, max_val), 2)

    raw_sensor_data.append(
        (timestamp_str, device_id, device_type, location, value)
    )

print(f"Generated {len(raw_sensor_data)} readings")
