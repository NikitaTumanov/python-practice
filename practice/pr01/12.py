import math

def f12(x):
    if x<23:
        return (x**8+46*x**4)
    elif 23<=x<66:
        return (x**4/2+x**3)
    elif 66<=x<153:
        return (math.tan(40*x**3)+x)
    elif 153<=x<249:
        return (abs(math.cos(x))-44*x**8-87)
    elif x>=249:
        return (86*x**3+x)

print(f'{f12(153):.2e}')
print(f'{f12(240):.2e}')