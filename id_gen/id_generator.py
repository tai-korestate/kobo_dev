#!/usr/bin/python3

from hashlib import sha256
import random 

ID_LEN = 10

def generate_id():

    randomizer = ''.join([str(random.randint(x,x+100)) for x in range(5)])

    my_file = open("ids.txt","a+")
    my_file.seek(0)
    cur_list = my_file.read().split(',')
    
    counter = len(cur_list)

    my_hash = sha256(str(counter).encode('utf-8')).hexdigest()[:ID_LEN]
    if my_hash in cur_list:
        my_hash = my_hash + randomizer


    my_file.write(my_hash + ',')

    my_file.close()

    return

while True:
    generate_id()
