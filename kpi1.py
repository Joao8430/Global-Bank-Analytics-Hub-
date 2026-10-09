#O objetivo é quem controla a maior fatia do mercado financeiro.  

import pandas as pd #Biblioteca para manipulação de Dados. 

df = pd.read_csv("bancos_tratado.csv") #Ler o arquivo 

ativo_total_mercado = df["Ativo Total"].sum() #Calcular o ativo total do mercado 

# Calcular a participação de mercado para cada instituição 
df["Market Share (%)"] = (
    df["Ativo Total"] /
    ativo_total_mercado
) * 100

#Mensagem dos calculos finais 
print(
    df[
        ["Instituição", "Market Share (%)"]
    ]
    .sort_values(
        by="Market Share (%)",
        ascending=False
    )
    .head(10)
)

#Mensagem dos lucros
print("\nTOP 10 LUCRO LÍQUIDO\n")

# Calcular o top 10 das instituições com maior lucro líquido 
top_lucro = (
    df.sort_values(
        by="Lucro Líquido (z) = (w) + (x) + (y)",
        ascending=False
    )
    .head(10)
)

#Mensagem dos lucros 
print(
    top_lucro[
        [
            "Instituição",
            "Lucro Líquido (z) = (w) + (x) + (y)"
        ]
    ]
)
df["ROA (%)"] = ( # Calcular o ROA para cada instituição (Return on Assets) 
    df["Lucro Líquido (z) = (w) + (x) + (y)"]
    /
    df["Ativo Total"]
) * 100
print("\nTOP ROA\n")
print(

    df

    .sort_values(
        by="ROA (%)",
        ascending=False
    )
    .head(10)
    [["Instituição", "ROA (%)"]]

)

#Taxa efetivia de impostos 
df["Taxa Imposto (%)"] = (

    abs(
        df["Imposto de Renda e Contribuição Social (x)"]
    )
    /
    abs(
        df["Resultado antes da Tributação e Participações (w) = (k) + (l) + (v)"]
    )
) * 100

print("\nTAXA DE IMPOSTO\n")

print(
    df
    [["Instituição", "Taxa Imposto (%)"]]
    .sort_values(
        by="Taxa Imposto (%)",
        ascending=False
    )
    .head(10)
)

#Score bancário / criamos um ranking próprio  
df["Score"] = (
    df["Market Share (%)"] * 0.4
    +
    df["ROA (%)"] * 0.6
)

print("\nRANKING FINAL\n")

ranking = (
    df
    .sort_values(
        by="Score",
        ascending=False
    )
)
print(
    ranking[
        [
            "Instituição",
            "Score"
        ]
    ]
    .head(20)
)

#Cria um Dataset analitico e depois salva.  
df.to_csv(
    "bancos_kpis.csv",
    index=False
)
#Mensagem do dataset criado.  
print(
    "\nDataset Analítico Criado!"
)

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

    "I - Instituição independente",

    "b1 - Banco Comercial, Banco Múltiplo com Carteira Comercial ou Caixa Econômica"

]

df = df[
    ~df["Instituição"].isin(remover)
]

#Criando um score mais robusto 
df["Market Share (%)"] = (
    df["Ativo Total"] /
    df["Ativo Total"].sum()
) * 100

# Normalizando os KPIs 
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

ranking = (

    df

    .sort_values(
        by="Executive Score",
        ascending=False
    )

)

print(
    ranking[
        [
            "Instituição",
            "Executive Score"
        ]
    ].head(20)
)

print(df["UF"].value_counts()) 

# Filtrando instituições com resultado antes da tributação acima de 1000 
df = df[
    abs(
        df["Resultado antes da Tributação e Participações (w) = (k) + (l) + (v)"]
    ) > 1000
]