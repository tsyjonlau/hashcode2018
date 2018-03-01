from distance import dist

def parse(filename):
    file = open(filename, 'r')
    firstLine = file.readline()
    
    
    infoList = firstLine.split('\n')
    infoList = infoList[0].split(' ')
    infos = {
        'R': int(infoList[0]),
        'C': int(infoList[1]),
        'F': int(infoList[2]),
        'N': int(infoList[3]),
        'B': int(infoList[4]),
        'T': int(infoList[5]) 
    }

    rides = []

    for line in file:
        line = line.split('\n')
        line = line[0].split(' ')
        rides.append({
            'start': (int(line[0]), int(line[1])),
            'finish': (int(line[2]), int(line[3])),
            'dist': dist((int(line[0]), int(line[1])), (int(line[2]), int(line[3]))),
            'earliest': int(line[4]),
            'latest': int(line[5]) 
        })

    return infos, rides