import pandas as pd

df = pd.read_csv(
    "bancos_tratado.csv" 
)

top10 = (

    df

    .sort_values(
        by="Ativo Total",
        ascending=False
    )

    .head(10)

)

print(
    top10[
        [
            "Instituição",
            "Ativo Total"
        ]
    ]
)