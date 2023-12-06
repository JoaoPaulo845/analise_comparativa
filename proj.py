#RECOMENDADO RODAR NO GOOGLE COLLAB OU JUPTER
#trecho 1
import pandas as pd
import matplotlib.pyplot as plt

def obter_dados_vendas():
    #[['2023-01-01', 'Produto1', 10, 100.0], ['2023-01-02', 'Produto2', 5, 200.0]]
    return [['2023-01-01', 'Produto1', 10, 100.0], ['2023-05-02', 'Produto1', 15, 100.0], ['2023-03-03', 'Produto1', 25, 100.0], ['2023-02-03', 'Produto1', 20, 100.0]]
#trecho 2
dados_vendas = obter_dados_vendas()
df_vendas = pd.DataFrame(dados_vendas, columns=['Data', 'Produto', 'Quantidade', 'Valor'])
df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])
print(df_vendas)
#trecho 3
df_agrupado = df_vendas.groupby(['Produto', pd.Grouper(key='Data', freq='M')]).agg({'Quantidade': 'sum'}).reset_index()

for produto in df_agrupado['Produto'].unique():
    df_temp = df_agrupado[df_agrupado['Produto'] == produto]
    plt.plot(df_temp['Data'], df_temp['Quantidade'], marker='o', linestyle='-', label=produto)

plt.title('Análise Comparativa de Vendas por Produto')
plt.xlabel('Data')
plt.ylabel('Quantidade Vendida')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()