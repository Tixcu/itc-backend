import urllib.request
import urllib.parse
import json


f = open('film_db.json', 'r')
str = f.read()
db = json.loads(str)
tname = input('Введите фразу присуствующую в названии фильма: ')
for i in db:
    if tname.lower() in i['title'].lower():
        print(i['title'])
