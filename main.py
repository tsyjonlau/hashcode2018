import sys
import parser

# File name input
fileName = sys.argv[1]

infos, rides = parser.parse(fileName)

# File name output 
fileName = (fileName.split('.'))[0] + '.out'
