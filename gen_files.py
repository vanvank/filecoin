#!/usr/bin/env python3
import os
import random
import string


def ran(n):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, n))  
    return salt


def gen_files(name, text, path):
    if not os.path.exists(path):
        os.makedirs(path)
    filename = os.path.join(path, name + ".txt")
    with open(filename,"w+") as f:
        f.write(text)
    print("ok")

for i in range(1,100):
    gen_files(ran(8), ran(32), "abc")
