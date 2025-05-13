#script utilizando series
import pandas as pd

idades = pd.Series([60,40,10,20,50,30,55,25,15,70])

maior = idades[idades >= 18]
menor = idades[idades < 18]

print('\n-- Lista das Idades Maiores e Iguais a 18 anos --')
print(maior.to_string(index=False))
print('\n-- Lista das Idades Menores que 18 anos --')
print(menor.to_string(index=False))