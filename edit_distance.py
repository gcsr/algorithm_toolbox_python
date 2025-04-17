def min (a, b, c):
    print(a, b, c)
    first_max = a if (a < b) else b
    return first_max if first_max < c else c

def edit_distance(first_string, second_string):
    first_string_len = len(first_string)
    second_string_len = len(second_string)
    string_matrix_array = [[None]*second_string_len for x in range(first_string_len)]
    for i in range (second_string_len):
        string_matrix_array [0][i] = i

    for j in range(first_string_len):
        string_matrix_array[j][0] = j

    for j in range(1, second_string_len):
        for i in range(1, first_string_len):
            insertion = string_matrix_array [i][j - 1] + 1
            deletion = string_matrix_array[i - 1][j] + 1
            match = string_matrix_array [i - 1][j -1]
            mismatch = string_matrix_array [i - 1][j -1] + 1
            if first_string[i] == second_string[j]:
                string_matrix_array[i][j] = min(insertion, deletion, match)
            else:
                string_matrix_array[i][j] = min(insertion, deletion, mismatch)
    # print(string_matrix_array)
    return string_matrix_array [first_string_len - 1][second_string_len - 1]


if __name__ == "__main__":
    #print(min(31,32,3))
    print(edit_distance(list("0" + input()), list("0" + input())))
    #print(edit_distance(input(), input()))
