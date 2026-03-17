#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

// DHT setup
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// LCD setup
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Sensor pins
int soilPin = A0;
int ldrPin = A1;
int rainPin = 6;
int buzzer = 8;

void setup() {

  Serial.begin(9600);

  dht.begin();

  lcd.init();
  lcd.backlight();
 
  pinMode(rainPin, INPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  int soil = analogRead(soilPin);
  int light = analogRead(ldrPin);
  int rain = digitalRead(rainPin);

  // -------- SERIAL DATA FOR PYTHON --------
  Serial.print(temp);
  Serial.print(",");
  Serial.print(hum);
  Serial.print(",");
  Serial.print(soil);
  Serial.print(",");
  Serial.print(light);
  Serial.print(",");
  Serial.println(rain);

  // -------- LCD DISPLAY --------
  lcd.clear();

  lcd.setCursor(0,0); 
  lcd.print("T:");
  lcd.print(temp);
  lcd.print(" H:");
  lcd.print(hum);

  lcd.setCursor(0,1);
  lcd.print("Soil:");
  lcd.print(soil);

  delay(3000);

  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print("Light:");
  lcd.print(light);

  lcd.setCursor(0,1);

  if(rain == 0)
  {
    lcd.print("Rain Detected");

    digitalWrite(buzzer, HIGH);
    delay(800);
    digitalWrite(buzzer, LOW);
  }
  else
  {
    lcd.print("No Rain");
  }

  if(soil > 700)
  {
    for(int i=0;i<3;i++)
    {
      digitalWrite(buzzer, HIGH);
      delay(200);
      digitalWrite(buzzer, LOW);
      delay(200);
    }
  }

  delay(3000);
}