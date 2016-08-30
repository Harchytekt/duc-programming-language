#!/usr/bin/python
# -*- coding: utf-8 -*-


from math import *


def fibo(n):
	""" Donne la valeur du nème élément de la suite de Fibonacci. """
	if n == 0:
		return n
	elif n == 1 or n == 2:
		return 1
	return fibo(n - 1) + fibo(n - 2)


def fibo2(n):
	""" Donne la valeur du nème élément de la suite de Fibonacci
	en utilisant le nombre d'or: (1 + sqrt(5)) / 2.0. """
	x = 1. / sqrt(5)
	y = sqrt(5)
	return int((x * ((1 + y) / 2.) ** n) - (x * ((1 - y) / 2.) ** n))


def give_fibo(m):
	""" Donne les n premiers éléments de la suite de Fibonacci. """
	a = 1
	while a < m:
		print fibo(a)
		a += 1


if __name__ == '__main__':
	print fibo(10)
	print fibo2(10)