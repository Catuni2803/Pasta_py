import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
nomes = ["Alice", "João", "Ana", "José", "Carlos", "Janaína", "Caio", "Cristiane"]
nomes_com_a = [ ]
nomes_com_c = [ ]
nomes_com_j = [ ]
for nome in nomes:
    if nome.startswith("A"):
        nomes_com_a.append(nome)
for nome in nomes:
    if nome.startswith("C"):
        nomes_com_c.append(nome)
for nome in nomes:
    if nome.startswith("J"):
        nomes_com_j.append(nome)
print(nomes_com_a)
print(nomes_com_c)
print(nomes_com_j)


idades_dos_individuos = [17, 18, 25, 43, 15, 29, 36, 50]
idades_dos_individuos_maiores_de_18 = [ ]

for idade in idades_dos_individuos:
    if idade > 18:
        idades_dos_individuos_maiores_de_18.append(idade)

idades_dos_individuos_menores_que_18 = [ ]

for idade in idades_dos_individuos:
    if idade <= 18:
        idades_dos_individuos_menores_que_18.append(idade)

print(idades_dos_individuos_maiores_de_18)
print(idades_dos_individuos_menores_que_18)

salarios = [2000,3000,1500,2100,5000,1500,2000,2000]
contagem = { }

for salario in salarios:
    if salario in contagem:
        contagem[salario] = contagem[salario]+1

    else:
        contagem[salario] = 1
print(contagem)

valores_abc = ["A", "B", "C", "C", "A", "C", "B", "B", "A"]
contagem_categorias = { }

for contagens in valores_abc:
    if contagens in contagem_categorias:
        contagem_categorias[contagens] = contagem_categorias[contagens]+1
    else:
        contagem_categorias[contagens] = 1

print(contagem)

numero = 1
while numero<= 10:
    if numero %5 == 0:
        print(f"Número {numero} é divisível por 5")
    numero +=1

while numero < 20:
    if numero % 2 == 0:
        print(f"Número {numero} é par")
    else:
        print(f"número {numero} é ímpar")