def fast_mul(n, m, result=0):
    if (n == 0 or m == 0):
        return 0
    if (n == 1):
        return result + m
    if (m == 1):
        return result + n
    if (n % 2 == 1):
        result += m
    return fast_mul(n // 2, m * 2, result)

def test_fast_mul():
    for i in range(101):
        for j in range(101):
            if (fast_mul(i, j) != i * j):
                print("Тест не пройден")
                return
    print("Тест пройден")

test_fast_mul()