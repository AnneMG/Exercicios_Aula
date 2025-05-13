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
soma_jan = df_vendedores['Vendas'].sum()
media_jan=df_vendedores['Vendas'].mean()
maior_jan=df_vendedores['Vendas'].max()
menor_jan=df_vendedores['Vendas'].min(),

print(f'O valor total das vendas é: {soma_jan}')
print(f'O media das vendas foi de:')
print(f'O maior valor das vendas foi de:')
print(f'O menor valor das vendas foi de:')