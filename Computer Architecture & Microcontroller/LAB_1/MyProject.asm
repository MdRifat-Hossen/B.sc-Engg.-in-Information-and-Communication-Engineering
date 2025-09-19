
_main:

;MyProject.c,1 :: 		void main() {
;MyProject.c,2 :: 		TRISB = 0x00; //Set PortB as Output
	CLRF       TRISB+0
;MyProject.c,3 :: 		PORTB = 0x00; //Initialize Portb as off state
	CLRF       PORTB+0
;MyProject.c,4 :: 		while(1)
L_main0:
;MyProject.c,6 :: 		portb.f0=0xff;
	BSF        PORTB+0, 0
;MyProject.c,7 :: 		portb.f1=0x00;
	BCF        PORTB+0, 1
;MyProject.c,8 :: 		delay_ms(500);
	MOVLW      6
	MOVWF      R11+0
	MOVLW      19
	MOVWF      R12+0
	MOVLW      173
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
;MyProject.c,10 :: 		portb.f0=0x00;
	BCF        PORTB+0, 0
;MyProject.c,11 :: 		portb.f1=0xff;
	BSF        PORTB+0, 1
;MyProject.c,12 :: 		delay_ms(500);
	MOVLW      6
	MOVWF      R11+0
	MOVLW      19
	MOVWF      R12+0
	MOVLW      173
	MOVWF      R13+0
L_main3:
	DECFSZ     R13+0, 1
	GOTO       L_main3
	DECFSZ     R12+0, 1
	GOTO       L_main3
	DECFSZ     R11+0, 1
	GOTO       L_main3
	NOP
	NOP
;MyProject.c,13 :: 		}
	GOTO       L_main0
;MyProject.c,14 :: 		}
L_end_main:
	GOTO       $+0
; end of _main
