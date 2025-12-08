def positive_sum(arr):
    if arr == []:
        return 0
    
    solution = 0
    
    for num in arr:
        if num > 0:
            solution += num
    return solution
        
print(positive_sum([-1,-2,-3,-4,-5]))
