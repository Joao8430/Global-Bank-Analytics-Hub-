import pandas as pd

df = pd.read_csv("bancos_tratado.csv") 

print("Shape original:") 
print(df.shape) 

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

print("\nShape após filtro:")
print(df.shape)

print("\nPrimeiras instituições:")
print(df["Instituição"].head(20))