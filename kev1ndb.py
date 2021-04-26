import socket
import psycopg2
from sqlalchemy import create_engine
import requests
import sys

#Connect to DB

engine = create_engine('postgresql://rds.amazonaws.com:3302/')

kev1ndb = psycopg2.connect(
                user = '',
                password = '',
                host = 'rds.amazonaws.com',
                port = 3302,
                database = ''
)

kev1ndb.autocommit = True

cursor = kev1ndb.cursor()


#create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                Message VARCHAR(4000) NOT NULL, TwitchUser VARCHAR(4000) NOT NULL)''')

#Commit DB
kev1ndb.commit()

#Connect to KEV1NTV IRC Channel
sock = socket.socket()
sock.connect(('irc.chat.twitch.tv',6667))
sock.send(f"PASS oauth\n".encode('utf-8'))
sock.send(f"NICK chemdev\n".encode('utf-8'))
sock.send(f"JOIN #kev1ntv\n".encode('utf-8'))
    





def parseChat(resp):
    resp = resp.rstrip().split('\r\n')
    for line in resp:
            if "PRIVMSG" in line:
                messager = line.split(':')[1].split('!')[0]
                msg = line.split(':', maxsplit=2)[2]
                line = messager + ": " + msg
                line = line.encode('utf-8')
                cursor.execute("INSERT INTO messages (Message, TwitchUser) VALUES (%s,%s)", (msg, messager))
                kev1ndb.commit()
                print(line)
        




while True:
    resp = sock.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
    elif len(resp) > 0:
            parseChat(resp)


