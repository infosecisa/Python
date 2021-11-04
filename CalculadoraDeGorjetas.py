# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:38:09 2021

@author: Belly
"""

print("Bem vindo à calculadora de gorjetas")
conta = input("Insira o valor da conta, por favor")
pessoas = input("Insira a quantidade de pessoas que pagarão a conta")
gorjeta = input("Insira a porcentagem de gorjeta que deseja dar: 10, 12, ou 15? ")
novaconta = float(conta)
novapessoas = int(pessoas)
novagorjeta = int(gorjeta)
gorjetaporcentagem = (novagorjeta / 100) + 1
calculogorjeta = novaconta * gorjetaporcentagem
divisaoconta = round((calculogorjeta / novapessoas), 2)
print(f"Cada pessoa irá pagar: {divisaoconta}")