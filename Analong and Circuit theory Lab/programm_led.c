void main() {
          TRISB=0x00;
          portb=0x00;
          portb.f0=1;
          delay_ms(5000);
          portb.f0=0;
          
}