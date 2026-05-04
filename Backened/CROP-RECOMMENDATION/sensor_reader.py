# import serial
# import time

# arduino = serial.Serial('COM5',9600,timeout=1)
# time.sleep(2)

# def read_sensor_data():
    
#     try:
#         line = arduino.readline().decode().strip()
#     except:
#         return None
    
#     if not line:
#         return None

#     values = line.split(",")

#     if len(values) == 5:
#         try:
#             return {
#                 "temperature": float(values[0]),
#                 "humidity": float(values[1]),
#                 "moisture": int(values[2]),
#                 "light": int(values[3]),
#                 "rain": int(values[4])
#             }
#         except ValueError:
#             return None

#     return None

# def read_sensor_data():
#     try:
#         line = arduino.readline().decode().strip()
#         print("RAW:", line)   # debug
#     except:
#         return None

#     if not line:
#         return None

#     values = line.split(",")

#     if len(values) == 5:
#         try:
#             data = {
#                 "temperature": float(values[0]),
#                 "humidity": float(values[1]),
#                 "moisture": int(values[2]),
#                 "light": int(values[3]),
#                 "rain": int(values[4])
#             }

#             # 🔥 ADD THIS (pump logic in Python)
#             dryValue = 750
#             data["pump"] = 1 if data["moisture"] > dryValue else 0

#             return data

#         except ValueError:
#             return None

#     return None


import serial
import time

# -------- SERIAL CONNECTION --------
try:
    arduino = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)  # allow Arduino to reset
    print("✅ Connected to Arduino on COM5")
except Exception as e:
    print("❌ Error connecting to Arduino:", e)
    arduino = None


# -------- READ SENSOR DATA FUNCTION --------
def read_sensor_data():
    if arduino is None:
        return None

    try:
        line = arduino.readline().decode().strip()
        print("RAW:", line)   # Debug (remove later if needed)
    except Exception as e:
        print("Read Error:", e)
        return None

    # Skip empty lines
    if not line:
        return None

    # Split comma-separated values
    values = line.split(",")

    # Expecting 6 values: temp, hum, soil, light, rain, pump
    if len(values) == 6:
        try:
            data = {
                "temperature": float(values[0]),
                "humidity": float(values[1]),
                "moisture": int(values[2]),
                "light": int(values[3]),
                "rain": int(values[4]),
                "pump": int(values[5])   # 1 = ON, 0 = OFF
            }
            return data

        except ValueError:
            print("⚠️ Conversion error:", values)
            return None

    else:
        print("⚠️ Invalid data format:", values)
        return None


# -------- TEST BLOCK (run file directly) --------
if __name__ == "__main__":
    print("Reading sensor data...\n")

    while True:
        data = read_sensor_data()

        if data:
            print("Parsed Data:", data)
        else:
            print("No valid data")

        time.sleep(1)