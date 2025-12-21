def comp(array1, array2):

    if array1 is None or array2 is None:
        return False
    
    square = [num**2 for num in array1]

    return sorted(square) == sorted(array2)

array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(array1, array2))