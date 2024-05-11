# добавить обработку ValueError
def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f"Error: {s} нельзя преобразовать в целое число"


# добавить обработку FileNotFoundError, IOError
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: данный файл не был обнаружен"
    except IOError:
        return "Ошибка ввода/вывода"
    finally:
        file.close()


# добавить обработку ZeroDivisionError, TypeError
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Деление на ноль невозможно"
    except TypeError:
        return f"Аргументы {a} и {b} должны являться числами"


# добавить обработку IndexError, TypeError
def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Индекс {index} за грианицами списка"
    except TypeError:
        return f"{index} должен являтся целым числом"
