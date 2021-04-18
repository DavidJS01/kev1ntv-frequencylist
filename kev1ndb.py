import socket
import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import requests
import sys

engine = create_engine('postgresql:')




kev1ndb = psycopg2.connect(
user = '',
password = '',
host = '',
port = 3302,
database = 'kev1ndb'
)

kev1ndb.autocommit = True


cursor = kev1ndb.cursor()


#create tables
cursor.execute("CREATE TABLE IF NOT EXISTS messages (Message VARCHAR(4000) NOT NULL, TwitchUser VARCHAR(4000) NOT NULL)")

kev1ndb.commit()




API_HEADERS = {
    'Client-ID': '[]',
    'Accept': 'application/vnd.twitchtv.v5+json'
}


Client_ID = ''
Secret = ''
authURL = 'https://id.twitch.tv/oauth2/token'

def StreamerCheck():

    AutParams = {'client_id': Client_ID, 'client_secret': Secret, 'grant_type': 'client_credentials'}


    AutCall = requests.post(url=authURL, params=AutParams) 
    access_token = AutCall.json()['access_token']

    head = {
        'Client-ID' : Client_ID,
        'Authorization' :  "Bearer " + access_token
    
        }
    
    r = requests.get('https://api.twitch.tv/helix/streams?user_id=48919437', headers = head).json()['data']
    if r:
        r=r[0]
        if r['type'] == '':
            status = 'offline'
            print(status)
            sys.exit()
        else:
            status = 'online'
            print(status)
    else: 
        status = 'offline'
        print(status)
        sys.exit()
    return




StreamerCheck()

sock = socket.socket()
sock.connect(('irc.chat.twitch.tv',6667))
sock.send(f"PASS oauth:\n".encode('utf-8'))
sock.send(f"NICK \n".encode('utf-8'))
sock.send(f"JOIN #kev1ntv\n".encode('utf-8'))




def parseChat(resp):
    resp = resp.rstrip().split('\r\n')
    for line in resp:
        if "PRIVMSG" in line:
            messager = line.split(':')[1].split('!')[0]
            msg = line.split(':', maxsplit=2)[2]
            line = messager + ": " + msg
            line = line.encode('utf-8')
            cursor.execute(" INSERT INTO messages (Message, TwitchUser) VALUES (%s,%s)", (msg, messager))
            kev1ndb.commit()
            print(line)
        





while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    elif len(resp) > 0:
        parseChat(resp)


    



         
    


