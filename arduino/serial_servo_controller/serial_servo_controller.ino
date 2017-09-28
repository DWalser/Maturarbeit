#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


Adafruit_PWMServoDriver pwm0 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwm1 = Adafruit_PWMServoDriver(0x41);
Adafruit_PWMServoDriver pwm2 = Adafruit_PWMServoDriver(0x42);

int pulsewidth(float angle){
  float pw_ms = (angle + 78.75)/112.5;
  return int(1.*4096.0/20.0*pw_ms);
}

void setup() {  
  Serial.begin(9600);

  pwm0.begin();
  pwm0.setPWMFreq(55.55555);  // 55.55 * 0.9 = 50 Hz
  pwm0.setPin(0, pulsewidth(90)); // 307 = 4096 / 20ms * 1.5ms

  pwm1.begin();
  pwm1.setPWMFreq(55.55555);  // 55.55 * 0.9 = 50 Hz
  pwm1.setPin(0, pulsewidth(90)); // 307 = 4096 / 20ms * 1.5ms

  pwm2.begin();
  pwm2.setPWMFreq(55.55555);  // 55.55 * 0.9 = 50 Hz
  pwm2.setPin(0, pulsewidth(90)); // 307 = 4096 / 20ms * 1.5ms
  
}

void loop() {
  if(Serial.available() > 2){
    char input = Serial.read();
    
    if(input == 'S'){
      int servo = Serial.read();
      int angle = Serial.read();
      int board = servo >> 4;
      servo = servo & 0x0F;
      //Serial.print("Board: ");
      //Serial.print(board);
      //Serial.print(" Servo: ");
      //Serial.print(servo);
      //Serial.print(" Angle: ");
      //Serial.println(angle);
      if(board == 0){
        pwm0.setPin(servo, pulsewidth(angle)); // 307 = 4096 / 20ms * 1.5ms
        }
      else if(board == 1){
        pwm1.setPin(servo, pulsewidth(angle)); // 307 = 4096 / 20ms * 1.5ms
        }
      else if(board == 2){
        pwm2.setPin(servo, pulsewidth(angle)); // 307 = 4096 / 20ms * 1.5ms
        }
    }
    delay(10);
    Serial.flush();
    delay(10);
  }
}
