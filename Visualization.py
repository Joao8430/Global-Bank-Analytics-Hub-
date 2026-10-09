import pandas as pd #Importa a biblioteca pandas para manipulação de Dados. 
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Dados.csv" 
)

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

plt.xticks(rotation=45)

plt.title(
    "Top 10 Bancos por Ativo Total"
)

plt.tight_layout()

plt.show()