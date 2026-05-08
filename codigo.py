import pandas as pd
import matplotlib.pyplot as plt

# leitura do arquivo csv
dados = pd.read_csv('dados_pantanal.csv')

# converter colunas para numérico
dados['temperatura_c'] = pd.to_numeric(dados['temperatura_c'], errors='coerce')
dados[' nivel_rio_m'] = pd.to_numeric(dados[' nivel_rio_m'], errors='coerce')
dados[' ndvi'] = pd.to_numeric(dados[' ndvi'], errors='coerce')

# preencher valores vazios com a média
dados[' nivel_rio_m'] = dados[' nivel_rio_m'].fillna(dados[' nivel_rio_m'].mean())
dados[' ndvi'] = dados[' ndvi'].fillna(dados[' ndvi'].mean())

# tratar data 
dados['data'] = pd.to_datetime(dados['data'])

# calculo dos médias 
medias = dados[['temperatura_c', ' nivel_rio_m', ' ndvi']].mean()

print('\nMédias calculadas:')
print(medias)

# gráfico
plt.figure(figsize=(12,6))

# temperatura
plt.subplot(2,1,1)
plt.plot(
    dados['data'],
    dados['temperatura_c'],
    marker='o',
    color='red',
    label='Temperatura'
)

plt.title('Evolução da temperatura no Pantanal')
plt.ylabel('Graus Celsius')
plt.grid(True)
plt.legend()

# nível do rio
plt.subplot(2,1,2)

plt.plot(
    dados['data'],
    dados[' nivel_rio_m'],
    marker='s',
    color='blue',
    label='Nível do Rio'
)

plt.title('Nível do rio ao longo do tempo')
plt.xlabel('Data')
plt.ylabel('Escala')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
