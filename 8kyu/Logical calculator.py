def logical_calc(array, op):
    if op == 'AND':
        result = True
        for v in array:
            result = result and v
        return result
    elif op == "OR":
        result  = False
        for v in array:
            result = result or v
        return result
    elif op == "XOR":
        result = False
        for v in array:
            result = result ^ v
        return result
        
