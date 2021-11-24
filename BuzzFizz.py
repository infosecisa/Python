# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:24:26 2021

@author: Belly
"""

for conta in range(1,101):
    if conta % 3 == 0:
        print("Fizz")
    elif conta % 5 == 0:
        print("Buzz")
    elif conta % 3 == 0 and conta % 5 == 0:
        print("FizzBuzz")
    else:
        print(conta)