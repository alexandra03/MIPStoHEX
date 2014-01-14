MIPStoHEX
=========

MIPS to Hexadecimal Program Converter
by Alexandra Sunderland


Takes an entire program in MIPS (reduced instruction set) and converts it to hexadecimal for use in the CS241 MIPS simulator (University of Waterloo)

	Includes support for the following MIPS instructions:
	- .word 
	- ADD 
	- SUB 
	- LIS 
	- SLT 
	- SLTU 
	- BEQ 
	- BNE 
	- JR  

	To be added: 
	- LW 
	- SW 
	
	Example input (commas and single spaces must be as shown, and one command per line): 
	add $3, $2, $0
	beq $3, $0, 1
	add $2, $0, $0
	jr $31

Usage:
Write MIPS program in a .txt file, and run "python MIPStoHEX.py myfile.txt > myHexFile.hex"
