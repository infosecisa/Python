# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 21:41:47 2021

@author: Belly
"""

numero = int(input("Digite um número"))
checagem = numero % 2

if checagem == 0:
    print('O número digitado é um número par')
else:
    print('O número digitado não é um número par')