import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame Ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_hom_culp = df_ocorrencias[df_ocorrencias['ano'].between(2003,2024)]
df_hom_dolo = df_ocorrencias[df_ocorrencias['ano'].between(2003,2024)]

# Criando o DataFrame Homicidio doloso
df_hom_dolo = df_ocorrencias[['cisp','hom_doloso']]
df_hom_dolo = df_hom_dolo.groupby(['cisp']).sum(['hom_doloso']).reset_index()

# Criando o DataFrame Homicidio culposo
df_hom_culp = df_ocorrencias[['cisp','hom_culposo']]
df_hom_culp = df_hom_culp.groupby(['cisp']).sum(['hom_culposo']).reset_index()

#Criando dataframe Homicidio doloso e culposo
df_dolo_culp = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_dolo_culp = df_dolo_culp.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()

# Criando o Array doloso
array_hom_dolo= np.array(df_hom_dolo["hom_doloso"])

# Criando o Array culposo
array_hom_culp = np.array(df_hom_culp["hom_culposo"])

# Obtendo os Quartis - Doloso
q1_dolo = np.quantile(array_hom_dolo, 0.25, method='weibull')
q2_dolo = np.quantile(array_hom_dolo, 0.50, method='weibull')
q3_dolo = np.quantile(array_hom_dolo, 0.75, method='weibull')
iqr_dolo = q3_dolo - q1_dolo

# Obtendo os Quartis - Culposo
q1_culp = np.quantile(array_hom_culp, 0.25, method='weibull')
q2_culp = np.quantile(array_hom_culp, 0.50, method='weibull')
q3_culp = np.quantile(array_hom_culp, 0.75, method='weibull')
iqr_culp = q3_culp - q1_culp

# Identificando os outliers superiores e inferiores - Dolosos
limite_superior_dolo = q3_dolo + (1.5 * iqr_dolo)
limite_inferior_dolo= q1_dolo - (1.5 * iqr_dolo)

# Identificando os outliers superiores e inferiores - Culposos
limite_superior_culp = q3_culp + (1.5 * iqr_culp)
limite_inferior_culp = q1_culp - (1.5 * iqr_culp)

# Filtrando o DataFrame homicidios dolosos
df_dolo_outliers_superiores = df_hom_dolo[df_hom_dolo['hom_doloso'] > limite_superior_dolo]
df_dolo_outliers_inferiores = df_hom_dolo[df_hom_dolo['hom_doloso'] < limite_inferior_dolo]

# Filtrando o DataFrame homicidios culposos
df_culp_outliers_superiores = df_hom_culp[df_hom_culp['hom_culposo'] > limite_superior_culp]
df_culp_outliers_inferiores = df_hom_culp[df_hom_culp['hom_culposo'] < limite_inferior_culp]

# Verificando a existência de Outliers Inferiores para hom doloso
print('\n- Verificando a existência de outliers inferiores - Homicidio Doloso')
if len(df_dolo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_dolo_outliers_inferiores)

# Verificando a existência de Outliers Inferiores para hom doloso
print('\n- Verificando a existência de outliers inferiores - Homicidio Culposo')
if len(df_culp_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_culp_outliers_inferiores)

# Verificando a existência de Outliers Superiores para hom doloso
print('\n- Verificando a existência de outliers superiores - Homicidio Doloso')
if len(df_dolo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_dolo_outliers_superiores)

# Verificando a existência de Outliers Superiores para hom doloso
print('\n- Verificando a existência de outliers superiores - Homicidio Culposo')
if len(df_culp_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_culp_outliers_superiores)

# Correlação entre homicidio doloso e culposo
# 0.9 a 1.0 (positiva ou negativa) = Muito forte correlação
# 0.7 a 0.9 (positiva ou negativa) = Forte correlação
# 0.5 a 0.7 (positiva ou negativa) = Moderada correlação
# 0.3 a 0.5 (positiva ou negativa) = Fraca correlação
# 0.0 a 0.3 (positiva ou negativa) = Sem correlação

#Formula para avaliar a correlação entre os numeros apurados entre homicidio doloso e culposo
corr_hom_dolo_culp = np.corrcoef(df_dolo_culp['hom_doloso'], df_dolo_culp['hom_culposo'])[0,1]

#Mostra os dados calculados dos homicidios
print(f"Correlação entre homicidio doloso e culposo: {corr_hom_dolo_culp:.3f}")

#Calculo para obtenção dos indicadores de coeficiente angular, intercepto e R²
#Visualização da Reta de Regressão, através do Gráfico de Regressão linear

dolo=df_dolo_culp[['hom_doloso']]
culp=df_dolo_culp[['hom_culposo']]
reg_homicidios= LinearRegression()
reg_homicidios.fit(dolo,culp)
print(f'Coeficiente angular:{reg_homicidios.coef_[0][0]:2f}')
print(f'Intercepto: {reg_homicidios.intercept_[0]:2f}')
print(f"R²: {reg_homicidios.score(dolo, culp):.3f}")

# Visualizando os Dados Analisados
print('\n- Visualizando os Dados Analisados -')
plt.subplots(2,3,figsize=(16,7))
plt.suptitle('Análise dos Dados - Homicidios dolosos e culposos',fontsize=16)

# Posição 01: Gráfico dos Outliers dos homicidios dolosos
df_dolo_outliers_superiores_order = df_dolo_outliers_superiores.sort_values(by='hom_doloso',ascending=True)
plt.subplot(2,3,1)
plt.title('Gráfico dos Outliers dos homicidios dolosos')
plt.barh(df_dolo_outliers_superiores_order['cisp'].astype(str),df_dolo_outliers_superiores_order['hom_doloso'])

# Posição 02: Gráfico dos Outliers dos homicidios culposos
df_culp_outliers_superiores_order = df_culp_outliers_superiores.sort_values(by='hom_culposo',ascending=True)
plt.subplot(2,3,2)
plt.title('Gráfico dos Outliers dos Homicidios culposos')
plt.barh(df_culp_outliers_superiores_order['cisp'].astype(str),df_culp_outliers_superiores_order['hom_culposo'])

# Posição 03: Gráfico de Correlação dos homicidios dolosos e culposos
plt.subplot(2,3,3)
plt.title('Correlação dos homicidios dolosos e culposos')
plt.scatter(df_dolo_culp['hom_doloso'],df_dolo_culp['hom_culposo'])
plt.xlabel('Homicidios dolosos')
plt.ylabel('Homicidios culposos')

# Posição 04: Gráfico de Regressão linear
plt.subplot(2,3,4)
plt.title('Regressão linear dos Homicidios culposos')
sns.regplot( x='hom_doloso', y='hom_culposo', data=df_dolo_culp, fit_reg=True)
plt.show()

