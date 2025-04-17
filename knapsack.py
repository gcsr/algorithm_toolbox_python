from sys import stdin


def maximum_gold(capacity, weights):
    len_weights = len(weights)
    array_capacity_weights = [[None]*(capacity + 1) for x in range(len_weights+ 1)]
    for i in range (len_weights + 1):
        array_capacity_weights [i][0] = 0

    for j in range(capacity + 1):
        array_capacity_weights[0][j] = 0

    # for row in array_capacity_weights:
    #    print(*row, sep="\t")

    for weight_looper in range(1, len_weights + 1):
        for capacity_looper in range(1, capacity + 1):
            array_capacity_weights [weight_looper][capacity_looper] = array_capacity_weights[weight_looper - 1][capacity_looper]
            if (weights[weight_looper - 1]) <= capacity_looper:
                value = array_capacity_weights[weight_looper - 1][capacity_looper - weights[weight_looper - 1]] + weights[weight_looper - 1]
                if value > array_capacity_weights [weight_looper][capacity_looper]:
                    array_capacity_weights[weight_looper][capacity_looper] = value

    for row in array_capacity_weights:
        print(*row, sep="\t")


    return array_capacity_weights[len_weights][capacity]
    # assert False


if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    # assert len(input_weights) == n

    print(maximum_gold(10, [2,8,4,6]))
    # print(maximum_gold(10,[1, 4, 8]))
