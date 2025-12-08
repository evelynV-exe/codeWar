def high_and_low(numbers):
    numlist = [int(n) for n in numbers.split()]
    high = max(numlist)
    low = min(numlist)
    return f"{high} {low}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))