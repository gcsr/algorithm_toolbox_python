def evaluate(a, op, b):
    # print(a, op, b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def isOp(char):
    if char == '+' or char == '-' or char == '*':
        return True
def min_and_max_calc(i, j, op_array, min_int_op_array, max_int_op_array):
    # print ('min_and_max_calc', i, j)
    minimum = 9223372036854775807
    maximum = -9223372036854775808
    for k in range(i, j):
        a = evaluate(max_int_op_array[i][k], op_array[k], max_int_op_array[k + 1][j])
        b = evaluate(max_int_op_array[i][k], op_array[k], min_int_op_array[k + 1][j])
        c = evaluate(min_int_op_array[i][k], op_array[k], max_int_op_array[k + 1][j])
        d = evaluate(min_int_op_array[i][k], op_array[k], min_int_op_array[k + 1][j])
        minimum, maximum = min([minimum, a, b, c, d]),max([maximum, a, b, c, d])

    # print('min_and_max_calc', minimum, maximum)
    return minimum, maximum
def maximum_value(dataset):
    dataset_char_array = list(dataset)
    int_array = []
    op_array = []
    appender = ''
    for char in dataset_char_array:
        if isOp(char):
            int_array.append(int(appender))
            appender = ''
            op_array.append(char)
        else:
            appender += char
    int_array.append(int(appender))
    len_int_array = len(int_array)
    # print(int_array)
    min_int_op_array = [[None] * len_int_array for x in range(len_int_array)]
    max_int_op_array = [[None] * len_int_array for x in range(len_int_array)]

    for i in range(len_int_array):
        min_int_op_array[i][i] = int_array[i]
        max_int_op_array[i][i] = int_array[i]

    '''for row in min_int_op_array:
        print(*row, sep="\t")
    for row in max_int_op_array:
        print(*row, sep="\t")'''

    for s in range(1,len_int_array):
        for i in range(0, len_int_array - s):
            j = i + s
            min_int_op_array[i][j], max_int_op_array[i][j] = min_and_max_calc(i, j, op_array, min_int_op_array, max_int_op_array)
            '''for row in min_int_op_array:
                print(*row, sep="\t")
            for row in max_int_op_array:
                print(*row, sep="\t")
    for row in min_int_op_array:
        print(*row, sep="\t")
    for row in max_int_op_array:
        print(*row, sep="\t")'''
    return max_int_op_array[0][len_int_array-1]

if __name__ == "__main__":
    print(maximum_value(input()))

