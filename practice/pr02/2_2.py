def f22(x):
    d = x & 0x80000000
    c = x & 0x7f800000
    b = x & 0x007fff00
    a = x & 0x000000ff
    a = a << 23
    b = b >> 8
    c = c >> 8
    x = a+b+c+d
    return x
"""
print(f'{f22(0xf6c7a9f3):#x}')
print(f'{f22(0x48714833):#x}')
"""