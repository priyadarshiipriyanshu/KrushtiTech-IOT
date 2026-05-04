#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

// DHT setup
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// LCD setup
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Pins
int soilPin = A0;
int ldrPin = A1;
int rainPin = 6;
int buzzer = 8;
int relayPin = 7;

// ONLY condition value
int dryValue = 750;

void setup() {

  Serial.begin(9600);

  dht.begin();
  lcd.init();
  lcd.backlight();

  pinMode(rainPin, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(relayPin, OUTPUT);

  digitalWrite(relayPin, HIGH); // pump OFF
}

void loop() {

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  int soil = analogRead(soilPin);
  int light = analogRead(ldrPin);
  int rain = digitalRead(rainPin);

  // -------- SERIAL OUTPUT --------
  // Serial.print("Temp:");
  // Serial.print(temp);

  // Serial.print(" | Hum:");
  // Serial.print(hum);

  // Serial.print(" | Soil:");
  // Serial.print(soil);

  // Serial.print(" | Light:");
  // Serial.print(light);

  // Serial.print(" | Rain:");
  // Serial.print(rain);

  // Serial.print(" | Pump:");
  // Serial.println(soil > dryValue ? "ON" : "OFF");

Serial.print(temp);
Serial.print(",");

Serial.print(hum);
Serial.print(",");

Serial.print(soil);
Serial.print(",");

Serial.print(light);
Serial.print(",");

Serial.print(rain);
Serial.print(",");

Serial.println(soil > dryValue ? 1 : 0);  // pump (1/0)


  // -------- LCD DISPLAY 1 --------
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("T:");
  lcd.print(temp);
  lcd.print(" H:");
  lcd.print(hum);

  lcd.setCursor(0,1);
  lcd.print("Soil:");
  lcd.print(soil);
  lcd.print("   ");

  delay(2000);

  // -------- LCD DISPLAY 2 --------
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Light:");
  lcd.print(light);
  lcd.print("   ");

  lcd.setCursor(0,1);
  lcd.print(rain == 0 ? "Rain Detected " : "No Rain       ");

  // -------- BUZZER --------
  if(rain == 0)
    digitalWrite(buzzer, HIGH);
  else
    digitalWrite(buzzer, LOW);

  delay(2000);

  // -------- PUMP CONTROL --------
  lcd.clear();
  lcd.setCursor(0,0);

  if(soil > dryValue)   // ONLY condition
  {
    digitalWrite(relayPin, LOW);   // Pump ON
    lcd.print("Pump ON        ");

    delay(2000);   // run pump for 2 seconds ONLY

    digitalWrite(relayPin, HIGH);  // Pump OFF after time
  }
  else
  {
    digitalWrite(relayPin, HIGH);  // always OFF
    lcd.print("Pump OFF       ");
  }

  delay(2000);
}