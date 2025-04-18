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
            print("filling at stop ", stops[i])
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
            print("filling at end ", stops[len(stops)-1])
            refills += 1
    return refills

if __name__ == "__main__":
    '''a = [5,2,3]
    b= [1,2,1]
    cost_arrays = []
    for i in range(len(a)):
        cost_arrays.append(a[i] / b[i])
    sorted_cost_array = sorted(range(len(cost_arrays)), key = lambda k : cost_arrays[k], reverse = True)
    print(cost_arrays)
    print(sorted_cost_array)'''
    # print(min_refills(1000, 200, [200, 400, 800, 900]))
    print(sorted([[1, 2],[1, 3], [2,4], [2,3]]))