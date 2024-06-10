list1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def is_odd(x):
    return x % 2


list2 = filter(is_odd, list1)


def x2(x):
    return x ** 2


list3 = map(x2, list(list2))


print(list(list3))