def count_digits_greater_than(n, t):
    if n < 0 or t < 0 or t > 9 or int(n) != n or int(t) != t:
        return -1

    n = int(n)
    t = int(t)
    count = 0

    while n > 0:
        digit = n % 10
        if digit > t:
            count = count + 1
        n = (n - digit) // 10

    return count