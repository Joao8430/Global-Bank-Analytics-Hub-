import pandas as pd #Biblioteca para manipulação de tabelas.  

# Ler o arquivo CSV 
df = pd.read_csv(
    "data/processed/bancos_limpo.csv"
)

# Informações sobre o DataFrame (Quantidade de registros, Tipos de dados, Valores Nulos) 
print(df.info())

#Mensagem de estatísticas descritivas (Valores mínimos, máximos, médias, etc.) 
print(df.describe()) 

#Função para converter valores numéricos 
def converter_numero(valor):

    # Verifica se o valor é nulo 
    if pd.isna(valor):
        return None
# Converte o valor para string e remove os caracteres indesejados 
    valor = str(valor)

# Remove os caracteres indesejados  
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")
#Retorna o valor convertido  
    return float(valor) 

df["Ativo Total"] = df["Ativo Total"].apply(converter_numero) 

# Selecionar os 10 maiores ativos 
top_ativos = (  
    df.sort_values(
        by="Ativo Total",
        ascending=False
    )
    .head(10)
)

#Mensagem com os 10 maiores ativos  
print(top_ativos[
    ["Instituição", "Ativo Total"]
])