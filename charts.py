import pandas as pd #Biblioteca para manipulação de tabelas/ Dados  
import matplotlib.pyplot as plt

df = pd.read_csv("bancos_tratado.csv")

top10 = (
    df.sort_values(
        by="Ativo Total",
        ascending=False
    )
    .head(10)
)

plt.figure(figsize=(12,6))
plt.bar(
    top10["Instituição"],
    top10["Ativo Total"]
)

plt.xticks(rotation=60)
plt.title(
    "Top 10 Instituições por Ativo Total"
)

plt.tight_layout()
plt.show()