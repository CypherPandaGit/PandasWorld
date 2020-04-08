import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/pokemon_data.csv')


# df.to_html('pokemon.html', index=False)

plot = df.plot.scatter(x= 'Attack',
                       y= 'Defense',
                       alpha= 0.5)
plt.show()
