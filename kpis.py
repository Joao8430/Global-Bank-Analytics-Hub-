#Biblioteca para manipulação de Tabela  
import pandas as pd 

#Ler os dados 
df = pd.read_csv("Dados.csv") 

# Calcular o ativo total do mercado 
ativo_total_mercado = df["Ativo Total"].sum() 

#Dataframe para saber a participação de mercado 
df["Market Share"] = (df["Ativo Total"] / ativo_total_mercado) * 100 

#Mensagem informando a participação de mercado   
print(
    df[
        ["Instituição", "Market Share"] 
    ]
)

#Calcular a margem líquida 
df["Margem Liquida (%)"] = (
    df["Lucro Líquido"]
    /
    df["Receita"]
) * 100

#Mensagem informando a margem líquida   
print(
    df[
        ["Instituição", "Margem Liquida (%)"] 
    ]
) 

#Calculo da taxa de imposto
df["Taxa Imposto (%)"] = (
    df["Impostos"]
    /
    df["Resultado Antes Tributos"] 
) * 100

#Mensagem informando a taxa de imposto   
print( 
    df[
        ["Instituição", "Taxa Imposto (%)"] 
    ]
)  

#Eficiência Operacional / Quanto menor o gasto melhor fica para a empresa. 
df["Eficiencia Operacional (%)"] = (
    df["Despesas Operacionais"] 
    /
    df["Receitas Operacionais"]
) * 100

#Mensagem informando a eficiência operacional 
print( 
    df[
        ["Instituição", "Eficiencia Operacional (%)"] 
    ]
)   

ranking = (
    df.
    sort_values( 
        by="Lucro Líquido",
        ascending=False
    )
)

print(
    ranking[
        ["Instituição", "Lucro Líquido"]
    ].head(10)
)

#Os maiores bancos dominam o mercado 
top5 = (
    df
    .sort_values(
        by="Ativo Total",
        ascending=False
    )
    .head(5)
)

#Score Financeiro 
participacao = (
    top5["Ativo Total"].sum()
    /
    df["Ativo Total"].sum()
) * 100

print(
    f"Top 5 controlam {participacao:.2f}% do mercado"
)

df["Score"] = (

    df["Market Share (%)"] * 0.4

    +

    df["Margem Liquida (%)"] * 0.3

    +

    (
        100 -
        df["Eficiencia Operacional (%)"]
    ) * 0.3

)

score_final = (
    df
    .sort_values(
        by="Score",
        ascending=False
    )
)

print(
    score_final[
        ["Instituição", "Score"]
    ].head(10)
)