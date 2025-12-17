import pandas as pd

#lecture du fichier de résultats 
df = pd.read_csv("data/tests.csv")

# affichage des premières lignes
print(df.head())

# liste des colonnes
print("colonnes : ", df.columns)

# nombre de lignes et de colonnes
print("nombre de ligne et de colonnes : ",df.shape)

# types de données
print("type de données : ", df.dtypes)

#vérification que test id est unique
print(df['test_id'].is_unique)

#affchage des unités pour chaque mesure
print(df.groupby('measurement')['unit'].unique())

print(df.groupby('measurement')['value'].describe())

