
def writeoutput(fileName, result):
    file = open(fileName, 'w')
    count = 1
    for res in result:
        file.write(str(count))
        file.write(" ")
        for r in res:
            file.write(str(r))
            file.write(str(" "))
        file.write("\n")
        count = count + 1