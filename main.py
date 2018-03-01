import sys
import parser

# File name input
fileName = sys.argv[1]

parser.parse(fileName)

# File name output 
fileName = (fileName.split('.'))[0] + '.out'
