#include <Servo.h>

// Servos to be used
Servo servo;
//int servonumber;
//int angle;

int numberCollect(int digits){
  int numberinput = 0;
  for (int i=0; i<digits; i++){
    char readbyte = Serial.read();
    numberinput *= 10;
    numberinput += (readbyte-'0');
    //delay(10);
  }
  return numberinput;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(10);
    // Put it in a default position, if needed
  servo.write(90);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 5){
    char input = Serial.read();
    
    if(input == 'S'){
      int servonumber = numberCollect(2);
      int angle = numberCollect(3);
      Serial.print("S");
      Serial.print(servonumber);
      Serial.print("W");
      Serial.println(angle);
      if(servonumber == 1){
        servo.write(angle);
      }
    }
    delay(500);
    Serial.flush();
    delay(500);
  }
  delay(500);
  Serial.println("waiting..");
}
