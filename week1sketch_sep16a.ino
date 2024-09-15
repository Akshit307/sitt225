// Include necessary libraries
int ledPin = 13;  // Define the LED pin

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud
  pinMode(ledPin, OUTPUT);  // Set the LED pin as output
}

void loop() {
  if (Serial.available() > 0) {
    // Read the number sent by Python
    int blinkTimes = Serial.parseInt();
    
    // Blink the LED the received number of times
    for (int i = 0; i < blinkTimes; i++) {
      digitalWrite(ledPin, HIGH);  // Turn the LED on
      delay(1000);                 // Wait for 1 second
      digitalWrite(ledPin, LOW);   // Turn the LED off
      delay(1000);                 // Wait for 1 second
    }

    // Generate a random number to send back to Python
    int randomDelay = random(1, 6);  // Random number between 1 and 5
    Serial.println(randomDelay);     // Send the random number to Python
  }
}
