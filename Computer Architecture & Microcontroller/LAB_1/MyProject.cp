#line 1 "E:/Lab/MyProject.c"
void main() {
 TRISB = 0x00;
 PORTB = 0x00;
 while(1)
 {
 portb.f0=0xff;
 portb.f1=0x00;
 delay_ms(500);

 portb.f0=0x00;
 portb.f1=0xff;
 delay_ms(500);
 }
}
