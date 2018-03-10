# coding: utf8
""" Made because i am to lazy to create filter manually"""
import json


def db_create(db):
    db = set()
    print('Input untill end of input. Use ctrl+d.')
    with open("forbidden_words.json", "w") as myfile:
        while True:
            try:
                inp = input("> ")
                db.add(inp)
            except EOFError:
                print("EOF")
                break
        myfile.write(json.dumps(list(db)))

        
def db_read():
    with open("forbidden_words.json", "r") as myfile:
        str = myfile.read()
        db = set(json.loads(str))
    db_create(db)


def main():
    choice = int(input('1.update. 2.create:\n'))
    if choice == 1:
        db_read()
    elif choice == 2:
        db = set()
        db_create(db)

        
if __name__ == '__main__':
    main()
            
