
def writeoutput(fileName, results):
    file = open(fileName, 'w')
    for vehicule, rides in results.items():
        file.write(str(len(rides)))
        file.write(" ")
        first = 0
        for ride in rides:
            if (first != 0):
                file.write(str(" "))
            file.write(str(ride))
            first = 1
        file.write("\n")
