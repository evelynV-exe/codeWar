def hex_hash(input):
    result = 0
    if input == '':
        return 0

    for ch in input:
        value = hex(ord(ch))[2:]

        for digit in value:
            if digit.isdigit():
                result += int(digit, 16)
    return result

input = 'kcxnjsklsHskjHDkl7878hHJk'
print(hex_hash(input))