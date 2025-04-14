from sys import stdin

def min_refills_sum(distance, tank, stops):
    # write your code here
    total_stops_distance = stops[0]
    if stops[0] > tank:
        return -1
    for i in range(1, len(stops)-1):
        total_stops_distance += stops[i] - stops[i-1]
        if stops[i] - stops[i-1] > tank:
            return -1
    if distance > total_stops_distance + tank:
        return -1
    return distance // tank

def min_refills(distance, tank, stops):
    # write your code here
    if stops[0] > tank:
        return -1
    if distance <= tank:
        return 0
    tank_left = tank - stops[0]
    distance_covered = stops[0]
    refills = 0
    # [200, 375, 550, 750]
    for i in range(0, len(stops)-1):
        if stops[i+1] - stops[i] > tank:
            return -1
        if stops[i+1] - stops[i] > tank_left:
            # print("filling at stop ", stops[i])
            refills += 1
            tank_left = tank
        tank_left -= stops[i+1] - stops[i]
        distance_covered += stops[i+1] - stops[i]
        if distance_covered >= distance:
            break
    if distance_covered < distance:
        if distance - distance_covered > tank:
            return -1
        elif tank_left < distance - distance_covered:
            # print("filling at end ", stops[len(stops) - 1])
            refills += 1
    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
    # print(min_refills(1250, 250, [200, 400, 600, 800, 1000]))
