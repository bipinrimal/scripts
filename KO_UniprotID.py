##########################################################################################
# This is small script that converts kegg orthology id to uniprotID. Usually Kegg				 #
# Orthology id has a lot of mappings to uniprotIDs. However, for protein function,       #
# only one will suffice. (This means it will not work for figuring out the taxonomic 		 #
# source of the gene). The script goes to swissprot protein list of the kegg id and      #
# retrieves first recommended name (RecName) of a protein mapping to the kegg orthology  #
# id. It takes one argument, a single column list of keggOrthology Ids									 #																		
##########################################################################################				

import urllib.request
#pip install beautifulsoup
from bs4 import BeautifulSoup as BS
import sys
import itertools

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
