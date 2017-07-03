#include <Servo.h>

// Servos to be used
Servo servo;

void setup()
{
  // This is using pin 10 (change accordingly)
  servo.attach(10);
  
  // initialize the serial port
  Serial.begin(9600);
  
  // Put it in a default position, if needed
  servo.write(90);
}

int angle;

void loop()
{  
  // wait for the servo angle
  while(Serial.available() == 0);
  angle = Serial.read();
  
  servo.write(angle);
}
