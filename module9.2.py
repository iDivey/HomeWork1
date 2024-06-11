# 1. Фабрика функций
def operations(o):
    if o == "сложи":
        def plus(x, y):
            return f"Сложил, получилось: {x + y}"

        return plus
    elif o == "сотая степень":
        def nxx100(n):
            return f"n в сотой степени: {n ** 100}"

        return nxx100
    elif o == "путь самурая":
        def hs(x):
            return f"У самурая нет цели, есть только путь в {x} шагов"

        return hs


plus = operations("сложи")
x_100 = operations("сотая степень")
samurai = operations("путь самурая")

print(plus(99, 201))
print(x_100(2))
print(samurai(300000))

# 2. Лямбда-Функции
degree = lambda x, n: x ** n
print(degree(11, 2))


def degree_func(x, y):
    return x ** y


print(degree_func(11, 2))


# 3. Вызываемые Объекты
class Pryamougjlnik:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        print(f"Стороны: {self.a}, {self.b} ")
        return f"Площадь: {self.a * self.b}"


S = Pryamougjlnik(4, 6)
print(S())
