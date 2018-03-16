# coding: utf8
""" Made because i am to lazy to create filter manually"""
import json


def db_create(db):
    db = set()
	# I fyou want to stp input use ctrl+d
    with open("forbidden_words.json", "w") as myfile:
        while True:
            try:
                db.add(inp)
            except EOFError:#Decided to leave it here cause don't want to create stopping word
                print("EOF")
                break
        myfile.write(json.dumps(list(db)))

        
def db_read():
    with open("forbidden_words.json", "r") as myfile:
        str = myfile.read()
        db = set(json.loads(str))
    db_create(db)


def main():
    #Print 1 if you to update existing db.
    if choice == 1:
        db_read()
	#Print 2 if you want to create new db or rewrite existing.
    elif choice == 2:
        db = set()
        db_create(db)

        
if __name__ == '__main__':
    main()
            
