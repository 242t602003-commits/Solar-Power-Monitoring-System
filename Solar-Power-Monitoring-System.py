# Solar-Power-Monitoring-System
Tracks solar panel voltage, current, power, and energy generation in real time.
import time
import csv
import random
from datetime import datetime

# ==========================================
# SOLAR POWER MONITORING SYSTEM
# ==========================================

SAMPLE_TIME = 5          # Reading interval in seconds
BATTERY_CAPACITY = 1000  # Battery capacity in Wh
battery_energy = 500     # Initial battery energy in Wh
total_energy = 0         # Total solar energy generated in Wh


# ------------------------------------------
# Create CSV file
# ------------------------------------------

with open("solar_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Date",
        "Time",
        "Solar Voltage (V)",
        "Solar Current (A)",
        "Power (W)",
        "Energy (Wh)",
        "Battery (%)"
    ])


print("=" * 65)
print("          SOLAR POWER MONITORING SYSTEM")
print("=" * 65)
print("Monitoring started...\n")


try:

    while True:

        # ----------------------------------
        # Simulated Solar Panel Measurements
        # ----------------------------------

        voltage = random.uniform(18, 22)
        current = random.uniform(1, 5)

        # Calculate solar power
        power = voltage * current

        # Calculate energy generated
        energy = power * (SAMPLE_TIME / 3600)

        total_energy += energy

        # ----------------------------------
        # Simulate Battery Charging
        # ----------------------------------

        battery_energy += energy

        if battery_energy > BATTERY_CAPACITY:
            battery_energy = BATTERY_CAPACITY

        battery_percentage = (
            battery_energy / BATTERY_CAPACITY
        ) * 100

        # ----------------------------------
        # Date and Time
        # ----------------------------------

        now = datetime.now()

        date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        # ----------------------------------
        # Display Information
        # ----------------------------------

        print("-" * 65)

        print(f"Date              : {date}")
        print(f"Time              : {current_time}")
        print(f"Solar Voltage     : {voltage:.2f} V")
        print(f"Solar Current     : {current:.2f} A")
        print(f"Solar Power       : {power:.2f} W")
        print(f"Energy Generated  : {total_energy:.3f} Wh")
        print(f"Battery Level     : {battery_percentage:.1f}%")

        # ----------------------------------
        # Battery Status
        # ----------------------------------

        if battery_percentage >= 90:
            status = "Battery Almost Full"
        elif battery_percentage >= 50:
            status = "Battery Normal"
        elif battery_percentage >= 20:
            status = "Battery Low"
        else:
            status = "Battery Critical"

        print(f"Battery Status    : {status}")

        # ----------------------------------
        # Save Data to CSV
        # ----------------------------------

        with open("solar_data.csv", "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                date,
                current_time,
                f"{voltage:.2f}",
                f"{current:.2f}",
                f"{power:.2f}",
                f"{total_energy:.3f}",
                f"{battery_percentage:.1f}"
            ])

        # Wait before next reading
        time.sleep(SAMPLE_TIME)


except KeyboardInterrupt:

    print("\n\nMonitoring stopped.")

    print(f"Total Solar Energy Generated: "
          f"{total_energy:.3f} Wh")

    print(f"Final Battery Level: "
          f"{battery_percentage:.1f}%")

    print("Data saved to solar_data.csv")
