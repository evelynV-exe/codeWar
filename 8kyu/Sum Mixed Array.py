def sum_mix(arr):
    solution = 0
    newArr = list(map(int, arr))
    for num in newArr:
        solution += num
    return solution
