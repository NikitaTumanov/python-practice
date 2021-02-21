def fast_pow(n, m, res=1):
    while m > 0:
        if m == 1:
            return res * n
        if m % 2 == 1:
            res *= n
        n *= n
        m //= 2
    return res

def test_fast_pow():
    for i in range(101):
        for j in range(101):
            if (fast_pow(i, j) != i ** j):
                print("Тест не пройден")
                return
    print("Тест пройден")

test_fast_pow()