import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#testar hipoteses na produção de sorvete RJ: (H1): Existe uma correlação positiva entre a temperatura média e 
#a produção de sorvete; (H2): A temperatura média é um bom preditor da produção de sorvete (modelo de 
#regressão linear simples).

endereco_dados = 'BASES\Base_sorvete.csv'

# Criando o DataFrame 
df_planilha=pd.read_csv(endereco_dados,sep=',',encoding='utf-8')
print('\n---- OBTENDO DADOS ----')
#print(df_planilha)

# Criando o DataFrame 
df_sorveteria = df_planilha[['Data','Producao_Sorvete','Temperatura_Media']]
df_temp_prod=df_sorveteria.groupby(['Data']).sum(['Temperatura_Media','Producao_Sorvete']).reset_index()

# Criando os Arrays 
array_temp= np.array(df_sorveteria["Temperatura_Media"])
array_prod= np.array(df_sorveteria["Producao_Sorvete"])

#Calculando a media e a temperatura e mediana
media = np.mean(array_temp)
print(f'A media da temperatura encontrada é:{media} ')
mediana=np.median(array_temp)
print(f'A mediana da temperatura encontrada é:{mediana} ')

#Calculando a media da producao
mediap = np.mean(array_prod)
print(f'A media da producao encontrada é:{mediap} ')
medianap=np.median(array_prod)
print(f'A mediana da producao encontrada é:{medianap}')

# Obtendo os Quartis  temperatura
q1_temp = np.quantile(array_temp, 0.25, method='weibull')
q2_temp = np.quantile(array_temp, 0.50, method='weibull')
q3_temp = np.quantile(array_temp, 0.75, method='weibull')
iqr_temp = q3_temp - q1_temp
print(f'O IQR é de: {iqr_temp}')

# Obtendo os Quartis  temperatura
q1_prod = np.quantile(array_prod, 0.25, method='weibull')
q2_prod = np.quantile(array_prod, 0.50, method='weibull')
q3_prod = np.quantile(array_prod, 0.75, method='weibull')
iqr_prod = q3_prod - q1_prod
print(f'O IQR é de: {iqr_prod}')

# Identificando os outliers superiores e inferiores
limite_superior_temp = q3_temp + (1.5 * iqr_temp)
limite_inferior_temp = q1_temp - (1.5 * iqr_temp)
print(f'O limite superior é de:{limite_superior_temp}')
print(f'O limite inferior é de:{limite_inferior_temp}')
limite_superior_prod = q3_prod + (1.5 * iqr_prod)
limite_inferior_prod = q1_prod - (1.5 * iqr_prod)

# Filtrando os limites
df_temp_outliers_superiores = df_sorveteria[df_sorveteria['Temperatura_Media'] > limite_superior_temp]
df_temp_outliers_inferiores = df_sorveteria[df_sorveteria['Temperatura_Media'] < limite_inferior_temp]
df_prod_outliers_superiores =df_sorveteria[df_sorveteria['Producao_Sorvete'] > limite_superior_prod]
df_prod_outliers_inferiores = df_sorveteria[df_sorveteria['Producao_Sorvete'] < limite_inferior_prod]

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
print('\n- Verificando a existência de outliers inferiores - Producao Sorvete')
if len(df_prod_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_prod_outliers_inferiores)

# Verificando a existência de Outliers superiores
print('\n- Verificando a existência de outliers superiores - Producao Sorvete')
if len(df_prod_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_prod_outliers_superiores)

#Formula para avaliar a correlação entre a temperatura media e a producao de sorvete
corr_temp_prod = np.corrcoef(df_sorveteria['Temperatura_Media'], df_sorveteria['Producao_Sorvete'])[0,1]
print(f"Correlação entre a temperatura media e a producao de sorvete: {corr_temp_prod:.3f}")

#Calculo para obtenção dos indicadores de coeficiente angular, intercepto e R²
temp=df_sorveteria[['Temperatura_Media']]
prod=df_sorveteria[['Producao_Sorvete']]
reg_sorvetes= LinearRegression()
reg_sorvetes.fit(temp,prod)
print(f'Coeficiente angular:{reg_sorvetes.coef_[0][0]:2f}')
print(f'Intercepto: {reg_sorvetes.intercept_[0]:2f}')
print(f"R²: {reg_sorvetes.score(temp,prod):.3f}")

# Visualizando os Dados Analisados
print('\n- Visualizando os Dados Analisados -')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados da sorveteria - Temperatura Media e Produção',fontsize=16)

# Posição 01: Gráfico dos Outliers superiores
df_temp_outliers_superiores_order = (df_sorveteria.sort_values(by='Temperatura_Media',ascending=True))
df_temp_outliers_superiores_order = df_temp_outliers_superiores_order.head(10)
plt.subplot(2,2,1)
plt.title('Gráfico dos Outliers da Temperatura Média')
plt.barh(df_temp_outliers_superiores_order['Data'].astype(str),df_temp_outliers_superiores_order['Temperatura_Media'])

# Posição 02: Gráfico dos Outliers superiores
df_prod_outliers_superiores_order = (df_sorveteria.sort_values(by='Producao_Sorvete',ascending=True))
df_prod_outliers_superiores_order = df_prod_outliers_superiores_order.head(10)
plt.subplot(2,2,2)
plt.title('Gráfico dos Outliers da Produção de Sorvete')
plt.barh(df_prod_outliers_superiores_order['Data'].astype(str),df_prod_outliers_superiores_order['Producao_Sorvete'])

# Posição 03: Gráfico de Correlação
plt.subplot(2,2,3)
plt.title('Correlação entre temperatura media e producao')
plt.scatter(df_sorveteria['Temperatura_Media'],df_sorveteria['Producao_Sorvete'])
plt.xlabel('Temperatura Media')
plt.ylabel('Producao de Sorvetes')

# Posição 04: Gráfico de Regressão linear
plt.subplot(2,2,4)
plt.title('Regressão linear para predição na produção de sorvetes e temperaturas')
sns.regplot( x='Temperatura_Media', y='Producao_Sorvete', data=df_temp_prod, fit_reg=True)
plt.show()