def basethree(n):
    sign = '-' if n<0 else ''
    r= abs(n)
    if n < 3:
        return str(n)
    s = ''
    while n != 0:
        s = str(n%3) + s
        n = n//3
    return sign+s
n=int(input())
print(basethree(n))
