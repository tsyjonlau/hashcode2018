
import sys
import output

# File name input
fileName = sys.argv[1]



result = [
    [1,2],
    [3]
]

print(result[0])
# File name output 
fileName = (fileName.split('.'))[0] + '.out'

output.writeoutput(fileName, result)