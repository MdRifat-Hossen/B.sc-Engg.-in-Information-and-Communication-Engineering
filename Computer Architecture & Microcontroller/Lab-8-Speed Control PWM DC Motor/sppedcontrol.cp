#line 1 "E:/ICE 3-1/Microcontroller and Computer Architecture/Lab/Lab-8-Speed Control PWM DC Motor/sppedcontrol.c"
void main()
{
 unsigned short duty = 0;

 TRISD = 0xFF;
 TRISB = 0x00;
 TRISC.F2 = 0;


 PORTB.F0 = 1;
 PORTB.F1 = 0;

 PWM1_Init(1000);
 PWM1_Start();
 PWM1_Set_Duty(duty);

 while (1)
 {
 if (RD0_bit && duty <= 240)
 {
 Delay_ms(100);
 if (RD0_bit && duty <= 240)
 {
 duty += 10;
 PWM1_Set_Duty(duty);
 }
 }

 if (RD1_bit && duty >= 10)
 {
 Delay_ms(100);
 if (RD1_bit && duty >= 10)
 {
 duty -= 10;
 PWM1_Set_Duty(duty);
 }
 }

 Delay_ms(10);
 }
}
