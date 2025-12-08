def high_and_low(numbers):
    numlist = [int(n) for n in numbers.split()]
    high = max(numlist)
    low = min(numlist)
    return f"{high} {low}"
