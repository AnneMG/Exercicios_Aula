# Script Utilizando Séries
import pandas as pd

def formatar(valor):
    return "{:.2f}%".format(valor)

roubo = pd.Series([100,90,80,120,110,90,70], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])
furto = pd.Series([80,60,70,60,100,50,30], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])
rec = pd.Series([70,50,90,80,100,70,50], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])

tx_rec = ((rec / roubo) * 100).apply(formatar)

print('\nQuantidade de Roubos e Furtos Diários')
print(roubo + furto)
print('\nPercentual de Recuperação e de Roubos de Veículos Diários')
print(tx_rec)