.include "m328Pdef.inc"


.def temp  = R16
.def time1 = r17
.def time2 = r18
.def time3 = r19
.def sum40 = r20
.def dir   = r21
.def temp2 = R25
.def flag40khz = R23
.def pin40khz = r24



.org 0x0000
	rjmp start

.org 0x004           ; local da memoria do ext_int1 
	rjmp int1_calc

.org 0x001A   ; timer1 ovf
	rjmp timer1_ovf

.org 0x001C   ; local da memoria do TIM0_COMPA 
	rjmp TIM0_COMPA

;//////////////////////////////////////// CONFIGURACAO INICIAL ////////////////////////////////////////////

start:

	;desativa interrupções
	cli
	
	ldi temp,0b00001111 ; saidas para sinal de 40kHz, 1 para cada direcao
	out DDRC,temp
	
	ldi temp,0b00000001 ;saida Direcao 4 (Oeste) + gravaçao e crystal
	out DDRB,temp
	
	ldi temp,0b11100100 ;saida Direcao 3,2,1, (Sul,Leste,Norte, 00 ,max485 select Rx/Tx, 00)
	out DDRD,temp

	;configura serial
		; baudrate 9600
	ldi temp,0b00000000 ;0
	sts UBRR0H, temp
	ldi temp,0b10000001 ;129
	sts UBRR0L, temp
		; ativa RX , 
	ldi temp,0b00010000; RX
	sts UCSR0B, temp
		; 8 Bit, sem paridade e 1 bit de fim 
	ldi temp, 0b00000110
	sts UCSR0C, temp

	ldi temp,0b10000001 ; pausar timer 0 e 1
	out GTCCR,temp
	
	;Timer0 40KHz
	ldi temp,0b00000000
	out TCCR0A,temp
	out TCCR0B,temp
	ldi temp,0b00000010    ;configura TCC0A    CTC mode	
	out TCCR0A,temp
	ldi temp,0b00000001    ;configura TCC0B    clk/1 
	out TCCR0B,temp
	ldi temp,0b11111000    ; OCR0A = 248  // para clk=20MHz
	out OCR0A,temp

	ldi temp,0b00000010    ;liga clk 40khz
	sts TIMSK0,temp

	;Timer1 config
	ldi temp,0b00000000
	sts TCCR1A,temp        ;configura TCCR1A    normal mode
	ldi temp,0b00000001    ;configura TCCR1B    clk/1
	sts TCCR1B,temp
	ldi temp,0b00000001    ;liga timer1 ovf
	sts TIMSK1,temp

	;interrupção externa
	ldi temp,0b00001100 ;  The rising edge of INT1 generates an interrupt request 
	sts EICRA,temp
	ldi temp,0b00000000 ; liga int1 depois
	out EIMSK,temp

	;zerar tudo 
	ldi temp,0b00000000

	ldi time1,0b00000000
	ldi time2,0b00000000
	ldi time3,0b00000000
	ldi sum40,0b00000000 ; contador de pulsos
	ldi dir,0b00000000
	ldi flag40khz,0b00000000    ; flag 40khz
	ldi pin40khz,0b00000000
	
	out PORTB,temp
	out PORTC,temp
	out PORTD,temp
	
	out TCNT0,temp		;|
	sts TCNT1L,temp     ; -->zerar o tempo									
	sts TCNT1H,temp		;|
	; zerra controles de direção
	cbi PORTD,5 ; entrada T1
	cbi PORTD,6 ; entrada T2
	cbi PORTD,7 ; entrada T3
	cbi PORTB,0 ; entrada T4
	; ativa interrupções
	sei	
	
	; vai para RX esperar comando				 
	rjmp RX

;//////////////////////////////// COMUNICACAO ///////////////////////////////////////
RX:
	; aguarda receber instrução em RX
	cbi PORTD,2 ;configura max485 para receber dados 
	
	lds temp, UCSR0A 
	sbrs temp, RXC0	;verifica se foram recebidos dados
	rjmp RX
	
	; guarda instrução recebida
	lds dir, UDR0
	ldi temp,0b00000000
	
	; desativa comunicação RX
	ldi temp,0b00000000
	sts UCSR0B, temp
	
	ldi time1,0b00000000
	ldi time2,0b00000000
	ldi time3,0b00000000
	
	; zera flag int1
	ldi temp,0b00000010
	sts EIFR, temp
	cli
	; verifica se comando = 1
	cpi dir, 0b00110001 
	BREQ DIR1 ; se = 1
	; verifica se comando = 2
	cpi dir, 0b00110010 
	BREQ DIR2
	; verifica se comando = 3
	cpi dir, 0b00110011 
	BREQ DIR3  ; se = 3
	; verifica se comando = 4
	cpi dir, 0b00110100 
	BREQ DIR4  ; se = 4
erro:
	ldi temp,0b00001000;TX on
	sts UCSR0B, temp
	sbi PORTD,2 ; configura max485 para enviar dados

	lds temp, UCSR0A 
	sbrs temp, UDRE0
	rjmp erro
	ldi r22,0b01000101
    sts UDR0, r22

	rjmp comfim



;////////////////////////////////////// SELECAO SAIDA-ENTRADA ////////////////////////////////////
DIR1:

	ldi pin40khz,0b00000001  ; saida T1
	
	; ativa int1
	ldi temp,0b00000010 
	out EIMSK,temp 
	
	ldi temp,0b00000000 ; reseta timer 0 e 1
	out TCNT0,temp		;|
	sts TCNT1L,temp     ; -->zerar o tempo									
	sts TCNT1H,temp		;|
	ldi time3,0b00000000

	ldi sum40, 0b00000000 ;zera contador de pulsos 
	
	out GTCCR,temp

;	cbi PORTD,5 ; entrada T4
	sbi PORTD,6 ; entrada T3 on
;	cbi PORTD,7 ; entrada T2
;	cbi PORTB,0 ; entrada T1
	sei	

	rjmp loop

DIR2:
	
	ldi pin40khz,0b00000010  ; saida T2
	
	; ativa int1
	ldi temp,0b00000010 
	out EIMSK,temp 
	
	ldi temp,0b00000000 ; reseta timer 0 e 1
	out TCNT0,temp		;|
	sts TCNT1L,temp     ; -->zerar o tempo									
	sts TCNT1H,temp		;|
	ldi time3,0b00000000
	
	ldi sum40, 0b00000000 ;zera contador de pulsos 
	
	out GTCCR,temp
	
	sbi PORTD,5 ; entrada T4 on
;	cbi PORTD,6 ; entrada T3
;	cbi PORTD,7 ; entrada T2
;	cbi PORTB,0 ; entrada T1 
	sei
	rjmp loop

DIR3:
	
	ldi pin40khz,0b00000100  ; saida T3
	
	; ativa int1
	ldi temp,0b00000010 
	out EIMSK,temp 

	ldi temp,0b00000000 ; reseta timer 0 e 1
	out TCNT0,temp		;|
	sts TCNT1L,temp     ; -->zerar o tempo									
	sts TCNT1H,temp		;|
	ldi time3,0b00000000

	out GTCCR,temp
;	cbi PORTD,5 ; entrada T4
;	cbi PORTD,6 ; entrada T3
;	cbi PORTD,7 ; entrada T2
	sbi PORTB,0 ; entrada T1 on
	sei
	rjmp loop

DIR4:

	ldi pin40khz,0b00001000  ; saida T4
	
	; ativa int1
	ldi temp,0b00000010 
	out EIMSK,temp 
	
	ldi temp,0b00000000 ; reseta timer 0 e 1
	out TCNT0,temp		;|
	sts TCNT1L,temp     ; -->zerar o tempo									
	sts TCNT1H,temp		;|
	ldi time3,0b00000000
	out GTCCR,temp


;	cbi PORTD,5 ; entrada T4
;	cbi PORTD,6 ; entrada T3
	sbi PORTD,7 ; entrada T2 on
;	cbi PORTB,0 ; entrada T1
	sei
	rjmp loop

;////////////////////////////////////////// LOOP //////////////////////////////////////////////////

loop:
	sei
	rjmp loop
	
;////////////////////////////////////////// 40kHz MAKE ////////////////////////////////////////////
TIM0_COMPA:
	cli

	cpi flag40khz,0b00000000 ; compara flag com 0 
	brne baixo ;se flag /= 0 vai para
	out PORTC,pin40khz
	ldi flag40khz,0b00000001 ; levanta flag 40khz
	sei
	rjmp loop
	
baixo:
	ldi flag40khz,0b00000000 ; zerra flag 40khz
	out PORTC,flag40khz
	sei
	;RET
	rjmp loop


;/////////////////////////////////////////////// TIMER EXTRA //////////////////////////

timer1_ovf:
	INC time3
	sei
	rjmp loop
	
;////////////////////////////////////////////// AQUISICAO DE DADOS ///////////////////////////

int1_calc:
	cli
	inc temp2
	cpi temp2, 0b00000111 
	BRMI loop ; se > 7
 
	
	ldi temp,0b10000011 ; pausar timer 0 e 1
	out GTCCR,temp
	
	lds time1,TCNT1L    ; guarda valores de tempo
	lds time2,TCNT1H 

	ldi temp,0b00000000 ;desativa int1
	out EIMSK,temp
	
	out PORTC,temp ;  seta 0 no pind2
	ldi flag40khz,0b00000000 ; zerra flag 40khz
	
	; zerra controles de direção
	cbi PORTD,5 ; entrada T1
	cbi PORTD,6 ; entrada T2
	cbi PORTD,7 ; entrada T3
	cbi PORTB,0 ; entrada T4

;////////////////////////////////////////////// TRANSMICAO DOS DADOS //////////////////////////////////////////////////////	

	ldi temp,0b00001000;TX on
	sts UCSR0B, temp
	sbi PORTD,2 ; configura max485 para enviar dados	
	sei

	rjmp TXdir

; comando de direcao para debug
TXdir:
	lds temp, UCSR0A 
	sbrs temp, UDRE0
	rjmp TXdir
    sts UDR0, dir
TXdirfim:
	lds temp, UCSR0A 
	sbrs temp,TXC0
	rjmp TXdirfim
	ldi temp,0b01100000;TX fim
	sts UCSR0A, temp
	
; tempo 
TXtime1:
	lds temp, UCSR0A 
	sbrs temp, UDRE0
	rjmp TXtime1
    sts UDR0, time1
TX1fim:
	lds temp, UCSR0A 
	sbrs temp,TXC0
	rjmp TX1fim
	ldi temp,0b01100000;TX fim
	sts UCSR0A, temp

TXtime2:
	lds temp, UCSR0A 
	sbrs temp, UDRE0
	rjmp TXtime2
    sts UDR0, time2
TX2fim:
	lds temp, UCSR0A 
	sbrs temp,TXC0
	rjmp TX2fim
	ldi temp,0b01100000;TX fim
	sts UCSR0A, temp

TXtime3:
	lds temp, UCSR0A 
	sbrs temp, UDRE0
	rjmp TXtime3
    sts UDR0, time3

	rjmp comfim
	
	
comfim: ; fim da comunicação

	ldi temp,0b00000000 ; reseta timer 0 e 1
	out TCNT0,temp		;|
	sts TCNT1L,temp     ; -->zerar o tempo									
	sts TCNT1H,temp		;|
	ldi time3,0b00000000


	lds temp, UCSR0A 
	sbrs temp,TXC0
	rjmp comfim
	ldi temp,0b01100000;TX fim
	sts UCSR0A, temp
	ldi temp,0b00010000; RX on
	sts UCSR0B, temp
	rjmp RX

