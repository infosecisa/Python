# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:50:06 2021

@author: Belly
"""

print('''
      
            /;
           / |'-,.
          /  '    `"---,.__
         /  '    ,'     ,  '"--,"|
        /  '    ,     ,'     ,"::|
       /  '   ,'    ,      ,"::::|
      /  '   ,    ,'     ,"::::::L
     /  '  ,'   ,'     ,"::::::::L
    /  '  ,    ,     ,":::::::::J
    k-,._    ,'   _.":::::::::::J
     \.  `"----'"".J::::::::::::|
      \.    .-,    .L:::::::::::|
       \.  (       .J:::::::::::!
        \.  `--     .L:::::::::/
         \.   .-.   .|::::::::/
          \. (   )  .J:::::::/
           \. `-'    .L:::::/
            \.  L    .|::::/
             \. !__  .J:::/
              \.  __  .L:/
               \. L_) .|/
                `-,__,-' 
          ''')
print("Bem vindo à Livraria dos Humores!")
escolha = input("Escolha o seu humor de hoje que eu te indicarei um livro: Medo, Tristeza, Alegria, Nojo ou Raiva?")
if escolha == "Medo":
    print("O livro ideal para o seu humor é: Em busca de sentido - Viktor Frankl")
elif escolha == "Tristeza":
    print("O livro ideal para o seu humor é: Meu ano de descanso e relaxamento - Ottessa Moshfegh")
elif escolha == "Alegria":
    print("O livro ideal para o seu humor é: Em Outra Vida, Talvez? - Taylor Jenkins Reid ")
elif escolha == "Nojo":
    print("O livro ideal para o seu humor é: Holocausto Brasileiro - Daniela Arbex")
elif escolha == "Raiva":
    print("O livro ideal para o seu humor é: Sobre A Ira / Sobre A Tranquilidade Da Alma - Sêneca")
else:
    print("Você desbloqueou o livro bônus: A morte é um dia que vale a pena viver - Ana Claudia Quintana Arantes")
