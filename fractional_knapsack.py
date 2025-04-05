from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    cost_arrays = []
    for i in range(len(weights)):
        cost_arrays.append(values[i] / weights[i])

    # print (cost_arrays)
    sorted_cost_array = sorted(range(len(cost_arrays)), key = lambda k : cost_arrays[k], reverse = True)
    # print(sorted_cost_array)
    optimal_sum = 0
    index = 0
    remaining_capacity = capacity
    while remaining_capacity > 0 and index < len(sorted_cost_array):
        if remaining_capacity >= weights[sorted_cost_array[index]]:
            optimal_sum = optimal_sum + weights[sorted_cost_array[index]] * cost_arrays[sorted_cost_array[index]];
            remaining_capacity -= weights[sorted_cost_array[index]]
        else:
            optimal_sum = optimal_sum + remaining_capacity * cost_arrays[sorted_cost_array[index]]
            remaining_capacity = 0

        # print(optimal_sum)
        index += 1
    return optimal_sum


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    # opt_value = optimal_value(8, [2,3,5], [200,50,90])
    print("{:.10f}".format(opt_value))
