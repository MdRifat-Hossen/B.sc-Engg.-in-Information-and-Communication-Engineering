 char arr[]={ 0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f};
           int i;
void main() {
        TRISB=0x00;
        portb=0x00;

        while(1){
        
              for(i=0;i<10;i++)
              {
            portb=arr[i];
            delay_ms(1000);
        
            }
        for(i=9;i>0;i--)
              {
            portb=arr[i];
            delay_ms(1000);

            }
        
        }
}