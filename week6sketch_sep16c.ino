#include <Arduino_LSM6DS3.h>

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Initialize the IMU (Gyroscope sensor)
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.println("Gyroscope data logging...");
  Serial.println("Time (ms),X-axis (dps),Y-axis (dps),Z-axis (dps)");
}

void loop() {
  float x, y, z;

  // Read gyroscope values
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x, y, z);
    
    // Log timestamp and gyroscope values
    Serial.print(millis());
    Serial.print(",");
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.println(z);
    
    // Delay to simulate real-time data logging
    delay(100); // Log every 100ms (adjust as needed)
  }
}
