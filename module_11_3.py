import unittest


def introspection_info(obj):
    introspect = dict()
    introspect['type'] = type(obj)
    list_attr = dir(obj)
    list_method = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    introspect['attributes'] = list_attr
    introspect['methods'] = list_method
    introspect['module'] = getattr(obj, '__module__', None)
    return introspect


class Figura:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        print(f"Стороны: {self.a}, {self.b} ")
        return f"Площадь: {self.a * self.b}"


S = Figura(5, 6)
print(introspection_info(S))
print(introspection_info(42))
