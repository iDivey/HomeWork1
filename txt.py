file_name = 'HW.txt'
file = open(file_name, mode='r')
file_content = file.read()
print(file_content)
file.close()
