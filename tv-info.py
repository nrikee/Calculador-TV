# coding=utf-8

from cmath import sqrt

__author__ = 'nRikee'

# 1 pulgada son 2.54 cm
toCm = 2.54

inches = input ( 'De cuántas pulgadas es la TV?\n' )
cm = inches * toCm

# Asumimos que la TV es de 16/9
b = sqrt ( cm ** 2 / 4.1604 )
a = 1.7777 * b
print 'Medidas:', '\n\t%.2fcm' % a.real, '\n\t%.2fcm' % b.real
print 'Distancia visionado:\n\t', str ( inches / 10 * 50 ) + 'cm'
