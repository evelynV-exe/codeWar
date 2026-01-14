def incrementer(nums):
    arr = []

    for i in range(len(nums)):
        nums[i] = nums[i] + i + 1

        if nums[i] >= 10:
            nums[i] = nums[i] % 10
            
        arr.append(nums[i])
    
    return arr

num = [4, 6, 9, 1 ,3]
incrementer(num)