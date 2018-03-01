from distance import dist

def update_score(position, rides):
    scores = []
    i = 0
    for ride in rides:
        scores.append([ride['index'], dist(position, ride['start']), ride['dist']])
        i = i + 1
    
    scores.sort(key = lambda l:l[1])
    scores.sort(key = lambda l:l[2], reverse=True)

    return scores

def run(infos, rides):
    nb_cars = infos['F']
    results = {}
    for j in range(infos["F"]):
        results[j] = []
    i = 1
    timemax = infos['T']
    while nb_cars > 0:
        time = 0
        position = (0, 0)
        while time < timemax:
            scores = update_score(position, rides)
            if len(scores) == 0:
                break
            results[i].append(scores[0][0])
            time = time + scores[0][1] + scores[0][2]

            for ride in rides:
                if ride['index'] == scores[0][0]:
                    position = rides[rides.index(ride)]['finish']
                    rides.pop(rides.index(ride))
                    break
        nb_cars = nb_cars - 1
        i = i + 1
        if i >= len(rides):
            break
    #print(results)
    return results        
    