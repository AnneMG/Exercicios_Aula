import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

endereco_dados = 'BASES\consumo_cerveja.csv'

# Lendo a planilha
df_planilha=pd.read_csv(endereco_dados,sep=',',encoding='utf-8')
print('\n---- OBTENDO DADOS ----')
#print(df_planilha)

# Criando o DataFrame 
df_cervejaria= df_planilha[['Data','Consumo','Temperatura', 'Tempo']]
df_temp_venda=df_cervejaria.groupby(['Data']).sum(['Consumo','Temperatura']).reset_index()

# Criando os Arrays de Temperatura e Venda
array_temp= np.array(df_cervejaria["Temperatura"])
array_venda= np.array(df_cervejaria["Consumo"])

#Calculando a media e a mediana (Temperatura e Consumo)
media = np.mean(array_temp)
print(f'A media da temperatura encontrada é:{media} ')
mediana=np.median(array_temp)
print(f'A mediana da temperatura encontrada é:{mediana} ')
mediav = np.mean(array_venda)
print(f'A media do consumo encontrada é:{mediav} ')
medianav=np.median(array_venda)
print(f'A mediana do consumo encontrada é:{medianav} ')

# Obtendo os Quartis Temperatura
q1_temp = np.quantile(array_temp, 0.25, method='weibull')
q2_temp = np.quantile(array_temp, 0.50, method='weibull')
q3_temp = np.quantile(array_temp, 0.75, method='weibull')
iqr_temp = q3_temp - q1_temp
print(f'O IQR é de: {iqr_temp}')

# Obtendo os Quartis Venda
q1_venda = np.quantile(array_venda, 0.25, method='weibull')
q2_venda = np.quantile(array_venda, 0.50, method='weibull')
q3_venda = np.quantile(array_venda, 0.75, method='weibull')
iqr_venda = q3_venda - q1_venda
print(f'O IQR é de: {iqr_venda}')

# Identificando os outliers superiores e inferiores
limite_superior_temp = q3_temp + (1.5 * iqr_temp)
limite_inferior_temp = q1_temp - (1.5 * iqr_temp)
limite_superior_venda = q3_venda + (1.5 * iqr_venda)
limite_inferior_venda = q1_venda - (1.5 * iqr_venda)

# Filtrando os limites
df_temp_outliers_superiores = df_cervejaria[df_cervejaria['Temperatura'] > limite_superior_temp]
df_temp_outliers_inferiores = df_cervejaria[df_cervejaria['Temperatura'] < limite_inferior_temp]
df_venda_outliers_superiores =df_cervejaria[df_cervejaria['Consumo'] > limite_superior_venda]
df_venda_outliers_inferiores = df_cervejaria[df_cervejaria['Consumo'] < limite_inferior_venda]

# Verificando a existência de Outliers Inferiores 
print('\n- Verificando a existência de outliers inferiores - Temperatura Media')
if len(df_temp_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_temp_outliers_inferiores)

# Verificando a existência de Outliers Superiores 
print('\n- Verificando a existência de outliers superiores - Temperatura Media')
if len(df_temp_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_temp_outliers_superiores)

# Verificando a existência de Outliers Inferiores 
print('\n- Verificando a existência de outliers inferiores - Producao cerveja')
if len(df_venda_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_venda_outliers_inferiores)

# Verificando a existência de Outliers superiores
print('\n- Verificando a existência de outliers superiores - Producao cerveja')
if len(df_venda_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_venda_outliers_superiores)
    
#Formula para avaliar a correlação entre a temperatura media e o consumo cerveja
corr_temp_venda = np.corrcoef(df_cervejaria['Consumo'], df_cervejaria['Temperatura'])[0,1]
print(f"Correlação entre a temperatura e consumo de cerveja: {corr_temp_venda:.3f}")

#Calculo para obtenção dos indicadores de coeficiente angular, intercepto e R²
temp=df_cervejaria[['Temperatura']]
venda=df_cervejaria[['Consumo']]
reg_cerveja= LinearRegression()
reg_cerveja.fit(temp,venda)
print(f'Coeficiente angular:{reg_cerveja.coef_[0][0]:2f}')
print(f'Intercepto: {reg_cerveja.intercept_[0]:2f}')
print(f"R²: {reg_cerveja.score(temp,venda):.3f}")

# Visualizando os Dados Analisados
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados - Temperatura Media e Venda de cervejas',fontsize=16)

# Posição 01: Gráfico dos Outliers superiores
df_temp_outliers_superiores_order = (df_cervejaria.sort_values(by='Temperatura',ascending=True))
df_temp_outliers_superiores_order = df_temp_outliers_superiores_order.head(10)
plt.subplot(2,2,1)
plt.title('Gráfico dos Outliers da Temperatura')
plt.barh(df_temp_outliers_superiores_order['Data'].astype(str),df_temp_outliers_superiores_order['Temperatura'])

# Posição 02: Gráfico dos Outliers superiores
df_venda_outliers_superiores_order = (df_cervejaria.sort_values(by='Consumo',ascending=True))
df_venda_outliers_superiores_order = df_venda_outliers_superiores_order.head(10)
plt.subplot(2,2,2)
plt.title('Gráfico dos Outliers do Consumo de cerveja')
plt.barh(df_venda_outliers_superiores_order['Data'].astype(str),df_venda_outliers_superiores_order['Consumo'])

# Posição 03: Gráfico de Correlação
plt.subplot(2,2,3)
plt.title('Correlação entre temperatura media e venda de cervejas')
plt.scatter(df_cervejaria['Temperatura'],df_cervejaria['Consumo'])
plt.xlabel('Temperatura')
plt.ylabel('Consumo de cervejas')

# Posição 04: Gráfico de Regressão linear
plt.subplot(2,2,4)
plt.title('Regressão linear para predição de consumo de cervejas e temperaturas')
sns.regplot( x='Temperatura', y='Consumo', data=df_temp_venda, fit_reg=True)
plt.show()