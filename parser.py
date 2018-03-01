def parse(filename):
    file = open(filename, 'r')
    firstLine = file.readline()
    
    
    infoList = firstLine.split('\n')
    infoList = infoList[0].split(' ')
    infos = {
        'R': infoList[0],
        'C': infoList[1],
        'F': infoList[2],
        'N': infoList[3],
        'B': infoList[4],
        'T': infoList[5] 
    }

    rides = []

    for line in file:
        line = line.split('\n')
        line = line[0].split(' ')
        rides.append({
            'start': (line[0], line[1]),
            'finish': (line[2], line[3]),
            'earliest': line[4],
            'latest': line[5] 
        })

    return infos, rides