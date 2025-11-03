def is_strictly_increasing_digits(n):
    if type(n) != int or n < 0:
        return -1
    if n < 10:
        return True
    last_digit=10
    while n>0:
        current_digit=n%10
        n=n//10
        if current_digit>=last_digit:
            return False
        last_digit=current_digit
    return True    
