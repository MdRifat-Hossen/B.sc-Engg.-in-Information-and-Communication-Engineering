
_main:

;Motor1.c,1 :: 		void main() {
;Motor1.c,2 :: 		TRISB=0x00;
	CLRF       TRISB+0
;Motor1.c,3 :: 		portb=0x00;
	CLRF       PORTB+0
;Motor1.c,5 :: 		while(1)
L_main0:
;Motor1.c,7 :: 		portb.f0=0;
	BCF        PORTB+0, 0
;Motor1.c,8 :: 		portb.f1=0;
	BCF        PORTB+0, 1
;Motor1.c,9 :: 		delay_ms(2000);
	MOVLW      21
	MOVWF      R11+0
	MOVLW      75
	MOVWF      R12+0
	MOVLW      190
	MOVWF      R13+0
L_main2:
	DECFSZ     R13+0, 1
	GOTO       L_main2
	DECFSZ     R12+0, 1
	GOTO       L_main2
	DECFSZ     R11+0, 1
	GOTO       L_main2
	NOP
;Motor1.c,11 :: 		portb.f0=1;
	BSF        PORTB+0, 0
;Motor1.c,12 :: 		portb.f1=0;
	BCF        PORTB+0, 1
;Motor1.c,13 :: 		delay_ms(2000);
	MOVLW      21
	MOVWF      R11+0
	MOVLW      75
	MOVWF      R12+0
	MOVLW      190
	MOVWF      R13+0
L_main3:
	DECFSZ     R13+0, 1
	GOTO       L_main3
	DECFSZ     R12+0, 1
	GOTO       L_main3
	DECFSZ     R11+0, 1
	GOTO       L_main3
	NOP
;Motor1.c,15 :: 		portb.f0=0;
	BCF        PORTB+0, 0
;Motor1.c,16 :: 		portb.f1=1;
	BSF        PORTB+0, 1
;Motor1.c,17 :: 		delay_ms(2000);
	MOVLW      21
	MOVWF      R11+0
	MOVLW      75
	MOVWF      R12+0
	MOVLW      190
	MOVWF      R13+0
L_main4:
	DECFSZ     R13+0, 1
	GOTO       L_main4
	DECFSZ     R12+0, 1
	GOTO       L_main4
	DECFSZ     R11+0, 1
	GOTO       L_main4
	NOP
;Motor1.c,19 :: 		portb.f0=1;
	BSF        PORTB+0, 0
;Motor1.c,20 :: 		portb.f1=1;
	BSF        PORTB+0, 1
;Motor1.c,21 :: 		delay_ms(2000);
	MOVLW      21
	MOVWF      R11+0
	MOVLW      75
	MOVWF      R12+0
	MOVLW      190
	MOVWF      R13+0
L_main5:
	DECFSZ     R13+0, 1
	GOTO       L_main5
	DECFSZ     R12+0, 1
	GOTO       L_main5
	DECFSZ     R11+0, 1
	GOTO       L_main5
	NOP
;Motor1.c,23 :: 		}
	GOTO       L_main0
;Motor1.c,24 :: 		}
L_end_main:
	GOTO       $+0
; end of _main
