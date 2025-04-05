if __name__ == "__main__":
    a = [5,2,3]
    b= [1,2,1]
    cost_arrays = []
    for i in range(len(a)):
        cost_arrays.append(a[i] / b[i])
    sorted_cost_array = sorted(range(len(cost_arrays)), key = lambda k : cost_arrays[k], reverse = True)
    print(cost_arrays)
    print(sorted_cost_array)