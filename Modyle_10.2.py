import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f"{self.name}, на нас напали!")
        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            if enemies > 0:
                print(f"{self.name}, сражается {days} день(дня)..., осталось {enemies} воинов.")
            else:
                print(f"{self.name} одержал победу спустя {days} день(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")