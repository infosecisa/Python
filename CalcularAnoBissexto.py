# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:30:56 2021

@author: Belly
"""

ano = int(input("Insira um ano"))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano é bissexto")
        else:
            print("O ano não é bissexto")
    else:
        print("O ano é bissexto")
else:
    print("O ano não é bissexto")