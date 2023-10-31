# %%
import pandas as pd
# %%
weather = pd.read_csv('public/weather.csv')
# %%
# Create histogram of max temperature using seaborn
# %%
import seaborn as sns   # seaborn is a visualization library
# %%
sns.distplot(weather['temp_max'], kde=False)
# %%
