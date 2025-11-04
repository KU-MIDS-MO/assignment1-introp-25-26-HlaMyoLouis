def sum_of_cubes_even(n):
    if n<0 or not isinstance(n, int):
        return -1
    if n>2000:
        print("warning")
    total=0
    i=0
    while i<=n:
        total = total + i**3
        i= i+2
    return float(total)