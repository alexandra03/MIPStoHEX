MIPS to HEX
=========

MIPS to Hexadecimal Program Converter
by Alexandra Sunderland



	Takes an entire program in MIPS (reduced instruction set) and converts it
	to hexadecimal for use in the CS241 MIPS simulator.

	Written by Alexandra Sunderland

	Includes support for the following MIPS instructions:
	- .word   - SLT    - BNE
	- ADD     - SLTU   - JR
	- SUB     - BEQ    - LIS

	To be added: 
	- LW / SW

	
Example input 
=============
	Input:
	add $3, $2, $0
	beq $3, $0, 1
	add $2, $0, $0
	jr $31

	Output:
	.word 0x401820
	.word 0x10600001
	.word 0x1020
	.word 0x3e00008


Usage
=====
		python MIPStoHEX.py myMips.txt > myHex.hex    => To convert an entire file and redirect output
		python MIPStoHEX.py 						  => Enters command-line mode to convert
														 one line at a time
