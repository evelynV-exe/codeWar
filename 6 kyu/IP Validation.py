def is_valid_IP(strng):
    
    if strng == '':
        return False
    
    number = strng.split(".")
    
    if len(number) != 4:
        return False

    for num in number:
        
        if not num.isdigit():
            return False
        
        integer = int(num)
        
        if integer < 0 or integer > 255:
            return False

        if str(num) != str(integer):
            return False
    return True
