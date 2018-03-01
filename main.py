import sys
import output
import parser

# File name input
fileName = sys.argv[1]

infos, rides = parser.parse(fileName)

result = [
    [1,2],
    [3]
]

print(result[0])
# File name output 
fileName = (fileName.split('.'))[0] + '.out'

output.writeoutput(fileName, result)
