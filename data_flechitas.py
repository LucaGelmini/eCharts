import pandas as pd

XLS_PATH = "/mnt/F/DISCO_F/Informes/ICA_2023/12.Diciembre/ICA esqueleto diciembre 2023.xlsx"
df = (
    pd.read_excel(XLS_PATH, header=4, sheet_name="c2")
    .iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]]
    .rename(columns={
        'Unnamed: 0': 'total', 'Unnamed: 1': 'secciones', 'Unnamed: 2': 'capitulos', 'Exportacionese': 'Expo2024',
        'Variación porcentual': 'viaExpo', 'Importaciones*': 'Impo2024', 'Variación porcentual.1': 'viaImpo',
        'Saldo*': 'saldo', 'Expo': 'expo2023', 'Impo': 'impo2023'})
    .dropna(subset="secciones")
    .drop(["total", "capitulos"], axis=1))
print(df)

df.to_json("data_secciones.json", orient="records")
