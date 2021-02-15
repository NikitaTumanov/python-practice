import math

def f14(n):
    if(n==0):
        return 5
    elif (n==1):
        return 7
    else:

        return (math.tan(f14(n - 1)) + f14(n - 1) / 98)

print(f'{f14(11):.2e}')
print(f'{f14(6):.2e}')
