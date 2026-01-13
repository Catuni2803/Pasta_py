import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

notas = np.array([7,5,10,8.5,9.5,9])
media_notas = np.mean(notas)
maior_nota = np.max(notas)

print(media_notas)
print(maior_nota)

dados = {"nome" : ["ana" ,"beatriz" ,"carla" ,"diego"], "idade" : [16,17,18,20], "salario" : [1000,2000,1515,5000]}

df=pd.DataFrame(dados)
sns.barplot(x= "idade" ,y= "salario" ,data=df)
plt.show( )

#comparacoes
maior_de_idade = df["idade"][3]>=18
bom_salario = df["salario"][3]>=3000
#logica combinada
adulto_idependente = maior_de_idade and bom_salario
jovem_dependente = (not maior_de_idade) and (not bom_salario)

#classificacoes
if adulto_idependente: 
    print ("adulto bem de vida")
elif jovem_dependente: 
    print ("jovem sem dinheiro")
else: 
    print ("nenhuma das opcoes")
    