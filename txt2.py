file_name = 'HW.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line, end='')

# от простого использования file.close() оператор with open (...) отличается тем, что в последнем первый срабатывает в любом случае, автоматически, без его указания
