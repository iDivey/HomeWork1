class InvalidDataException (TypeError):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class ProcessingException(KeyError):
    def __init__(self, message):
        self.message = message


def f(a, b):
    if type(a) != type(b):
        raise InvalidDataException('Конфликт типов', {'a': a, 'b': b})
    print(a + b)


try:
    f(1, 'asfddfg')
except InvalidDataException as e:
    print(f'Что пошло не так: {e.message}, проверь: {e.extra_info}')


dict_ = {'День рождения': 15, 'Месяц рождения': 8, 'Год рождения': 1997}


def f1(a):
    if dict_.get(a) is None:
        raise ProcessingException(f'Ключа "{a}" не cуществует в словаре')
    print(dict_[a])


f1('День рождения')
try:
    f1('Город рождения')
except ProcessingException as e1:
    print(f'Ошибка в процессе выполнения: {e1.message}')
    raise
