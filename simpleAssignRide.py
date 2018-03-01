
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