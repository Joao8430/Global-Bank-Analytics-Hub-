import pandas as pd #Importa a biblioteca pandas para manipulação de Dados 

arquivo = "dados (1).csv" #Armazena o arquivo para leitura 

df = pd.read_csv( #Converte o CSV em DataFrame.  
    arquivo,
    sep=";",
    encoding="utf-8" #A forma como o arquivo vai ser lido. 
)

print(df.head()) #Mostra as primeiras linhas do DataFrame 