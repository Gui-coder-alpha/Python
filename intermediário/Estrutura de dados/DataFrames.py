#Usado principalmente para análise de dados
#como tabelas e colunas, sendo bidimensionais
#contendo strings, números, booleanos, etc

#Dicionários ou arquivos CSV

import pandas as pd

data = {'A': ["a", "b", "c"],
        'B': ["c", "b", "a"],
        'C': ["c", "a", "b"],}

df = pd.DataFrame(data)  #Cria um dataframe, um matriz basicamente, no qual o nome da coluna
print(df)               #é o index, ou seja, o nome das colunas, e dentro deles, os valores, por colunas.

print("/////////////////////////////////////////")
print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')

estrutura = {'Nome': ['Ana', 'Pedro', 'Maria', 'José'],
             'Idade': [28, 34, 29, 40],
             'Salário': [3000, 5000, 4000, 4500],
             'Data_Admissao': pd.to_datetime(['2020-01-01', '2019-05-15', '2021-07-10', '2018-03-20'])}

datas_frame = pd.DataFrame(estrutura)
print(datas_frame)
print("/////////////////////////////////////////")

#filtrando
df_filtrando = datas_frame[datas_frame['Idade'] > 30]
print(df_filtrando)
print("/////////////////////////////////////////")

#Agrupando         parentese para o nome do dicionário
media_de_salario = datas_frame.groupby('Idade')['Salário'].mean()
print(media_de_salario)
print("/////////////////////////////////////////")

#Adicionando mais 1 coluna de ano
datas_frame['Ano_Admissao'] = datas_frame['Data_Admissao'].dt.year
print(datas_frame)
print("/////////////////////////////////////////")

#Pivot table
pivot = datas_frame.pivot_table(index = 'Idade', columns = 'Ano_Admissao', values = 'Salário', aggfunc = 'mean')
print(pivot)
print("/////////////////////////////////////////")
print('/////////////////////////////////////////')

#Aprendendo a manipular dataframes
datas_frame['Salário_dobrado'] = datas_frame['Salário'].apply(lambda x: x*2) #duplica o salário e adciona uma nova coluna salario dobrado
print(datas_frame)
print("/////////////////////////////////////////")

datas_frame['Media_movel'] = datas_frame['Salário'].rolling(window = 2).mean() #media móvel
#media movel pega os valores de window = x e faz a media dos x valores anteriores.
print(datas_frame)
print("/////////////////////////////////////////")

datas_frame['comprimento_do_nome'] = datas_frame['Nome'].str.len() #comprimento do nome, simples
print(datas_frame)
print("/////////////////////////////////////////")

# Agrupando por Ano de Admissão e calculando a média e a soma dos salários
agrupamento_complexo = datas_frame.groupby('Ano_Admissao').agg({'Salário': ['mean', 'sum']})
print(agrupamento_complexo)

