import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for n, line in enumerate(file, 1):
            line = line.rstrip()
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start1 = datetime.now()
read_info('./file 1.txt')
read_info('./file 2.txt')
read_info('./file 3.txt')
read_info('./file 4.txt')
end1 = datetime.now()

start2 = datetime.now()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
end2 = datetime.now()

print(f'Линенйный вызов закончил за: {end1 - start1}')
print(f'Многопроцессорный вызов закончил за: {end2 - start2}')


