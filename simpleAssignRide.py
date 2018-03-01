
import distance

def simpleAssignRide(infos, rides):
    vehicule = 1
    rideIndex = 0
    results = {}
    i = 0
    for i in range(infos["F"]):
        results[i+1] = []
    for ride in rides:
        results[vehicule].append(rideIndex)
        if (vehicule == infos["F"]):
            vehicule = 1
        else:
            vehicule = vehicule + 1
        rideIndex = rideIndex + 1
    return results

def isAssignable(vehicule, ride):
    dist = 0
    if vehicule['currentStep'] < ride['earliest']:
        dist = ride['earliest'] - vehicule['currentStep']
    ride_dist = distance.dist(ride['start'], ride['finish'])
    to_ride_dist = distance.dist(ride['start'], vehicule['currentPos'])
    dist = dist + ride_dist + to_ride_dist + vehicule['currentStep']
    if dist < ride['latest']:
        return dist
    return -1

def assignRideV2(infos, rides):
    vehicules = {}
    rideIndex = 0
    results = {}
    i = 0
    for i in range(infos["F"]):
        results[i+1] = []
        vehicules[i+1] = {
            'currentPos': (0, 0),
            'currentStep': 0
        }
    for ride in rides:
        for key, vehicule in vehicules.items():
            dist = isAssignable(vehicule, ride)
            if dist != -1:
                vehicule['currentStep'] = dist
                vehicule['currentPos'] = ride['finish']
                results[key].append(rideIndex)
                break
        rideIndex = rideIndex + 1
    return results

#def isProfitable(ride_dist, total_ride_dist):
