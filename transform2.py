import pandas as pd

# =====================
# LEITURA
# =====================

df = pd.read_csv("Dados.csv", sep=";")

# =====================
# REMOVER LINHAS VAZIAS
# =====================

df = df.dropna(
    subset=["Instituição"]
)

# =====================
# REMOVER COLUNAS VAZIAS
# =====================

df = df.dropna(
    axis=1,
    how="all"
)

# =====================
# RESETAR ÍNDICE
# =====================

df = df.reset_index(drop=True)

print(df.shape)

print(df.head())

def converter_numero(valor):

    if pd.isna(valor):
        return None

    valor = str(valor)

    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    try:
        return float(valor)
    except:
        return None
    
colunas_financeiras = [

    "Ativo Total",

    "Resultado de Intermediação Financeira",

    "Resultado com Transações de Pagamento",

    "Outras Receitas / Despesas",

    "Resultado antes da Tributação e Participações (w) = (k) + (l) + (v)",

    "Imposto de Renda e Contribuição Social (x)",

    "Lucro Líquido (z) = (w) + (x) + (y)"

]

for coluna in colunas_financeiras:

    if coluna in df.columns:

        df[coluna] = df[coluna].apply(
            converter_numero
        )

print("\nTipos após conversão:\n")

print(
    df[colunas_financeiras].dtypes
)


df.to_csv(

    "bancos_tratado.csv",

    index=False

)

print("\nArquivo salvo com sucesso!") 