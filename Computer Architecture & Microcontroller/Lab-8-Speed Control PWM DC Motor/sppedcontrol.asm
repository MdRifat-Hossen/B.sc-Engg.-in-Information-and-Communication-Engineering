
_main:

;sppedcontrol.c,1 :: 		void main()
;sppedcontrol.c,3 :: 		unsigned short duty = 0; // PWM duty cycle (0–255)
	CLRF       main_duty_L0+0
;sppedcontrol.c,5 :: 		TRISD = 0xFF;   // PORTD as input for buttons
	MOVLW      255
	MOVWF      TRISD+0
;sppedcontrol.c,6 :: 		TRISB = 0x00;   // PORTB as output for direction control
	CLRF       TRISB+0
;sppedcontrol.c,7 :: 		TRISC.F2 = 0;   // Set RC2 as output for PWM
	BCF        TRISC+0, 2
;sppedcontrol.c,10 :: 		PORTB.F0 = 1;   // IN1
	BSF        PORTB+0, 0
;sppedcontrol.c,11 :: 		PORTB.F1 = 0;   // IN2
	BCF        PORTB+0, 1
;sppedcontrol.c,13 :: 		PWM1_Init(1000);         // Initialize PWM at 1 kHz
	BSF        T2CON+0, 0
	BSF        T2CON+0, 1
	MOVLW      124
	MOVWF      PR2+0
	CALL       _PWM1_Init+0
;sppedcontrol.c,14 :: 		PWM1_Start();            // Start PWM
	CALL       _PWM1_Start+0
;sppedcontrol.c,15 :: 		PWM1_Set_Duty(duty);     // Start with 0 duty
	MOVF       main_duty_L0+0, 0
	MOVWF      FARG_PWM1_Set_Duty_new_duty+0
	CALL       _PWM1_Set_Duty+0
;sppedcontrol.c,17 :: 		while (1)
L_main0:
;sppedcontrol.c,19 :: 		if (RD0_bit && duty <= 240) // Speed up
	BTFSS      RD0_bit+0, BitPos(RD0_bit+0)
	GOTO       L_main4
	MOVF       main_duty_L0+0, 0
	SUBLW      240
	BTFSS      STATUS+0, 0
	GOTO       L_main4
L__main20:
;sppedcontrol.c,21 :: 		Delay_ms(100); // Debounce
	MOVLW      2
	MOVWF      R11+0
	MOVLW      4
	MOVWF      R12+0
	MOVLW      186
	MOVWF      R13+0
L_main5:
	DECFSZ     R13+0, 1
	GOTO       L_main5
	DECFSZ     R12+0, 1
	GOTO       L_main5
	DECFSZ     R11+0, 1
	GOTO       L_main5
	NOP
;sppedcontrol.c,22 :: 		if (RD0_bit && duty <= 240)
	BTFSS      RD0_bit+0, BitPos(RD0_bit+0)
	GOTO       L_main8
	MOVF       main_duty_L0+0, 0
	SUBLW      240
	BTFSS      STATUS+0, 0
	GOTO       L_main8
L__main19:
;sppedcontrol.c,24 :: 		duty += 10;
	MOVLW      10
	ADDWF      main_duty_L0+0, 0
	MOVWF      R0+0
	MOVF       R0+0, 0
	MOVWF      main_duty_L0+0
;sppedcontrol.c,25 :: 		PWM1_Set_Duty(duty);
	MOVF       R0+0, 0
	MOVWF      FARG_PWM1_Set_Duty_new_duty+0
	CALL       _PWM1_Set_Duty+0
;sppedcontrol.c,26 :: 		}
L_main8:
;sppedcontrol.c,27 :: 		}
L_main4:
;sppedcontrol.c,29 :: 		if (RD1_bit && duty >= 10) // Slow down
	BTFSS      RD1_bit+0, BitPos(RD1_bit+0)
	GOTO       L_main11
	MOVLW      10
	SUBWF      main_duty_L0+0, 0
	BTFSS      STATUS+0, 0
	GOTO       L_main11
L__main18:
;sppedcontrol.c,31 :: 		Delay_ms(100); // Debounce
	MOVLW      2
	MOVWF      R11+0
	MOVLW      4
	MOVWF      R12+0
	MOVLW      186
	MOVWF      R13+0
L_main12:
	DECFSZ     R13+0, 1
	GOTO       L_main12
	DECFSZ     R12+0, 1
	GOTO       L_main12
	DECFSZ     R11+0, 1
	GOTO       L_main12
	NOP
;sppedcontrol.c,32 :: 		if (RD1_bit && duty >= 10)
	BTFSS      RD1_bit+0, BitPos(RD1_bit+0)
	GOTO       L_main15
	MOVLW      10
	SUBWF      main_duty_L0+0, 0
	BTFSS      STATUS+0, 0
	GOTO       L_main15
L__main17:
;sppedcontrol.c,34 :: 		duty -= 10;
	MOVLW      10
	SUBWF      main_duty_L0+0, 0
	MOVWF      R0+0
	MOVF       R0+0, 0
	MOVWF      main_duty_L0+0
;sppedcontrol.c,35 :: 		PWM1_Set_Duty(duty);
	MOVF       R0+0, 0
	MOVWF      FARG_PWM1_Set_Duty_new_duty+0
	CALL       _PWM1_Set_Duty+0
;sppedcontrol.c,36 :: 		}
L_main15:
;sppedcontrol.c,37 :: 		}
L_main11:
;sppedcontrol.c,39 :: 		Delay_ms(10); // Small loop delay
	MOVLW      26
	MOVWF      R12+0
	MOVLW      248
	MOVWF      R13+0
L_main16:
	DECFSZ     R13+0, 1
	GOTO       L_main16
	DECFSZ     R12+0, 1
	GOTO       L_main16
	NOP
;sppedcontrol.c,40 :: 		}
	GOTO       L_main0
;sppedcontrol.c,41 :: 		}
L_end_main:
	GOTO       $+0
; end of _main
