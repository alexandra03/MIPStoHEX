'''
	
	MIPS to Hex converter

	Takes an entire program in MIPS (reduced instruction set) and converts it
	to hexadecimal for use in the CS241 MIPS simulator.


	Written by Alexandra Sunderland
	January 13th 2014

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

'''
import sys

# Turns an integer into a binary string of the given length
# example: getBin(3,5)=00011
getBin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)


# Locates the nth occurence of subString and returns it's index in command
def findReg(command, subString, n):
    inst = command.find(subString)
    while inst>=0 and n>1:
        inst=command.find(subString, inst+len(subString))
        n-=1
    return inst


# Extracts the nth register number, without the dollar sign
def getRegNumber(command, n):
	if n==3 or command.find("jr")>-1 or command.find("lis")>-1:
		return command[findReg(command, "$", n)+1 :]
	else:
		return command[findReg(command, "$", n)+1: findReg(command, " ", n+1)-1]


# Turns the binary instruction into hex, and prints it to stdout
def binaryToHex(binaryString):
	HexCommand=hex(int(binaryString,2))
	print ".word "+ HexCommand


# Returns the register number in binary, with the appropriate number of 
# 0's in front to make the string 5 bits
def binR(register):
	return str(getBin(int(register),5))

# Main control. Extracts the command and the registers, creates the 
# binary instruction string and sends it off to be converted to hex
def mipsToBinary(mipsCommand):
	command=mipsCommand[:mipsCommand.find(" ")]

	if command==".word":
		r1=mipsCommand[mipsCommand.find(" ")+1:]
	else:
		r1=getRegNumber(mipsCommand, 1)

	if command!="jr" and command!="lis" and command!="lw" and command!="sw" and command!=".word":
		r2=getRegNumber(mipsCommand, 2)
		if command!="beq" and command!="bne":
			r3=getRegNumber(mipsCommand, 3)
		else:
			r3=mipsCommand[findReg(mipsCommand, ",", 2)+2:]

	if command=="jr":
		binaryString="0b000000"+str(getBin(int(r1),5))+"000000000000000001000"
	elif command=="add":
		binaryString="0b000000"+binR(r2)+binR(r3)+binR(r1)+"00000100000"
	elif command=="sub":
		binaryString="0b000000"+binR(r2)+binR(r3)+binR(r1)+"00000100010"
	elif command=="slt":
		binaryString="0b000000"+binR(r2)+binR(r3)+binR(r1)+"00000101010"
	elif command=="sltu":
		binaryString="0b000000"+binR(r2)+binR(r3)+binR(r1)+"00000101011"
	elif command=="lis":
		binaryString="0b0000000000000000"+binR(r1)+"00000010100"
	elif command=="beq":
		binaryString="0b000100"+binR(r1)+binR(r2)+str(getBin(int(r3),16))
	elif command=="bne":
		binaryString="0b000101"+binR(r1)+binR(r2)+str(getBin(int(r3),16))
	elif command==".word":
		binaryString=str(getBin(int(r1),32))

	binaryToHex(binaryString)


def main():
	f=open(sys.argv[1],'r') # Opens the file passed in as an argument
	for line in f:
		try:
			mipsToBinary(line)
		except:
			print "Error in line, could not convert"


if __name__=="__main__":
	main()
