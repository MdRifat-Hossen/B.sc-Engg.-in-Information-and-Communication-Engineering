void main()
{
    unsigned short duty = 0; // PWM duty cycle (0–255)

    TRISD = 0xFF;   // PORTD as input for buttons
    TRISB = 0x00;   // PORTB as output for direction control
    TRISC.F2 = 0;   // Set RC2 as output for PWM

    // Run motor in anticlockwise direction
    PORTB.F0 = 1;   // IN1
    PORTB.F1 = 0;   // IN2

    PWM1_Init(1000);         // Initialize PWM at 1 kHz
    PWM1_Start();            // Start PWM
    PWM1_Set_Duty(duty);     // Start with 0 duty

    while (1)
    {
        if (RD0_bit && duty <= 240) // Speed up
        {
            Delay_ms(100); // Debounce
            if (RD0_bit && duty <= 240)
            {
                duty += 10;
                PWM1_Set_Duty(duty);
            }
        }

        if (RD1_bit && duty >= 10) // Slow down
        {
            Delay_ms(100); // Debounce
            if (RD1_bit && duty >= 10)
            {
                duty -= 10;
                PWM1_Set_Duty(duty);
            }
        }

        Delay_ms(10); // Small loop delay
    }
}