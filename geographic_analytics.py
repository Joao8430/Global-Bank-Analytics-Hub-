import pandas as pd 

df = pd.read_csv("bancos_tratado.csv") 

remover = [

    "C - Conglomerado",
    "S1 - Segmento 1",
    "S2 - Segmento 2",
    "S3 - Segmento 3",
    "S4 - Segmento 4",
    "S5 - Segmento 5",

    "1 - Público",
    "2 - Privado Nacional",
    "3 - Privado com Controle Estrangeiro",

    "I - Instituição independente"

]

df = df[
    ~df["Instituição"].isin(remover)
]

print(
    df["UF"]
    .value_counts()
)

#Ativo total por estado  
print("\nATIVO TOTAL POR UF\n") 
ativos_uf = (
    df
    .groupby("UF")["Ativo Total"] #Agrupa por UF e soma o Ativo Total 
    .sum()
    .sort_values(
        ascending=False
    )
)

#Lucro por estado  
print(ativos_uf) 
print("\nLUCRO POR UF\n")
lucro_uf = (
    df
    .groupby("UF")[
        "Lucro Líquido (z) = (w) + (x) + (y)" 
    ] 
    .sum()
    .sort_values(
        ascending=False
    )
)

print(lucro_uf)

print(df["UF"].value_counts())

print(
    df.groupby("UF")["Ativo Total"]
      .sum()
      .sort_values(ascending=False)
)

