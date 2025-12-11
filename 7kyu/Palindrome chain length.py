def palindrome_chain_length(n):
    #reverse the original number
    def reverse(n):
        return str(n) == str(n)[::-1]

    step = 0

    while not reverse(n):
        num = int(str(n)[::-1])
        n += num
        step += 1
    return step

print(palindrome_chain_length(87))