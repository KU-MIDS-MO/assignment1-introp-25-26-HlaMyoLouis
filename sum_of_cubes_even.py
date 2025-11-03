def sum_of_cubes_even(n):
    if n<0:
        return -1
    if n>2000:
        print("warning")
    total=0
    i=0
    while i<=n:
        if i%2 == 0:
            total = total + i**3
            i= i+1
    return float(total)
        