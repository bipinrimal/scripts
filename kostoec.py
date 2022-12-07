import urllib.request
import re
from bs4 import BeautifulSoup as BS
import sys
import csv


infile=sys.argv[1]


ectoko={}
infile='bid.txt'
file=open(infile,'r')

for index,line in enumerate(file):
    url = 'https://www.genome.jp/dbget-bin/www_bget?eco:'+line
    page = urllib.request.urlopen(url).read()
    soup = BS(page, 'html.parser')
    links=soup.find_all('a',href=re.compile('dbget-bin\/www_bget\?ec:'))
    if index % 10 == 0:
        print('KOs processed:',(index))
    elif index % 10 == 1 :
        print('Fetching EC numbers ......')
    for link in links:
        ectoko[link.text]=line

with open('kotoec.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in ectoko.items():
       writer.writerow([key, value])