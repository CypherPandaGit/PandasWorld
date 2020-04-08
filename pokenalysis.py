import pandas as pd

df = pd.read_csv('data/pokemon_data.csv')

print(df.head(60)['Name'])

df.to_html('pokemon.html', index=False)
