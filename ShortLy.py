__author__ = 'aditya.ma'
import math
import sys
import linecache
from random import randint
import math
import os.path
import sqlite3

#there are 63 characters in total to which I can map  0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

conn = sqlite3.connect('test.db')
curr=conn.cursor()
curr.execute('create table if not exists short_url (url varchar(100), hash varchar(100))')
conn.commit()

BASE = 63
UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48

COUNTER=0

def get_rand_num():
    k=randint(0,99999)
    return k


def get_line(line_num):

    result=curr.execute('select * from short_url where hash=?',(str(line_num),))
    row =curr.fetchone()
    if not row:
        return 0
    return row[0]


def encode_url(url):
    global COUNTER
    rand_num=get_rand_num()
    if not get_line(rand_num):
        result=curr.execute('insert into short_url(url,hash) values(?,?)',(url,str(rand_num)))
        conn.commit()
        str1='http://shortly/'
        str1+=expand(rand_num)
        return str1
    elif COUNTER<100000:
        COUNTER+=1
        return encode_url(url)
    else:
        return -1
    fo.close()



def decode_url(url):
    str1=url.split('/',4)[3]
    line_num=shrink(str1)
    result=get_line(line_num)
    return result



def true_word(char):
    if char.isdigit():
        return ord(char) - DIGIT_OFFSET
    elif 'A' <= char <= 'Z':
        return ord(char) - UPPERCASE_OFFSET
    else:
        return ord(char) - LOWERCASE_OFFSET


def true_chr(integer):
    if integer < 10:
        return chr(integer + DIGIT_OFFSET)
    #lowecase characters
    elif 10 <= integer <= 35:
        return chr(integer + UPPERCASE_OFFSET)
    #uppercase characters
    else:
        return chr(integer + LOWERCASE_OFFSET)


def shrink(key):
    int_sum = 0
    reversed_key = key[::-1]
    for idx, char in enumerate(reversed_key):
        int_sum += true_word(char) * int(math.pow(BASE, idx))
    return int_sum


def expand(integer):
    if integer == 0:
        return '0'
    string = ""
    while integer > 0:
        remainder = integer % BASE
        string = true_chr(remainder) + string
        integer /= BASE
    return string



if __name__ == '__main__':
    url=sys.argv[1]
    url=encode_url(url)
    print url
    url=decode_url(url)
    print(url)
