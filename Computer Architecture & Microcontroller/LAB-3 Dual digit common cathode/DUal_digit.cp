#line 1 "E:/ICE 3-1/Microcontroller and Computer Architecture/Lab/LAB-3 Dual digit/DUal_digit.c"
char array_cc[]={0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F};
void main() {
 int i=0, x, y, j=0;
 TRISB = 0x00;
 TRISC = 0x00;
 portb = 0x00;
 portc = 0xff;
 while(1)
 {
 for(j=0;j<50;j++)
 {
 portb=array_cc[i/10];
 portc.f0=1;
 delay_ms(10);
 portc.f0=0;

 portb=array_cc[i%10];
 portc.f1=1;
 delay_ms(10);
 portc.f1=0;

 }
 i++;
 if(i>99)
 i=0;
 }
}
