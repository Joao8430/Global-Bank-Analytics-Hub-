import pandas as pd 

# ======================================
# LEITURA
# ======================================

df = pd.read_csv("bancos_tratado.csv")

# ======================================
# REMOVER AGREGAÇÕES
# ======================================

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

# ======================================
# MARKET SHARE
# ======================================

ativo_total = df["Ativo Total"].sum()

df["Market Share (%)"] = (
    df["Ativo Total"]
    /
    ativo_total
) * 100

# ======================================
# ROA
# ======================================

df["ROA (%)"] = (

    df["Lucro Líquido (z) = (w) + (x) + (y)"]

    /

    df["Ativo Total"]

) * 100

# ======================================
# TAXA DE IMPOSTO
# ======================================

df["Taxa Imposto (%)"] = (

    abs(
        df["Imposto de Renda e Contribuição Social (x)"]
    )

    /

    abs(
        df["Resultado antes da Tributação e Participações (w) = (k) + (l) + (v)"]
    )

) * 100

# ======================================
# SCORE EXECUTIVO
# ======================================

df["MS_Norm"] = (

    df["Market Share (%)"]

    /

    df["Market Share (%)"].max()

)

df["ROA_Norm"] = (

    df["ROA (%)"]

    /

    df["ROA (%)"].max()

)

df["Executive Score"] = (

    df["MS_Norm"] * 0.70

    +

    df["ROA_Norm"] * 0.30

)

# ======================================
# SALVAR DATASET FINAL
# ======================================

df.to_csv(
    "fato_bancos.csv",
    index=False
)

print("Dataset BI criado com sucesso!")

print(df.shape)