import serial
import time

arduino = serial.Serial('COM6',9600,timeout=1)
time.sleep(2)

def read_sensor_data():
    
    try:
        line = arduino.readline().decode().strip()
    except:
        return None
    
    if not line:
        return None

    values = line.split(",")

    if len(values) == 5:
        try:
            return {
                "temperature": float(values[0]),
                "humidity": float(values[1]),
                "moisture": int(values[2]),
                "light": int(values[3]),
                "rain": int(values[4])
            }
        except ValueError:
            return None

    return None