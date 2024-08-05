def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        print(n)
        if n <= 1:
            return False
        if n == 2:
            return 'Простое'
        if n % 2 == 0:
            return 'Cоставное'
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return 'Cоставное'
            return 'Простое'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

