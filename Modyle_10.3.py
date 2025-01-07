import threading
from time import sleep
from threading import Lock
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self, *args, **kwargs):
        for i in range(100):
            amount = randint(50, 500)
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}')

        if self.balance >= 500 and self.lock.locked():
            self.lock.release()

        sleep(0.001)

    def take(self, *args, **kwargs):
        for i in range(100):
            amount = randint(50, 500)
            print(f"Запрос на {amount}")

            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=bk.deposit, args=(bk,))
th2 = threading.Thread(target=bk.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')