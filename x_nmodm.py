def fun(x,n,m):
    s=bin(n)
    c=1
    for i in s[2:]:
        if i=='0':
            c=(c**2)%m
        if i=='1':
            c= (c**2*x)%m
    return c
print(fun(2,43,71))

