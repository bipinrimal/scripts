
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import sys
import pandas as pd

url="http://rest.genome.jp/list/module"

def get_modules(url):
    module_names=pd.read_table(url,sep="\t")
    module_id=[module_names.iloc[:,0]]
    return(module_id[0].values.tolist()[2:])

def get_def(module_id):
    base_url="https://www.genome.jp/entry/"
    url=base_url+module_id
    response = urlopen(url)
    html = response.read()
    b = bs(html)
    tag=b.findAll("td", attrs={'class':'td30'})[1]
    return(tag.text.strip())


def main():
    module_ids = get_modules(url)
    if not module_ids:
        sys.exit(1)
    module_ids=['M00001','M00002','M00003']
    for module_id in module_ids:
        #module_id=module_id[3:]
        module_defs = get_def(module_id)

        #print('Writing {} definitions to "{}.txt'.format(len()),len(uniprot_ids))

        # print('Writing {} uniprot ids to "{}.txt"').format(len(uniprot_ids), orthology_id)

        with open('link_module_def.txt', 'w') as out:
            out.write('%s   %s' % (module_id, module_defs))
            print('%s   %s' %(module_id, module_defs))

if __name__ == '__main__':
    main()
