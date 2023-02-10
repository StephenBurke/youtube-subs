import numpy as np
import pandas as pd
import pickle
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so

df = pd.read_pickle('./youtube_subs.pkl')

# Initialise the subplot function using number of rows and columns
fig, axis = plt.subplots(1, 2, figsize=(20, 8), sharey=True)
fig.suptitle('Top Subscribered YouTube Channels \nApril 2019 to December 2022')

plt.yticks(rotation=20)

sns.set_style('dark')
sns.set(font_scale=1.7)
sns.color_palette('pastel')

# views v category
sns.barplot(
    ax=axis[0],
    data=df,
    y='Category',
    x='Video_Views',
    errorbar=None,
    orient='h')

axis[0].set_title('YouTube views')
axis[0].set_xlabel("Video Views (in 10's of billions)")


# views/video_count v category
sns.barplot(
    ax=axis[1],
    data=df,
    y='Category',
    x='views_over_counts',
    errorbar=None,
    orient='h')

axis[1].set_title('YouTube views per video count')
axis[1].set_xlabel("Video Views (in 10's of millions)")
axis[1].set_ylabel('')

plt.show()
