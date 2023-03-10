import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('./youtube_subs.csv', index_col=0, dtype={
    'Rank': 'int16',
    'Youtube Channel': 'string',
    'Subscribers': 'int32',
    'Video Views': 'int64',
    'Video Count': 'int32',
    'Category': 'category',
    'Started': 'int32'})

df = df.rename({
    'Youtube Channel': 'Youtube_Channel',
    'Video Views': 'Video_Views',
    'Video Count': 'Video_Count'
}, axis=1)

df['Category'].replace({
    'https://us.youtubers.me/global/all/top-1000-most_subscribed-youtube-channels': 'Other'},
    inplace=True)

df = df[df.Video_Views != 0]
df['Rank'] = df['Subscribers'].rank(ascending=False)
df['Rank'] = df['Rank'].astype(int)
df['views_over_counts'] = df.Video_Views/df.Video_Count
df.to_pickle('./youtube_subs.pkl')
