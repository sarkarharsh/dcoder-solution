"""
I don't know what is wrong
One of the cases is incorrect
I am not able to correct it
If anyone is able to correct it, please refer it to me
"""

# taking inputs
testCases = int( input() )
listDecimals = []

for i in range( testCases ):
	listDecimals.append( float( input() ) )

# rounding and printing
for i in listDecimals:
	print( round( i, 2 ) )
