import sys
import output
import parser
import simpleAssignRide

# File name input
fileName = sys.argv[1]

infos, rides = parser.parse(fileName)

results = simpleAssignRide.assignRideV2(infos, rides)
# File name output
fileName = (fileName.split('.'))[0] + '.out'

output.writeoutput(fileName, results)
