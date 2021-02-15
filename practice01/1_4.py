import math

def func(n):
    if(n==0):
        return 5
    elif (n==1):
        return 7
    else:

        return (math.tan(func(n-1))+func(n-1)/98)

print(f'{func(11):.2e}')
print(f'{func(6):.2e}')
