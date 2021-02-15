def f13(n, m):
    a=0
    b=0
    for i in range(1,n+1):
        for j in range(1,m+1):
           a+=(j**5+i**8)
           b+=(62*i**6+j**3)

    return (a-(b/55))

print(f'{f13(26, 19):.2e}')
print(f'{f13(82, 98):.2e}')