# -*- coding: utf-8 -*-

class Geometric:

    def calculateArea(self):
        print('Calculating area')


class Square(Geometric):

    def __init__(self, a):
        self.side = a

    def _perimetr(self):
        print('Perimetr of Square {} : {}\n'.format(self.side, self.side * 4))

    def calculateArea(self):
        print('Area of Square {} : {}\n'.format(self.side, pow(self.side, 2)))


geom = Geometric()
geom.calculateArea()
sq = Square(5)
sq.calculateArea()
sq._perimetr()

print('Check subclass : ', issubclass(Square, Geometric))
print('Check instance sq->Square : ', isinstance(sq, Square))
print('Check instance sq->Geometric : ', isinstance(sq, Geometric))
print('Check instance sq->dict : ', isinstance(sq, dict))

'''
    Самостотельная работа
'''

# Задание 11
import math


class Circle(Geometric):

    def __init__(self, radius):
        self.__radius = radius

    def calculateArea(self):
        print('Площадь круга {} = {} '.format(self.__radius, (math.pi * pow(self.__radius, 2))))


circ = Circle(5)
circ.calculateArea()
