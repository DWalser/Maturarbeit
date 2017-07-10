#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x42);

int pulsewidth(float angle){
  float pw_ms = (angle + 78.75)/112.5;
  return int(1.*4096.0/20.0*pw_ms);
}

void setup() {  
  Serial.begin(9600);

  pwm.begin();
  pwm.setPWMFreq(55.55555);  // 55.55 * 0.9 = 50 Hz

  pwm.setPin(0, pulsewidth(90)); // 307 = 4096 / 20ms * 1.5ms
  
}

void loop() {
  if(Serial.available() > 2){
    char input = Serial.read();
    
    if(input == 'S'){
      int servo = Serial.read();
      int angle = Serial.read();
      int board = servo >> 4;
      servo = servo & 0x0F;
      //Serial.print(board);
      //Serial.println(angle);
      pwm.setPin(servo, pulsewidth(angle)); // 307 = 4096 / 20ms * 1.5ms
    }
    delay(10);
    Serial.flush();
    delay(10);
  }
}
