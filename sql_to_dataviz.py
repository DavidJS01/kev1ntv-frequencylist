# -*- coding: utf-8 -*-
from collections import Counter
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import plotly.express as px


engine = create_engine('postgresql://')




kev1ndb = psycopg2.connect(
user = 'root',
password = '',
host = '',
port = 3302,
database = 'kev1ndb'
)

kev1ndb.autocommit = True


cursor = kev1ndb.cursor()
cursor.execute("SELECT message FROM messages")
z = cursor.fetchall()
lst = str(z).split()
h = [words.replace('(', "").replace(',', "").replace('(', "").replace("'", "").replace(')', "") for words in lst]
counts = Counter(h)
print(counts)
x = []
y = []

data_for_viz = {"Words": x, "Times Used": y}

for words, count in counts.most_common(30):
    print(words, count)
    x.append(words)
    y.append(count)

print(data_for_viz)

df = pd.DataFrame.from_dict(data_for_viz)
print(df)

data_kev1ntv = px.bar(df, x='Words', y='Times Used')
data_kev1ntv.update_layout(uniformtext_minsize=12)
print(data_kev1ntv.show())

cursor = kev1ndb.cursor()
cursor.execute("SELECT twitchuser FROM messages")
z = cursor.fetchall()
lst = str(z).split()
h = [words.replace('(', "").replace(',', "").replace('(', "").replace("'", "").replace(')', "") for words in lst]
# lst = [word for line in z for word in line.split(" ")]
counts = Counter(h)
print(counts)
x = []
y = []

data_for_viz = {"Twitch User": x, "Messages Sent": y}

for words, count in counts.most_common(30):
    print(words, count)
    x.append(words)
    y.append(count)

print(data_for_viz)

df = pd.DataFrame.from_dict(data_for_viz)
print(df)

data_kev1ntv = px.bar(df, x='Twitch User', y='Messages Sent')
data_kev1ntv.update_layout(uniformtext_minsize=12)
print(data_kev1ntv.show())
