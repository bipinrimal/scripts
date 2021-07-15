
from urllib2.request import urlopen
from bs4 import BeautifulSoup as bs
import sys


def get_ids(url):
    response = urllib2.urlopen(url)
    html = response.read()
    b = bs(html)
    links = b.find_all('a')
    valid_link = lambda x: 'www_bget' in x.get('href')
    links = filter(valid_link, links)
    return [link.text for link in links]


def get_orthology_ids(pathway_id):
    URL = 'http://www.genome.jp'
    FUN = '/dbget-bin/get_linkdb?-t+orthology+path:'
    return get_ids(URL + FUN + pathway_id)


def get_gene_ids(orthology_id):
    URL = 'http://www.genome.jp'
    FUN = '/dbget-bin/get_linkdb?-t+genes+ko:'
    return get_ids(URL + FUN + orthology_id)


def get_fasta(gene_id):
    URL = 'http://www.genome.jp'
    FUN = '/dbget-bin/www_bget?-f+-n+n+'
    response = urllib2.urlopen(URL + FUN + gene_id)
    html = bs(response.read())
    return html.pre.text

def main():
    ortho_ids=get_orthology_ids('map00121')
    print(ortho_ids)

    for oid in ortho_ids:
        gene_ids=get_gene_ids(oid)

        with open(oid+'.fa','w') as out:
            for i, gene_id in enumerate(gene_ids,1):
                sys.stdout.write('.')
                if not i%5:
                    sys.stdout.write('')
                if not i%50:
                    sys.stdout.write('\n')
                sys.stdout.flus()

                fasta=get_fasta(gene_id)
                out.write(fasta)
	
