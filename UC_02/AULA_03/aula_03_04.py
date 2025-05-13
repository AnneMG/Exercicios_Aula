#- O total e a média de pessoas vacinadas no período.
#- O total e a média da população do Brasil.
#- A taxa de vacinação anual, dos últimos 4 anos, sabendo que para se chegar a esse número, deve-se dividir a 
# quantidade de vacinados pela quantidade da população

import pandas as pd

def formatar(valor):
    return "{:,.2f}%".format(valor)

def visual(v):
    return "{:,.2f}%".format(v)

pop_vac= pd.Series([30000000, 25000000, 10000000, 5000000], index = ['2021','2022','2023','2024'])
pop_total=pd.Series([213317639, 214477744, 215574303, 216687971], index = ['2021','2022','2023','2024'])

media1= (pop_vac.sum()/4)
media2= (pop_total.sum()/4)

tx_vac= ((pop_vac/pop_total)*100).apply(formatar)
total_tx= (pop_vac.sum()/pop_total.tail(1).iloc[0])*100 #ultima posicao de uma serie

print(f'O total de pessoas vacinadas no período é:')
print(pop_vac.apply(visual))
print(f'A média de pessoas vacinadas no período é:{media1.mean():,.2f}')

print(f'O total da população do Brasil anual é')
print(pop_total.apply(visual))
print(f'A média do total da população do Brasil é: {media2.mean():,.2f}')

print (f'O total da taxa de vacinação anual é:{total_tx:.0f}')
print (f'O percentual de vacinação anual é:{tx_vac}%')