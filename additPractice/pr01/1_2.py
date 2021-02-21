def fast_pow(x, y, res=1):
    while y > 0:
        if y == 1:
            return res * x
        if y % 2 == 1:
            res *= x
        x *= x
        y //= 2
    return res

def test_fast_pow():
    for i in range(101):
        for j in range(101):
            if (fast_pow(i, j) != i ** j):
                print("Тест не пройден")
                return
    print("Тест пройден")

test_fast_pow()