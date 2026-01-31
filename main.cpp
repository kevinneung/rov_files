#include <Arduino.h>

// put function declarations here:
int xPin = A0;
int yPin = A1;
int buttonPin = 2;
int xVal;
int yVal;
int buttonState;

void setup() {
  Serial.begin(9600);
  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
  pinMode(buttonPin, INPUT_PULLUP);

}

void loop() {
  xVal = analogRead(xPin);
  yVal = analogRead(yPin);
  buttonState = digitalRead(buttonPin);

  // Print statement: X: XXXX | Y: YYYY | Button: 0/1
  Serial.print("X: ");
  Serial.print(xVal);
  Serial.print(" | Y: ");
  Serial.print(yVal);
  Serial.print(" | Button: ");
  Serial.print(buttonState);
  Serial.print("\n");
  
  delay(100);
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}