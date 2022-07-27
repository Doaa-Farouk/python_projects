# import sqlite3
# from sqlite3.dbapi2 import Cursor
import re

# db = sqlite3.connect("contacts.db")
# cr = db.cursor()
# cr.execute("create table if not exists MyContacts (Name str,PhoneNumber int ,Validation bool)")
# # names = ["Ahmad Ali", "Mohammad Taha", "Nada Taha","Roaa Sari",]
# name = input("enter your name: ")
# number = input("enter your phone number: ")
# if len(number) == 9:
#     valid = True
# else: 
#     valid = False

number = input("enter your phone number: ")
valid = re.match(r'/^7[0-9]{0,8}/',number)
print(valid)

# cr.execute("insert into MyContacts values(?,?,?)", (name, number, valid))

# db.commit()

