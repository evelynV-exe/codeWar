def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    
    solution = [0, 0]
    
    for num in arr:
        if num < 0:
            solution[1] += num
        elif num > 0:
            solution[0] += 1
    return solution
