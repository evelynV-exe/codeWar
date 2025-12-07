def sum_array(arr):
    if arr is None or arr == [] or len(arr) <= 2:
        return 0
    
    # remove the maximum number and lowest number
    arrCopy = arr.copy()
    arrCopy.remove(max(arr))
    arrCopy.remove(min(arr))

    solution = 0
    for num in arrCopy:
        solution += num
    
    return solution

print(sum_array([6, 2, 1, 8, 10]))