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
    for j in range(1, infos["F"] + 1):
        results[j] = []

    i = 1
    timemax = infos['T']
    cars_indices = [0] * len(rides)

    while nb_cars > 0:
        time = 0
        position = (0, 0)
        

        while time < timemax:
            scores = update_score(position, rides)
            if len(scores) == 0:
                break

            found = False
            for score in scores:
                if cars_indices[score[0]] == 0 and time + score[2] <= rides[score[0]]['latest'] and time + score[2] <= timemax:
                    results[i].append(score[0])
                    time = time + score[1] + score[2]
                    position = rides[score[0]]['finish']
                    cars_indices[score[0]] = 1
                    found = True
                
            
            if found == False:
                break            

        nb_cars = nb_cars - 1
        i = i + 1
        if i > len(rides):
            break
    #print(results)
    return results        
    