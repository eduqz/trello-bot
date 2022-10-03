import requests
import json
from decouple import config


API_KEY = config('API_KEY')
API_TOKEN = config('API_TOKEN')


base_url = "https://api.trello.com/1"

headers = {
   "Accept": "application/json"
}

base_query = {
   'key': API_KEY,
   'token': API_TOKEN
}

def get_board_custom_fields(board_id):
    url = base_url + '/boards/%s/customFields' % board_id

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=base_query
    )

    response_data = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
    return response_data

def list_boards():
    url = base_url + "members/my/boards"

    query = base_query
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    print(response.text)

    response_data = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
    return response_data

def create_card(name, id_list):
    url = base_url + "/cards"

    query = base_query
    base_query['idList'] = id_list
    query['name'] = name

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    response_data = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
    return response_data

def set_custom_field(card_id, custom_field_id, id_value):
    url = base_url + "/card/%s/customField/%s/item" % (card_id, custom_field_id)

    query = base_query
    base_query['idValue'] = id_value

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    response_data = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
    return response_data