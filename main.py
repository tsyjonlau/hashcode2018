import sys
import output
import parser
from simpleAssignRide import *
from assign_by_score_c import run

# File name input
fileName = "a_example.in"
infos, rides = parser.parse(fileName)
results = assignRideV2(infos, rides)
fileName = (fileName.split('.'))[0] + '.out'
output.writeoutput(fileName, results)


fileName = "b_should_be_easy.in"
infos, rides = parser.parse(fileName)
results = assignRideV2(infos, rides)
fileName = (fileName.split('.'))[0] + '.out'
output.writeoutput(fileName, results)


fileName = "c_no_hurry.in"
infos, rides = parser.parse(fileName)
results = run(infos, rides)
fileName = (fileName.split('.'))[0] + '.out'
output.writeoutput(fileName, results)


fileName = "d_metropolis.in"
infos, rides = parser.parse(fileName)
results = assignRideV2(infos, rides)
fileName = (fileName.split('.'))[0] + '.out'
output.writeoutput(fileName, results)


fileName = "e_high_bonus.in"
infos, rides = parser.parse(fileName)
results = assignRideV2(infos, rides)
fileName = (fileName.split('.'))[0] + '.out'
output.writeoutput(fileName, results)


# File name output
