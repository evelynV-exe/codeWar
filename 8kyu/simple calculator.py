def calculator(x, y, op):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "unknown value"
    
    solution = 0
    if op == "+":
        solution = x+y
    elif op == "-":
        solution = x-y
    elif op == "*":
        solution = x*y
    elif op == "/":
        solution = x/y
    else:
        solution = "unknown value"
    return solution
