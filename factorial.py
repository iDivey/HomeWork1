def test(*args):
    print(args)


test('arguments', 2, 34, 656, 'кварги')


def factorial(n):
    if n == 1 or n == 0:
        return 1
    factorial_n_minus_one = factorial(n=n - 1)
    return n * factorial_n_minus_one


print(factorial(0))
