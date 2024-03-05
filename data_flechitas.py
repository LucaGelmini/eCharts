import pandas as pd

XLS_PATH = "/mnt/F/DISCO_F/Informes/ICA_2023/12.Diciembre/ICA esqueleto diciembre 2023.xlsx"
df = (
    pd.read_excel(XLS_PATH, header=4, sheet_name="c2")
    .iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]]
    .rename(columns={
        'Unnamed: 0': 'total',
        'Unnamed: 1': 'secciones',
        'Unnamed: 2': 'capitulos',
        'Exportacionese': 'expo2024',
        'Variación porcentual': 'viaExpo',
        'Importaciones*': 'impo2024',
        'Variación porcentual.1': 'viaImpo',
        'Saldo*': 'saldo',
        'Expo': 'expo2023',
        'Impo': 'impo2023'})
    .dropna(subset="secciones")
    .drop(["total", "capitulos"], axis=1))
# print(df)

df.to_json("data_secciones.json", orient="records", index=False)


# Data complejos, cuadro 1

XLS_PATH_COMPLEJOS = "./esqueleto_complejos_2024.xlsx"

df_complejos = (
    pd.read_excel(XLS_PATH_COMPLEJOS, sheet_name="CUA NUE PAR TEXTO", header=4)
    .rename(columns={
        "Unnamed: 0": "Complejo",
        "Paricipación sobre el total exportado 2023*": "Part_2023",
        "Paricipación sobre el total exportado 2022*": "Part_2022",
        "2022*": "2022_dol",
        "2023*": "2023_dol",
        "Variación porcentual 2023*/22*": "varia",
        "Año récord 2002-2023": "top2002-2023"
    })
    .round(1)
    .drop(0)
)
print(df_complejos)
df_complejos.to_json("data_complejos_c1.json", orient="records", index=False)
