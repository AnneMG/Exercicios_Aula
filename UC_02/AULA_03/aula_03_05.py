import pandas as pd

def formatar(valor):
    return "{:.2f}%".format(valor)

Maria = pd.Series([800,700,1000,900,1200,600,600], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])
Joao = pd.Series([900,500,1100,1000,900,500,700], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])
Manuel = pd.Series([700,600,900,1200,900,700,400], index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'])

print('A vendedora Maria realizou o quantitativo de vendas por dia:')
print(Maria)
print('O vendedor Joao realizou o quantitativo de vendas por dia:')
print(Joao)
print('O vendedor Manuel realizou o quantitativo de vendas por dia:')
print(Manuel)
print(f'A vendedora Maria realizou a média de vendas na semana: {Maria.mean():.0f}%')
print(f'O vendedor Joao realizou a média de vendas na semana: {Joao.mean():.0f}%')
print(f'O vendedor Manuel realizou a média de vendas na semana: {Manuel.mean():.0f}%')