# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:30:54 2021

@author: Belly
"""

idade = input("Qual a sua idade? ")
calculoidade = 90 - int(idade)
dias = 365 * calculoidade
semanas = 52 * calculoidade
meses = 12 * calculoidade
print(f"Você tem {dias} dias, {semanas} semanas e {meses} meses restantes de vida")