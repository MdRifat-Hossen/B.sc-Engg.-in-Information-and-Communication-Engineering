void main() {
    TRISB = 0x00; //Set PortB as Output
    PORTB = 0x00; //Initialize Portb as off state
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