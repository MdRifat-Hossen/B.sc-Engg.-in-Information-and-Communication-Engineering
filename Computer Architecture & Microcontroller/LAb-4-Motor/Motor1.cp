#line 1 "E:/ICE 3-1/Microcontroller and Computer Architecture/Lab/LAb-4-Motor/Motor1.c"
void main() {
 TRISB=0x00;
 portb=0x00;

 while(1)
 {
 portb.f0=0;
 portb.f1=0;
 delay_ms(2000);

 portb.f0=1;
 portb.f1=0;
 delay_ms(2000);

 portb.f0=0;
 portb.f1=1;
 delay_ms(2000);

 portb.f0=1;
 portb.f1=1;
 delay_ms(2000);

 }
}
