import sys
"""
This script counts lines in standard input
Input: text from the system
"""
count = 0

for line in sys.stdin:
	count +=1

print(count, 'lines in standard input')
