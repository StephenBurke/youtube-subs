import numpy as np
import pandas as pd
import pickle
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

df = pd.read_pickle('./youtube_subs.pkl')

plt.rcParams["figure.figsize"] = [20, 8]
plt.rcParams["figure.autolayout"] = True
sns.set_style('dark')
sns.set(font_scale=1.5)

text_size = 23
subtitle_size = 20

bar_plot = sns.barplot(
    data=df,
    y='Category',
    x='Video_Views',
    errorbar=None,
    orient='h')

bar_plot.set_xlabel('Video Views (in 10 billions)')
bar_plot.set_title(
    'YouTube Views per category spanning from April 2019 to December 2022')

# next add plot showing category with views per video count

plt.yticks(rotation=20)
plt.show()
