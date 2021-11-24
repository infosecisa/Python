# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:35:05 2021

@author: Belly
"""

import random
conta = ""
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letras= int(input("Quantas letras você deseja na sua senha?\n"))
nr_simbolos = int(input("Quantos símbolos você deseja na sua senha?\n"))
nr_numeros = int(input("Quantos números você deseja na sua senha?\n"))

for letra in letras:
    if nr_letras != 0:
        conta = conta + letra
        nr_letras = nr_letras - 1



    for simbolo in simbolos:
        if nr_simbolos != 0:
            conta = conta + simbolo
            nr_simbolos = nr_simbolos - 1



        for numero in numeros:
            if nr_numeros != 0:
                conta = conta + numero
                nr_numeros = nr_numeros - 1
print(conta)
