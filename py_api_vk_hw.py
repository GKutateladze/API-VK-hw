from urllib.parse import urlencode
import requests
import json

APP_ID = 6414364
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.73'
}

TOKEN = '0a30610ef08e4fbe3e7730adaebe6bd25837a1e040744602f7ce9fbc99feb89699b9c16fbbdc811cd04e4'

def get_mutual(source_uid, target_uid):

    params = {
        'source_uid': source_uid,
        'target_uid': target_uid,
        'access_token': TOKEN,
        'v': '5.73'
    }

    response = requests.get('https://api.vk.com/method/friends.getMutual', urlencode(params)).text
    idList = json.loads(response)['response']
    for id in idList:
        print("vk.com/id"+str(id))

#get_mutual(6414364, 9467743) #me and my blogger friend with open account
get_mutual(5, 10)
