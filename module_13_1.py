import asyncio


async def start_strongman(name, power):
    if power > 10:
        print('Слишком тяжелые шары')
    else:
        print(f'Cилач {name} начал соревнования.')
        num = 1
        for i in range(5):
            await asyncio.sleep(10 - power)
            print(f'Cилач {name} поднял {num} шар.')
            num += 1
        print(f'Cилач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Vasya', 5))
    task2 = asyncio.create_task(start_strongman('Kolya', 3))
    task3 = asyncio.create_task(start_strongman('Shwartz', 8))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
