# 🌾 KrushtiTech - Smart Agriculture IoT + AI System

## 📋 Project Overview

KrushtiTech is an innovative Smart Agriculture system that combines **Internet of Things (IoT)**, **Artificial Intelligence (AI)**, and a user-friendly **web interface**. The system utilizes an Arduino UNO microcontroller with various sensors to collect real-time environmental data such as temperature, humidity, soil moisture, light intensity, and rainfall. This data is processed by machine learning models to provide intelligent crop recommendations and plant disease detection, empowering farmers with data-driven insights for efficient farming practices.

## 🎯 Purpose and Use of the Project

### Problems Faced by Farmers
Traditional farming often relies on guesswork and experience, leading to several challenges:
- **Lack of real-time data**: Farmers can't monitor environmental conditions continuously
- **Wrong crop choices**: Selecting unsuitable crops based on limited information
- **Water wastage**: Inefficient irrigation leading to over or under-watering
- **Late disease detection**: Plant diseases go unnoticed until it's too late

### How KrushtiTech Helps
KrushtiTech addresses these issues through:
- **Real-time monitoring**: Continuous sensor data collection and visualization
- **Smart crop prediction**: AI-powered recommendations based on soil and environmental factors
- **Early disease detection**: Machine learning models identify plant diseases from leaf images
- **Automated irrigation**: Smart pump control based on soil moisture levels

### Real-World Impact
- **Better crop yields**: Optimized farming decisions lead to higher productivity
- **Reduced losses**: Early disease detection prevents crop damage
- **Resource efficiency**: Smart irrigation conserves water and reduces costs
- **Sustainable farming**: Data-driven practices promote environmentally friendly agriculture

## 📁 Project Structure

```
KrushtiTech/
├── Backend/
│   ├── CROP-RECOMMENDATION/          # Streamlit app + ML model for crop prediction
│   │   ├── webapp.py                 # Main Streamlit dashboard
│   │   ├── sensor_reader.py          # Arduino serial data reader
│   │   ├── Crop_recommendation.csv   # Training dataset
│   │   └── requirements.txt          # Python dependencies
│   └── PLANT-DISEASE-IDENTIFICATION/ # Plant disease detection system
│       ├── main.py                   # Disease detection script
│       ├── trained_plant_disease_model.keras  # Trained ML model
│       ├── training_hist.json        # Training history
│       └── requirements.txt          # Python dependencies
├── Frontend/
│   └── KrushtiTech-web-app/          # Web interface
│       ├── index.html                # Main webpage
│       ├── css/                      # Stylesheets
│       ├── js/                       # JavaScript files
│       └── images/                   # Static images
├── Datasets/                         # Additional datasets
└── Arduino/                          # Hardware code (not shown in structure)
```

## 🔧 Hardware Components

- **Arduino UNO**: Main microcontroller board
- **DHT11 Sensor**: Temperature and humidity measurement
- **Soil Moisture Sensor**: Measures soil water content
- **Rain Sensor**: Detects rainfall
- **LDR (Light Dependent Resistor)**: Measures light intensity
- **LCD Display (I2C)**: Shows sensor readings
- **Relay Module**: Controls pump for irrigation
- **Water Pump**: Automated watering system
- **Buzzer**: Audio alerts for system status
- **Breadboard & Jumper Wires**: Circuit connections

## 🔌 Hardware Connections (Step-by-Step)

1. **DHT11 Sensor**:
   - VCC → Arduino 5V
   - GND → Arduino GND
   - DATA → Arduino Digital Pin 2

2. **Soil Moisture Sensor**:
   - VCC → Arduino 5V
   - GND → Arduino GND
   - Analog Output → Arduino Analog Pin A0

3. **LDR Sensor**:
   - One leg → Arduino 5V
   - Other leg → Arduino Analog Pin A1 + 10KΩ resistor to GND

4. **Rain Sensor**:
   - VCC → Arduino 5V
   - GND → Arduino GND
   - Digital Output → Arduino Digital Pin 6

5. **LCD Display (I2C)**:
   - VCC → Arduino 5V
   - GND → Arduino GND
   - SDA → Arduino Analog Pin A4
   - SCL → Arduino Analog Pin A5

6. **Buzzer**:
   - Positive → Arduino Digital Pin 8
   - Negative → Arduino GND

7. **Relay Module**:
   - VCC → Arduino 5V
   - GND → Arduino GND
   - Signal → Arduino Digital Pin 9
   - Relay output connected to water pump

## ⚙️ Arduino Setup (Arduino IDE)

1. **Install Arduino IDE**:
   - Download from [arduino.cc](https://www.arduino.cc/en/software)
   - Install and launch the application

2. **Install Required Libraries**:
   - Open Arduino IDE
   - Go to Sketch → Include Library → Manage Libraries
   - Search and install:
     - "DHT sensor library" by Adafruit
     - "LiquidCrystal I2C" by Frank de Brabander

3. **Upload Arduino Code**:
   - Open the `.ino` file from the Arduino folder
   - Select Board: Tools → Board → Arduino UNO
   - Select COM Port: Tools → Port → (your Arduino COM port)
   - Click Upload button
   - Verify serial output format: `temperature,humidity,soil,light,rain`

## 🐍 Python Backend Setup (VS Code)

1. **Open Project in VS Code**:
   - Launch VS Code
   - File → Open Folder → Select KrushtiTech project folder

2. **Install Python**:
   - Download from [python.org](https://www.python.org/)
   - Ensure Python is added to PATH during installation

3. **Install Dependencies**:
   - Open VS Code terminal
   - Navigate to project root
   - Run: `pip install -r requirements.txt`

4. **Key Files Explanation**:
   - `sensor_reader.py`: Reads serial data from Arduino
   - `webapp.py`: Streamlit web application for data visualization

## 🌱 How to Run Crop Recommendation (STEP-BY-STEP)

1. **Connect Arduino Hardware**:
   - Ensure all sensors are properly connected
   - Power on the Arduino board

2. **Close Arduino Serial Monitor**:
   - If open, close any serial monitor to free the COM port

3. **Open VS Code Terminal**:
   - Navigate to `Backend/CROP-RECOMMENDATION` folder

4. **Run the Application**:
   ```
   streamlit run webapp.py
   ```

5. **Access the Dashboard**:
   - Open browser and go to `http://localhost:8501`

6. **View Live Data**:
   - Monitor real-time sensor readings on the dashboard

7. **Make Predictions**:
   - Enter NPK values and pH level
   - Click "Predict Crop" button
   - View recommended crops based on conditions

## 🩺 How to Run Plant Disease Detection (STEP-BY-STEP)

1. **Navigate to Disease Detection Folder**:
   - Go to `Backend/PLANT-DISEASE-IDENTIFICATION`

2. **Open VS Code Terminal**:
   - Ensure you're in the correct directory

3. **Run the Script**:
   ```
   python main.py
   ```

4. **Provide Input**:
   - Upload or provide path to leaf image

5. **Get Results**:
   - The trained model analyzes the image
   - Output displays detected disease name and confidence

## 🌐 How to Run Frontend

1. **Navigate to Frontend Folder**:
   - Go to `Frontend/KrushtiTech-web-app`

2. **Open in Browser**:
   - Right-click `index.html`
   - Open with your preferred web browser

3. **Explore Features**:
   - Navigate through different sections
   - View weather forecasts, guides, and more

## 🔄 Full System Workflow

```
Sensors → Arduino UNO → Serial Communication → Python Backend → Streamlit Dashboard → Machine Learning Models → User Interface
```

1. Sensors collect environmental data
2. Arduino processes and transmits data via serial
3. Python scripts read and process the data
4. Streamlit creates interactive web dashboard
5. ML models analyze data for predictions
6. Users receive recommendations and alerts

## ✨ Features

- 📊 **Live Sensor Monitoring**: Real-time display of environmental parameters
- 💧 **Smart Irrigation System**: Automated pump control based on soil moisture
- 🌾 **Crop Recommendation**: AI-powered suggestions for optimal crop selection
- 🩺 **Plant Disease Detection**: Machine learning-based disease identification
- 📄 **Farmer Reports**: Downloadable reports with recommendations
- 🔊 **Buzzer Alerts**: Audio notifications for critical conditions
- 🌤️ **Weather Integration**: Weather forecast integration in web app

## 🔧 Troubleshooting

### COM Port Issues
- **Problem**: COM port not detected
- **Solution**: Check device manager, reinstall Arduino drivers, try different USB ports

### Sensor Reading Problems
- **Problem**: Sensor values showing 0
- **Solution**: Verify connections, check sensor power supply, calibrate sensors

### LCD Display Issues
- **Problem**: LCD not displaying text
- **Solution**: Check I2C address (usually 0x27), verify SDA/SCL connections

### Rain Sensor Inaccuracy
- **Problem**: Incorrect rain detection
- **Solution**: Adjust sensitivity threshold in code, clean sensor surface

### Streamlit Not Running
- **Problem**: Application fails to start
- **Solution**: Check Python installation, install missing dependencies, verify port availability

## 👨‍💻 Author

**Priyanshu Priyadarshi**

---

*Made with ❤️ for sustainable agriculture*
