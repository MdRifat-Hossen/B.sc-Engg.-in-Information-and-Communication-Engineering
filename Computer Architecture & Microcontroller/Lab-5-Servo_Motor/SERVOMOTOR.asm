
_servoRotate0:

;SERVOMOTOR.c,1 :: 		void servoRotate0() //0 Degree
;SERVOMOTOR.c,4 :: 		for(i=0;i<50;i++)
	CLRF       R1+0
	CLRF       R1+1
L_servoRotate00:
	MOVLW      0
	SUBWF      R1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__servoRotate021
	MOVLW      50
	SUBWF      R1+0, 0
L__servoRotate021:
	BTFSC      STATUS+0, 0
	GOTO       L_servoRotate01
;SERVOMOTOR.c,6 :: 		PORTB.F0 = 1;
	BSF        PORTB+0, 0
;SERVOMOTOR.c,7 :: 		Delay_us(800);
	MOVLW      3
	MOVWF      R12+0
	MOVLW      18
	MOVWF      R13+0
L_servoRotate03:
	DECFSZ     R13+0, 1
	GOTO       L_servoRotate03
	DECFSZ     R12+0, 1
	GOTO       L_servoRotate03
	NOP
;SERVOMOTOR.c,8 :: 		PORTB.F0 = 0;
	BCF        PORTB+0, 0
;SERVOMOTOR.c,9 :: 		Delay_us(19200);
	MOVLW      50
	MOVWF      R12+0
	MOVLW      221
	MOVWF      R13+0
L_servoRotate04:
	DECFSZ     R13+0, 1
	GOTO       L_servoRotate04
	DECFSZ     R12+0, 1
	GOTO       L_servoRotate04
	NOP
	NOP
;SERVOMOTOR.c,4 :: 		for(i=0;i<50;i++)
	INCF       R1+0, 1
	BTFSC      STATUS+0, 2
	INCF       R1+1, 1
;SERVOMOTOR.c,10 :: 		}
	GOTO       L_servoRotate00
L_servoRotate01:
;SERVOMOTOR.c,11 :: 		}
L_end_servoRotate0:
	RETURN
; end of _servoRotate0

_servoRotate90:

;SERVOMOTOR.c,12 :: 		void servoRotate90() //90 Degree
;SERVOMOTOR.c,15 :: 		for(i=0;i<50;i++)
	CLRF       R1+0
	CLRF       R1+1
L_servoRotate905:
	MOVLW      0
	SUBWF      R1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__servoRotate9023
	MOVLW      50
	SUBWF      R1+0, 0
L__servoRotate9023:
	BTFSC      STATUS+0, 0
	GOTO       L_servoRotate906
;SERVOMOTOR.c,17 :: 		PORTB.F0 = 1;
	BSF        PORTB+0, 0
;SERVOMOTOR.c,18 :: 		Delay_us(1500);
	MOVLW      4
	MOVWF      R12+0
	MOVLW      228
	MOVWF      R13+0
L_servoRotate908:
	DECFSZ     R13+0, 1
	GOTO       L_servoRotate908
	DECFSZ     R12+0, 1
	GOTO       L_servoRotate908
	NOP
;SERVOMOTOR.c,19 :: 		PORTB.F0 = 0;
	BCF        PORTB+0, 0
;SERVOMOTOR.c,20 :: 		Delay_us(18500);
	MOVLW      49
	MOVWF      R12+0
	MOVLW      11
	MOVWF      R13+0
L_servoRotate909:
	DECFSZ     R13+0, 1
	GOTO       L_servoRotate909
	DECFSZ     R12+0, 1
	GOTO       L_servoRotate909
	NOP
	NOP
;SERVOMOTOR.c,15 :: 		for(i=0;i<50;i++)
	INCF       R1+0, 1
	BTFSC      STATUS+0, 2
	INCF       R1+1, 1
;SERVOMOTOR.c,21 :: 		}
	GOTO       L_servoRotate905
L_servoRotate906:
;SERVOMOTOR.c,22 :: 		}
L_end_servoRotate90:
	RETURN
; end of _servoRotate90

_servoRotate180:

;SERVOMOTOR.c,23 :: 		void servoRotate180() //180 Degree
;SERVOMOTOR.c,26 :: 		for(i=0;i<50;i++)
	CLRF       R1+0
	CLRF       R1+1
L_servoRotate18010:
	MOVLW      0
	SUBWF      R1+1, 0
	BTFSS      STATUS+0, 2
	GOTO       L__servoRotate18025
	MOVLW      50
	SUBWF      R1+0, 0
L__servoRotate18025:
	BTFSC      STATUS+0, 0
	GOTO       L_servoRotate18011
;SERVOMOTOR.c,28 :: 		PORTB.F0 = 1;
	BSF        PORTB+0, 0
;SERVOMOTOR.c,29 :: 		Delay_us(2200);
	MOVLW      6
	MOVWF      R12+0
	MOVLW      181
	MOVWF      R13+0
L_servoRotate18013:
	DECFSZ     R13+0, 1
	GOTO       L_servoRotate18013
	DECFSZ     R12+0, 1
	GOTO       L_servoRotate18013
	NOP
	NOP
;SERVOMOTOR.c,30 :: 		PORTB.F0 = 0;
	BCF        PORTB+0, 0
;SERVOMOTOR.c,31 :: 		Delay_us(17800);
	MOVLW      47
	MOVWF      R12+0
	MOVLW      58
	MOVWF      R13+0
L_servoRotate18014:
	DECFSZ     R13+0, 1
	GOTO       L_servoRotate18014
	DECFSZ     R12+0, 1
	GOTO       L_servoRotate18014
	NOP
;SERVOMOTOR.c,26 :: 		for(i=0;i<50;i++)
	INCF       R1+0, 1
	BTFSC      STATUS+0, 2
	INCF       R1+1, 1
;SERVOMOTOR.c,32 :: 		}
	GOTO       L_servoRotate18010
L_servoRotate18011:
;SERVOMOTOR.c,33 :: 		}
L_end_servoRotate180:
	RETURN
; end of _servoRotate180

_main:

;SERVOMOTOR.c,34 :: 		void main()
;SERVOMOTOR.c,36 :: 		TRISB = 0; // PORTB as Ouput Port
	CLRF       TRISB+0
;SERVOMOTOR.c,37 :: 		do
L_main15:
;SERVOMOTOR.c,39 :: 		servoRotate0(); //0 Degree
	CALL       _servoRotate0+0
;SERVOMOTOR.c,40 :: 		Delay_ms(2000);
	MOVLW      21
	MOVWF      R11+0
	MOVLW      75
	MOVWF      R12+0
	MOVLW      190
	MOVWF      R13+0
L_main18:
	DECFSZ     R13+0, 1
	GOTO       L_main18
	DECFSZ     R12+0, 1
	GOTO       L_main18
	DECFSZ     R11+0, 1
	GOTO       L_main18
	NOP
;SERVOMOTOR.c,41 :: 		servoRotate90(); //90 Degree
	CALL       _servoRotate90+0
;SERVOMOTOR.c,42 :: 		Delay_ms(2000);
	MOVLW      21
	MOVWF      R11+0
	MOVLW      75
	MOVWF      R12+0
	MOVLW      190
	MOVWF      R13+0
L_main19:
	DECFSZ     R13+0, 1
	GOTO       L_main19
	DECFSZ     R12+0, 1
	GOTO       L_main19
	DECFSZ     R11+0, 1
	GOTO       L_main19
	NOP
;SERVOMOTOR.c,43 :: 		servoRotate180(); //180 Degree
	CALL       _servoRotate180+0
;SERVOMOTOR.c,44 :: 		}while(1);
	GOTO       L_main15
;SERVOMOTOR.c,45 :: 		}
L_end_main:
	GOTO       $+0
; end of _main
