import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [10, 10]
df = pd.read_csv('data/LF_415_NUTS0.csv')

shape = df.head


ax = df.plot.scatter(x='NUTS_0',
                       y='2010',
                       alpha=1,
                       color='DarkBlue',
                       label='2010',
                     title='EU Population projection')

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

ax.set_xlabel('STATES')
ax.set_ylabel('DENSITY')

plt.show()

# scatter alpha=0.5, hexbin gridsize=25,

# print(shape)
