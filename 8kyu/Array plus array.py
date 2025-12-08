import numpy

def array_plus_array(arr1,arr2):
    solution = 0
    addedArr = numpy.add(arr1, arr2)
    for num in addedArr:
        solution += num
    return solution
