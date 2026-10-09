#Importa a biblioteca pandas para manipulação de tabela. 
import pandas as pd

#ler o arquivo CSV 
df = pd.read_csv("src/Dados.csv", sep=";")
 
print("\nShape:")
print(df.shape)

print("\nPrimeiras linhas:")
print(df.head())

print("\nTipos:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isnull().sum())