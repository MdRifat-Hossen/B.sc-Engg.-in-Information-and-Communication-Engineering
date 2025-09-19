
_main:

;DUal_digit.c,2 :: 		void main() {
;DUal_digit.c,3 :: 		int i=0, x, y, j=0;
	CLRF       main_i_L0+0
	CLRF       main_i_L0+1
	CLRF       main_j_L0+0
	CLRF       main_j_L0+1
;DUal_digit.c,4 :: 		TRISB = 0x00;
	CLRF       TRISB+0
;DUal_digit.c,5 :: 		TRISC = 0x00;
	CLRF       TRISC+0
;DUal_digit.c,6 :: 		portb = 0x00;
	CLRF       PORTB+0
;DUal_digit.c,7 :: 		portc = 0xff;
	MOVLW      255
	MOVWF      PORTC+0
;DUal_digit.c,8 :: 		while(1)
L_main0:
;DUal_digit.c,10 :: 		for(j=0;j<50;j++)
	CLRF       main_j_L0+0
	CLRF       main_j_L0+1
L_main2:
	MOVLW      128
	XORWF      main_j_L0+1, 0
	MOVWF      R0+0
	MOVLW      128
	SUBWF      R0+0, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main9
	MOVLW      50
	SUBWF      main_j_L0+0, 0
L__main9:
	BTFSC      STATUS+0, 0
	GOTO       L_main3
;DUal_digit.c,12 :: 		portb=array_cc[i/10];
	MOVLW      10
	MOVWF      R4+0
	MOVLW      0
	MOVWF      R4+1
	MOVF       main_i_L0+0, 0
	MOVWF      R0+0
	MOVF       main_i_L0+1, 0
	MOVWF      R0+1
	CALL       _Div_16x16_S+0
	MOVF       R0+0, 0
	ADDLW      _array_cc+0
	MOVWF      FSR
	MOVF       INDF+0, 0
	MOVWF      PORTB+0
;DUal_digit.c,13 :: 		portc.f0=1;
	BSF        PORTC+0, 0
;DUal_digit.c,14 :: 		delay_ms(10);
	MOVLW      26
	MOVWF      R12+0
	MOVLW      248
	MOVWF      R13+0
L_main5:
	DECFSZ     R13+0, 1
	GOTO       L_main5
	DECFSZ     R12+0, 1
	GOTO       L_main5
	NOP
;DUal_digit.c,15 :: 		portc.f0=0;
	BCF        PORTC+0, 0
;DUal_digit.c,17 :: 		portb=array_cc[i%10];
	MOVLW      10
	MOVWF      R4+0
	MOVLW      0
	MOVWF      R4+1
	MOVF       main_i_L0+0, 0
	MOVWF      R0+0
	MOVF       main_i_L0+1, 0
	MOVWF      R0+1
	CALL       _Div_16x16_S+0
	MOVF       R8+0, 0
	MOVWF      R0+0
	MOVF       R8+1, 0
	MOVWF      R0+1
	MOVF       R0+0, 0
	ADDLW      _array_cc+0
	MOVWF      FSR
	MOVF       INDF+0, 0
	MOVWF      PORTB+0
;DUal_digit.c,18 :: 		portc.f1=1;
	BSF        PORTC+0, 1
;DUal_digit.c,19 :: 		delay_ms(10);
	MOVLW      26
	MOVWF      R12+0
	MOVLW      248
	MOVWF      R13+0
L_main6:
	DECFSZ     R13+0, 1
	GOTO       L_main6
	DECFSZ     R12+0, 1
	GOTO       L_main6
	NOP
;DUal_digit.c,20 :: 		portc.f1=0;
	BCF        PORTC+0, 1
;DUal_digit.c,10 :: 		for(j=0;j<50;j++)
	INCF       main_j_L0+0, 1
	BTFSC      STATUS+0, 2
	INCF       main_j_L0+1, 1
;DUal_digit.c,22 :: 		}
	GOTO       L_main2
L_main3:
;DUal_digit.c,23 :: 		i++;
	INCF       main_i_L0+0, 1
	BTFSC      STATUS+0, 2
	INCF       main_i_L0+1, 1
;DUal_digit.c,24 :: 		if(i>99)
	MOVLW      128
	MOVWF      R0+0
	MOVLW      128
	XORWF      main_i_L0+1, 0
	SUBWF      R0+0, 0
	BTFSS      STATUS+0, 2
	GOTO       L__main10
	MOVF       main_i_L0+0, 0
	SUBLW      99
L__main10:
	BTFSC      STATUS+0, 0
	GOTO       L_main7
;DUal_digit.c,25 :: 		i=0;
	CLRF       main_i_L0+0
	CLRF       main_i_L0+1
L_main7:
;DUal_digit.c,26 :: 		}
	GOTO       L_main0
;DUal_digit.c,27 :: 		}
L_end_main:
	GOTO       $+0
; end of _main
