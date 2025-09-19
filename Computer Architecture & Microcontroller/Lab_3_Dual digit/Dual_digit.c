char segment[]={0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F};
int i=0;
void main() {
     trisb=0x00;       //portB set as output
     trisc=0x00;       //PortC set as output
     portb=0x00;       //Initialize portb as off state
     portc=0x00;       //Initialize portC as off state
     trisd=0xff;       //PortD set as Input
     portd=0;          //Initialize portD as Off state
     while(1){
          portc.f0=0;               //  First Digit On
          portb=segment[i/10];      //  First Digit Calculate
          delay_ms(30);
          portc.f0=1;               //  First Digit OFF


          portc.f1=0;               //  Second Digit On
          portb=segment[i%10];      // Second Digit Calculate
          delay_ms(30);
          portc.f1=1;                //  Second Digit OFF

          //increasing
          if(portd.f0==1){
             i++;
             while(portd.f0)
                 portd.f0==1;
          }
          //decreasing
          if(portd.f1==1){
             i--;
             while(portd.f1)
                 portd.f1==1;
          }
          if(i<0 || i>99)
             i=0;
             i++;
     }
}
