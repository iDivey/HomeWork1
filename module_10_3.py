from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    lock = Lock()
    balance = 0

    def deposit(self):
        i = 0
        while i != 100:
            plus = randint(50, 500)
            self.balance += plus
            print(f'Пополнение: {plus}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            i += 1
            sleep(0.001)

    def take(self):
        i = 0
        while i != 100:
            minus = randint(50, 500)
            print(f'Запрос на {minus}')
            if minus <= self.balance:
                self.balance = self.balance - minus
                print(f'Снятие: {minus}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            i += 1
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
