import urllib.request
import re
from bs4 import BeautifulSoup as BS
import sys
import csv
import itertools

#kegg_id=sys.argv[1]
infile=sys.argv[1]

#ec=[]
#kegg_id=[]

ectoko={}
infile="kos.txt"
file=open(infile,'r')
for line in file:
    url = 'https://www.genome.jp/dbget-bin/www_bget?ko:'+line
    page = urllib.request.urlopen(url).read()
    soup = BS(page, 'html.parser')
    links=soup.find_all('a',href=re.compile('dbget-bin\/www_bget\?ec:'))

    for link in links:
        print(link.text)
        ectoko[link.text]=line
        #ec.append(link.text)
        #kegg_id.append(line)

with open('kotoec.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in ectoko.items():
       writer.writerow([key, value])


ids=open('Kotoec.txt','w')
for (ec_id, kegg) in zip(ec, kegg_id):
    ids.write("%s\t%s\n" %(str(ec_id), str(kegg)))
ids.close()



with open('KOtoEC3.txt','a') as bipin:
    for (ec_id,kegg) in zip(ec, kegg_id):
        bipin.write("%s\t%s\n" %(str(ec_id), str(kegg)))
        bipin.close()

with open('v.csv', 'w') as csvfile:
    cwriter = csv.writer(csvfile, delimiter=',')

    for (ec_id, kegg) in zip(ec, kegg_id):
        cwriter.writerow(zip(kegg, ec_id))


def ECtoKO(ec_id):
    url = 'https://www.genome.jp/dbget-bin/www_bget?ec:'+ec_id
    page = urllib.request.urlopen(url).read()
    soup = BS(page, 'html.parser')
    links=soup.find_all('a',href=re.compile('dbget-bin\/www_bget\?ko:'))
    print(ec_id)
    for link in links:
        print(link.text)


