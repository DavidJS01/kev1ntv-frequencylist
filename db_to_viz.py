# -*- coding: utf-8 -*-
from collections import Counter
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import plotly.express as px


#Create and Connect to DB
engine = create_engine('postgresqlrds.amazonaws.com:3302')

kev1ndb = psycopg2.connect(
                user = '',
                password = '',
                host = 'rds.amazonaws.com',
                port = 3302,
                database = ''
)

kev1ndb.autocommit = True

#Access DB
cursor = kev1ndb.cursor()
cursor.execute("SELECT message FROM messages")

#Fetch all messages, splitting them into individual words before cleaning the data
z = cursor.fetchall()
lst = str(z).split()
h = [words.replace('(', "").replace(',', "").replace('(', "").replace("'", "").replace(')', "") for words in lst]

#Count each word per appearance
counts = Counter(h)
print(counts)

#Assort data into a dictionary
x = []
y = []

data_for_viz = {"Words": x, "Times Used": y}
for words, count in counts.most_common(30):
    x.append(words)
    y.append(count)

#Create dataframe and visualize dataframe using Plotly
df = pd.DataFrame.from_dict(data_for_viz)

data_kev1ntv = px.bar(df, x='Words', y='Times Used')
data_kev1ntv.update_layout(uniformtext_minsize=12)
print(data_kev1ntv.show())

#Access DB
cursor = kev1ndb.cursor()
cursor.execute("SELECT twitchuser FROM messages")


#Fetch all users before cleaning the data
z = cursor.fetchall()
lst = str(z).split()
h = [words.replace('(', "").replace(',', "").replace('(', "").replace("'", "").replace(')', "") for words in lst]

#Count each word per appearance
counts = Counter(h)


#Sort data into a dictionary
x = []
y = []

data_for_viz = {"Twitch User": x, "Messages Sent": y}
for words, count in counts.most_common(30):
    x.append(words)
    y.append(count)

#Create dataframe and visualize dataframe using Plotly
df = pd.DataFrame.from_dict(data_for_viz)

data_kev1ntv = px.bar(df, x='Twitch User', y='Messages Sent')
data_kev1ntv.update_layout(uniformtext_minsize=12)
print(data_kev1ntv.show())