import os
import sys
import json

import vk_api


def auth(): #Dirty because vk always generating different keys. Dunno if i can fix this.
    login = '8' + os.environ.get('VK_LOG')
    password = os.environ.get('VK_PASS')
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk


def content_control(text):
    with open('forbidden_words.json', 'r') as file:
        forb_words = json.loads(str(file.read()))
        for word in forb_words:
            if word in text: return False
        return True
    

def create_post_db(vk): 
    raws = vk.newsfeed.search(q = 'python', extended = 1, count = 100)
    db = list()
    if os.stat('vk_posts.json').st_size != 0:
        with open('vk_posts.json', 'r') as file:
            str = file.read()
            db = json.loads(str)
    for post in raws['items']:
        if content_control(post['text']) and post not in db:
            db.append(post)
    with open('vk_posts.json', 'w') as file:
        file.write(json.dumps(db))
    return 0


"""
Left this here because i am not sure if i need this anymore
def update_post_db(vk):
    raws = vk.newsfeed.search(q = 'python', extended = 1, count = 100)
    with open('vk_posts.json', 'r') as file:
        str = file.read()
        db = json.loads(str)
        for post in raws['items']:
            if content_control(post['text']) and post not in db:
                db.append(post)
    with open('vk_posts.json', 'w') as file:
        file.write(json.dumps(db))
    return 0
"""


def main():
    ses = auth()
    # Create data base if doesn't exists
    try:
        file = open('vk_posts.json', 'r')
    except IOError:
        file = open('vk_posts.json', 'w')

    create_post_db(ses)

        
if __name__ == '__main__':        
    main()
