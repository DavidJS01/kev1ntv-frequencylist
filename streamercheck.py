import requests

API_HEADERS = {
    'Client-ID': '[]',
    'Accept': 'application/vnd.twitchtv.v5+json'
}

URL = ''
Client_ID = ''
Secret = ''
authURL = ''

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
            
    return




