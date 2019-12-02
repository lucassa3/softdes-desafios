"""
Script para add usuario
"""

import sqlite3
import hashlib

def add_user(user, pwd, typevar):
    """Adiciona um usuario

    :param user: Nome do ususario. 
    :type user: str. 
    :param pwd: Senha. 
    :type state: str. 
    :param typevar: tipo do usuario. 
    :type state: str. 
    :returns: void. 

    """ 
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute(
        'Insert into USER(user,pass,type) values("{0}","{1}","{2}");'
        .format(user, pwd, typevar)
    )
    conn.commit()
    conn.close()

with open('users.csv', 'r') as file:
    LINES = file.read().splitlines()

for users in LINES:
    cur_user = users.split(',')[0]
    cur_type = users.split(',')[1]
    print(cur_user)
    print(cur_type)
    add_user(cur_user, hashlib.md5(cur_user.encode()).hexdigest(), cur_type)