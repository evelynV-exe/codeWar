def square_digits(num):
    string = str(num)
    result = ''
    for digit in string:
        result += str(int(digit) ** 2)
    return int(result)
