# -*- coding: utf-8 -*-

'''
    Условия
'''

#if..else
num = int(input('Склоько раз вы были в Эрмитаже? '))
if num > 0:
    print('Отлично!')
    print('Надеюсь, что тебе понравился музей!')
else:
    print('Тебе обязательно нужно его посетить!')

#if..elif..else
course = int(input('На каком курсе ты учишься? '))
if course == 1:
    print('У тебя всё только начинается!')
elif course == 2:
    print('Ты уже знаешь много вещей!')
elif course == 3:
    print('Базовый курс окончен! Пора приступить к профессиональным дисциплинам!')
else:
    print('Не забудь, что в июне тебе нужно защищать диплом!')

x = 5
y = 12
if y % x > 0 :
    print('%d не является делителем числа %d' % (y,x))

z=3
x = '{} является делителем числа {}'.format(z,y) if y % z == 0 else '{} не является делителем числа {}'.format(z,y)
print(x,'\n\n')

#Самостоятельная работа

#Задание 2
p = int(input('Сколько лабораторных работ вы сдали за год?'))
if (p > 10) : print(p)
if (p > 10) :
    print(p)
print(p) if (p > 10) else 0

#Задание 3
a = 453321
b = 12342
if (a > b): print(a % b)
print(b % a) if (b > a) else 0
if (a == b):
    print(a*b)






