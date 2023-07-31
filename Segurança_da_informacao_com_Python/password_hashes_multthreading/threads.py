""" Working with threads """

from threading import Thread
from time import sleep


def car(speed, pilot):
    path = 0
    while path <= 100:
        path += speed
        sleep(0.2)
        print(f'Pilot: {pilot} km {path}')


t_car_one = Thread(target=car, args=[20, 'A.Senna'])
t_car_two = Thread(target=car, args=[10, 'Prost'])

t_car_one.start()
t_car_two.start()
