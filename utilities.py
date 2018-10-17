'''
Created on Jul 12, 2018

@author: Rahat Ibn Rafiq
'''
import json
import requests


def read_json_data(filepath):
    data = []
    f = open(filepath, "r")
    for line in f:
        if len(line) < 1:
            continue
        try:
            data.append(json.loads(line))
        except ValueError as e:
            print("Bad json. Line is: "+line+" Error is : "+e)
            continue
    return data


def get_instagram_profile_webpage_json(username):
    user_web_page = "https://www.instagram.com/"+username+"/"
    response = requests.get(user_web_page)
    status_code = response.status_code
    if status_code == 404:
        return
    content = str(response.content)
    index = content.index("window._sharedData")
    content = content[index:]
    index = content.index(";</script>")
    content = content[:index]
    index = content.index("{")
    content = content[index:]
    json_data = json.loads(content)
    return status_code,json_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]
