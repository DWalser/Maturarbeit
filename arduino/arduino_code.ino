#include <Servo.h>

// Servos to be used
Servo shoulder;
Servo elbow;
Servo wrist;
Servo base;
Servo gripper;

void setup()
{
  // tell servos what pins they are on
  shoulder.attach(10);
  elbow.attach(9);
  wrist.attach(5);
  base.attach(6);
  gripper.attach(11);
  
  // initialize the serial port
  Serial.begin(9600);
  
  // Put it in a default position
  shoulder.write(90);
  elbow.write(90);
  wrist.write(90);
  base.write(90);
  gripper.write(0);
}

int num;
int angle;

void loop()
{
  // wait for the servo number
  while(Serial.available() == 0);
  num = Serial.read();
  
  // wait for the servo angle
  while(Serial.available() == 0);
  angle = Serial.read();
  
  // Turn selected servo to the angle
  if (num == 10)
    shoulder.write(angle);
  else if (num == 9)
    elbow.write(angle);
  else if (num == 5)
    wrist.write(angle);
  else if (num == 6)
    base.write(angle);
  else if (num == 11)
    gripper.write(angle);
}
