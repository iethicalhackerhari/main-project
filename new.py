import requests
# import json
# e406ea5622f69e29cdd544906c7c5b63bb30d585672ae0a40ba323106947c275 netflix
# 864e2137135cc5870e232c7502db018475f10cb9c89877349cd610b5b249edc5
# 54d85b9a386f621c249b0621582d60afae81efc1babe355ce337808c8b616979

def get_id():
    target = input()
    url = "https://www.virustotal.com/api/v3/urls"

    payload = f"url=https%3A%2F%2F{target}"
    headers = {
        "accept": "application/json",
        "x-apikey": "f4857af691da521a33d571b180eafc949231d58b863ad99a7945c51d68d96c21",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    id = response.json()['data']['id']
    id = str(id)
    id = id.split('-')[1]
    return id

# https://api.builtwith.com/free1/api.json?KEY=d994e4ae-76b0-406f-9c22-7a1a86fb8c39&LOOKUP=builtwith.com




def get_report():
    id = get_id()
    url = f"https://www.virustotal.com/api/v3/urls/{id}"

    headers = {
        "accept": "application/json",
        "x-apikey": "f4857af691da521a33d571b180eafc949231d58b863ad99a7945c51d68d96c21"
    }

    response = requests.get(url, headers=headers)

    print(response.json()['data']['attributes']['total_votes'])
    
get_report()
# get_builtwith()



def get_builtwith():
       
    url = f"https://api.builtwith.com/v20/api.json?KEY=d994e4ae-76b0-406f-9c22-7a1a86fb8c39&LOOKUP=netflix.com"

    

    response = requests.get(url)
    
    r= response.json()
    print(r['Results'])
    # i=0
    # while response.json()['groups']:
    #     print(response.json()['groups'][i]['name'])
    #     i+=1