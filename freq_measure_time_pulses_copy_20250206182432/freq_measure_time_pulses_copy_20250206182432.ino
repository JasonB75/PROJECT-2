#include <FreqMeasure.h>

void setup() {
  Serial.begin(57600);
  FreqMeasure.begin();
}

void loop() {
  if (FreqMeasure.available() > 1 ) {
    int pulse1 = FreqMeasure.read();
    int pulse2 = FreqMeasure.read();

    if (pulse1 > pulse2){
      Serial.println(0);
    } else if (pulse1 < pulse2){
      Serial.println(1);
    }
    
  }
}