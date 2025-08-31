#include "DHT.h"

#define DHTPIN 8     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22   // DHT 22 (AM2302)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  float humidity = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float temperature = dht.readTemperature();

  // Check for presence of data
  if (!isnan(humidity) && !isnan(temperature)) {
  
  Serial.print("Temperature: ");
  Serial.print(temperature); 
  Serial.print(", Humidity: ");
  Serial.println(humidity);
  
  }

  

}
