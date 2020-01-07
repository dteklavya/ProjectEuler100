#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Multiples of 3 and 5
   
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer:
	233168

"""


def sum_multiples_of(number, target):
    last = target // number
    return number * (last * (last + 1)) // 2


def sum_of_multiples_of_three_and_five(number): 
    return sum_multiples_of(3, number-1) + sum_multiples_of(5, number-1) \
            - sum_multiples_of(15, number-1)


assert(sum_of_multiples_of_three_and_five(1000) == 233168)

