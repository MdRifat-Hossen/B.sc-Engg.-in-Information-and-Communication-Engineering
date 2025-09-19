
_main:

;ADCINPUT.c,5 :: 		void main()
;ADCINPUT.c,8 :: 		UART1_Init(9600);
	MOVLW      51
	MOVWF      SPBRG+0
	BSF        TXSTA+0, 2
	CALL       _UART1_Init+0
;ADCINPUT.c,10 :: 		ADC_Init();
	CALL       _ADC_Init+0
;ADCINPUT.c,12 :: 		while(1)
L_main0:
;ADCINPUT.c,15 :: 		valADC = ADC_Read(0);
	CLRF       FARG_ADC_Read_channel+0
	CALL       _ADC_Read+0
	MOVF       R0+0, 0
	MOVWF      _valADC+0
	MOVF       R0+1, 0
	MOVWF      _valADC+1
;ADCINPUT.c,17 :: 		IntToStr(valADC,x);
	MOVF       R0+0, 0
	MOVWF      FARG_IntToStr_input+0
	MOVF       R0+1, 0
	MOVWF      FARG_IntToStr_input+1
	MOVLW      _x+0
	MOVWF      FARG_IntToStr_output+0
	CALL       _IntToStr+0
;ADCINPUT.c,19 :: 		UART1_Write_Text("Analog value = ");
	MOVLW      ?lstr1_ADCINPUT+0
	MOVWF      FARG_UART1_Write_Text_uart_text+0
	CALL       _UART1_Write_Text+0
;ADCINPUT.c,20 :: 		UART1_Write_Text(x);
	MOVLW      _x+0
	MOVWF      FARG_UART1_Write_Text_uart_text+0
	CALL       _UART1_Write_Text+0
;ADCINPUT.c,22 :: 		strcpy(x,"");
	MOVLW      _x+0
	MOVWF      FARG_strcpy_to+0
	MOVLW      ?lstr2_ADCINPUT+0
	MOVWF      FARG_strcpy_from+0
	CALL       _strcpy+0
;ADCINPUT.c,23 :: 		UART1_Write(13);
	MOVLW      13
	MOVWF      FARG_UART1_Write_data_+0
	CALL       _UART1_Write+0
;ADCINPUT.c,24 :: 		Delay_ms(1000);
	MOVLW      11
	MOVWF      R11+0
	MOVLW      38
	MOVWF      R12+0
	MOVLW      93
	MOVWF      R13+0
L_main2:
	DECFSZ     R13+0, 1
	GOTO       L_main2
	DECFSZ     R12+0, 1
	GOTO       L_main2
	DECFSZ     R11+0, 1
	GOTO       L_main2
	NOP
	NOP
;ADCINPUT.c,25 :: 		}
	GOTO       L_main0
;ADCINPUT.c,26 :: 		}
L_end_main:
	GOTO       $+0
; end of _main
