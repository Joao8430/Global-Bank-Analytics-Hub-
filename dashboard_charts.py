import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bancos_tratado.csv")

ativos_uf = (

    df.groupby("UF")["Ativo Total"]

    .sum()

    .sort_values(
        ascending=False
    )

    .head(10)

)

plt.figure(figsize=(12,6))

ativos_uf.plot(kind="bar")

plt.title(
    "Top 10 Estados por Ativo Total"
)

plt.ylabel("Ativo Total")

plt.tight_layout()

plt.show()

lucro_uf = (

    df.groupby("UF")

    ["Lucro Líquido (z) = (w) + (x) + (y)"]

    .sum()

    .sort_values(
        ascending=False
    )

    .head(10)

)

plt.figure(figsize=(12,6))

lucro_uf.plot(kind="bar")

plt.title(
    "Top 10 Estados por Lucro"
)

plt.tight_layout()

plt.show()