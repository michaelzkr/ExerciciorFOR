# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ogA-RvUzXcUvsvjU7zWuiGDPv5My6bes
"""

# Faça um programa que leia 5 números e informe o maior número.
numero_maior = 0
for i in range(5):
  numero = int(input("Digite um número"))
  if numero > numero_maior:
   numero_maior = numero
   print(numero_maior)

#Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzam resto igual a 2.]

for i in range(1000, 2001):
 if i % 11 == 2:
  print(i)

# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for moedas in range(5):
  numero = float(input(f"digite o {moedas+1}º número "))
  soma += numero
  media = soma/5

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")

#Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
numero = int(input("Digite um número para calcular a tabuada:"))
print(f"Tabuada do {numero}")
for i in range(1, 11):
  resultado = numero * i
  print(resultado)

for i in range(1, 11):
    print(f"Tabuada do {i}:")
    for moedas in range(1, 11):
        resultado = i * moedas
        print(f"{i} + {moedas} = {resultado}")

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
for i in range(1, 21):
  print(i)
#Depois modifique o programa para que ele mostre os números um ao lado do outro.
for i in range(1, 21):
  print(i,end = '')