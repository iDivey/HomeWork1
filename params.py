def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params("F - ftornik", b=25, c=[1,2,3])
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3]) - Работают, но с предупреждением о смене типа


values_list = [1, 'Hi', True]
values_dict = {'a': [1,2,3], 'b': 'Dream', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['By', 4.5]
print_params(*values_list_2, 42)


# def append_to_list(item, list_my=None):
#     if list_my is None:
#         list_my = []
#     list_my.append(item)
#     print(list_my)
#
#
# append_to_list(1)
