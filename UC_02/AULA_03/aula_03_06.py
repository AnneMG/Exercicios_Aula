#- Gerar um relatório com todos os dados da tabela.
#- O total e a média de vendas.
#- A média das idades, assim como a maior e menor idade.
#- O nome do vendedor com maior e menor quantidade de vendas no período.
#- A quantidade de vendas por sexo.

import pandas as pd

vendedores =[
    ['Ana','F',28,120],['Bruno','M',34,150],['Carlos','M',45,110],
    ['Diana','F',30,95],['Eduardo','M',40,130],['Fernanda','F',29,140],
    ['Gustavo','M',38,105],['Helena','F',31,125],['Igor','M',27,100],
    ['Juliana','F',33,135]
]

colunas = ['Nome', 'sexo','idade','Vendas']

df_vendedores = pd.DataFrame(vendedores, columns=colunas)

print('Relatório de Vendas:')
print(df_vendedores)

#criando metricas
soma_v = df_vendedores['Vendas'].sum()
media_v=df_vendedores['Vendas'].mean()

media_id=df_vendedores['idade'].mean()
maior_id=df_vendedores['idade'].max()
menor_id=df_vendedores['idade'].min()

maior_v = df_vendedores['Vendas'].max()
menor_v=df_vendedores['Vendas'].min()

melhor_v= df_vendedores[df_vendedores['Vendas'] == maior_v]['Nome']
pior_v= df_vendedores[df_vendedores['Vendas'] == menor_v]['Nome']

vendas_f= df_vendedores[df_vendedores['sexo'] == 'F']['Vendas'].sum()
vendas_m= df_vendedores[df_vendedores['sexo'] == 'M']['Vendas'].sum()

print(f'O valor total das vendas é: {soma_v}')
print(f'O media das vendas foi de:{media_v}')

print(f'O media de idades dos vendedores é de:{media_id}')
print(f'A maior idade dos vendedores é de:{maior_id}')
print(f'A menor idade dos vendedores é de:{menor_id}')

print(f'O vendedor que mais realizou vendas foi:{melhor_v.values[0]} vendendo {maior_v} produtos')
print(f'O vendedor que menos vendeu foi:{pior_v.values[0]} vendendo {menor_v} produtos')

print(f'A quantidade de vendas realizadas por mulheres foi de: {vendas_f}')
print(f'A quantidade de vendas realizadas por homens foi de: {vendas_m}')
