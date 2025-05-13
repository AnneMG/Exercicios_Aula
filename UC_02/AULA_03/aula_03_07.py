#Numeros simulados sobre a segurança publica do Rio de Janeiro p
import pandas as pd

def visual(v):
    return "{:,.2f}%".format(v)

ocorrencias = [ 
['Rio de Janeiro',6775561,35000], 
['Niteroi',515317,2500], 
['São Gonçalo',1091737,15000], 
['Duque de Caxias',924624,12000], 
['Nova Iguaçu',821128,10000], 
['Belford Roxo',513118,9000], 
['São João de Meriti',471906,8500], 
['Petrópolis',306678,1000], 
['Volta Redonda',273988,2000], 
['Campos dos Goytacazes',507548,4000], 
]

colunas = ['Nome', 'pop','qtd']
df_ocorrencia = pd.DataFrame(ocorrencias, columns=colunas)

total_ped=df_ocorrencia['qtd'].sum()
media_ped=df_ocorrencia['qtd'].mean()
total_pop=df_ocorrencia['pop'].sum()
media_pop=df_ocorrencia['pop'].mean()
maior_rped=df_ocorrencia['qtd'].max()
menor_rped=df_ocorrencia['qtd'].min()
maior_rpop=df_ocorrencia['pop'].max()
menor_rpop=df_ocorrencia['pop'].min()
maior_mun= df_ocorrencia[df_ocorrencia['qtd'] == maior_rped]['Nome']
menor_mun=df_ocorrencia[df_ocorrencia['qtd'] == menor_rped]['Nome']
maior_pes=df_ocorrencia[df_ocorrencia['pop'] == maior_rpop]['Nome']
menor_pes=df_ocorrencia[df_ocorrencia['pop'] == menor_rpop]['Nome']
taxa = ((df_ocorrencia['qtd'] / df_ocorrencia['pop']*100)).apply(visual)


print(f'O total de roubos a pedestres no Estado do Rio de Janeiro no último semestre: {total_ped}')
print(f'A média de roubos a pedestres no Estado do Rio de Janeiro no último semestre: {media_ped}')
print(f'O total da população no Estado do Rio de Janeiro: {total_pop}')
print(f'A média da população no Estado do Rio de Janeiro: {media_pop}')
print(f'O maior valor encontrado em relação aos roubos de pedestres: {maior_rped}')
print(f'O menor valor encontrado em relação aos roubos de pedestres: {menor_rped}')
print(f'O maior valor encontrado em relação a população: {maior_rpop}')
print(f'O menor valor encontrado em relação a população: {menor_rped}')
print(f'O nome do município com maior índice de roubos a pedestres foi {maior_mun.values[0]} e menor foi {menor_mun.values[0]}.')
print(f'O nome do município com maior quantidade de pessoas é {maior_pes.values[0]} e o menor {menor_pes.values[0]} .')
#A taxa de roubos a pedestres por município, sabendo que para se chegar a esse número, deve-se dividir a
#quantidade de roubos pela quantidade da população.

print('Relatorio de taxa de roubos a pedestres por municipio:')
print(df_ocorrencia['Nome'] + '  '+ taxa)
