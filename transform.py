import pandas as pd #Biblioteca para manipulação de Dados. 

# Ler o arquivo CSV  
df = pd.read_csv("dados (1).csv", sep=";") 

#Remove as linhas totalmente vazias 
df = df.dropna(how="all") 

#Remove colunas vazias 
df = df.dropna(axis=1, how="all") 

print(df.shape) # Imprime o DataFrame após a remoção de linhas e colunas vazias 

df.to_csv("dados_transformados.csv", sep=";", index=False) 

