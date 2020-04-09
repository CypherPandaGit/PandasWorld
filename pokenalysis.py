import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/LF_415_NUTS0.csv')

shape = df.head


ax = df.plot.scatter(x='NUTS_0',
                       y='2010',
                       alpha=1,
                       color='DarkBlue',
                       label='2010')
df.plot.scatter(x='NUTS_0',
                y='2020',
                alpha=0.5,
                color='Green',
                label='2020',
                ax=ax)
df.plot.scatter(x='NUTS_0',
                y='2030',
                alpha=0.4,
                color='Grey',
                label='2030',
                ax=ax)
df.plot.scatter(x='NUTS_0',
                y='2040',
                alpha=0.3,
                color='Grey',
                label='2040',
                ax=ax)
df.plot.scatter(x='NUTS_0',
                y='2050',
                alpha=0.2,
                color='Grey',
                label='2050',
                ax=ax)
plt.show()

# scatter alpha=0.5, hexbin gridsize=25,

print(shape)
