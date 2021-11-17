# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 21:56:10 2021

@author: Belly
"""

peso = float(input("Insira o seu peso"))
altura = float(input("Insira a sua altura"))
calculoimc = (peso / (altura * altura))
print(calculoimc)

if calculoimc < 18.5:
    print("Você está abaixo do peso")
elif 24.9 >= calculoimc >= 18.5 : 
    print("Seu peso está normal")
elif  29.9 >= calculoimc >= 25:
    print("Você está com sobrepeso")
elif 34.9 >= calculoimc >= 30:
    print("Você está com obesidade grau I")
elif 39.9 >= calculoimc >= 35:
    print("Você está com obesidade grau II")
else:
    print("Você está com obesidade grau III ou mórbida")