import serial
import csv
import time
from datetime import datetime

# Set up serial port (change COM port if needed)
ser = serial.Serial('COM61', 9600)

# Open or create CSV file
csv_file = open('Tempdata_24AUG.csv', 'a', newline='')
writer = csv.writer(csv_file)

# Write header if file is new
if csv_file.tell() == 0:
    writer.writerow(['Timestamp', 'Temperature (°C)', 'Humidity (%)'])

try:
    while True:
        # Read and decode serial data
        line = ser.readline().decode('utf-8').strip()
        print(f"Raw line: '{line}'")  # Debug output

        # Split by comma
        parts = line.split(',')
        print(f"Split parts: {parts}")  # Debug output

        # Check if we have at least temperature and humidity
        if len(parts) >= 2:
            temperature = parts[0].strip()
            humidity = parts[1].strip()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Write to CSV
            writer.writerow([timestamp, temperature, humidity])
            csv_file.flush()

            # Print to console
            print(f"{timestamp}: Temperature = {temperature}°C, Humidity = {humidity}%")
        else:
            print(f"⚠️ Malformed line: '{line}'")

except KeyboardInterrupt:
    print("🛑 Logging stopped by user.")

finally:
    csv_file.close()
    ser.close()
    print("✅ CSV file and serial port closed.")
