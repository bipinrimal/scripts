import urllib.request
import itertools
import re
from bs4 import BeautifulSoup as BS
import sys
import csv

file=open('Kos.txt')
url=""
for index,line in enumerate(file):
    if index == 0:
        url = 'http://rest.kegg.jp/link/ec/' + str.strip(line)
    else:
        url=url+'+'+str.strip(line)
    if index % 10000 == 0:
        page=urllib.request.urlopen(url)

file = open('Kos.txt')
url = ""

with open('Kos.txt','r') as file :
    slices = itertools.islice(file, 100)
    for index, line in enumerate(slices):
        if index == 0:
            url = 'http://rest.kegg.jp/link/ec/' + str.strip(line)
        else:
            url = url + '+' + str.strip(line)
        #if index % 10 == 9:
            #print(index)
            #print(url)
        page = urllib.request.urlopen(url)
        data=data.decode('utf-8')


def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk



