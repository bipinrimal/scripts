import urllib.request
from bs4 import BeautifulSoup as BS
import sys
import itertools

kegg_id=sys.argv[1]
infile=sys.argv[1]

uniprot_id=[]
kegg_id=[]
file=open(infile,'r')
for line in file:
    url = 'https://www.genome.jp/dbget-bin/get_linkdb?-t+swissprot+ko:'+line
    page = urllib.request.urlopen(url).read()
    soup = BS(page, 'html.parser')
    links=soup.find_all('a')
    print("%s\t%s" %(line.strip(), links[1].text))

    kegg_id.append(line.strip())
    uniprot_id.append(links[1].text)


ids=open('uniprot_ids.txt','w')
for (k_id,up_id) in zip(kegg_id, uniprot_id):
    ids.write("%s\t%s\n" %(str(k_id), str(up_id)))

ids.close()

