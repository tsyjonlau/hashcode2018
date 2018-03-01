
def writeoutput(fileName, results):
    file = open(fileName, 'w')
    for vehicule, rides in results.items():
        file.write(str(vehicule))
        file.write(" ")
        for ride in rides:
            file.write(str(ride))
            file.write(str(" "))
        file.write("\n")
