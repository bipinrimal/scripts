import urllib.request
import sys
import json

query=sys.argv[1]
fo=open("chemical_names.txt")

def getPubChemID(query):
    url = "https://cts.fiehnlab.ucdavis.edu/rest/convert/Chemical%20Name/PubChem%20CID/"+query
    result=urllib.request.urlopen(url).read()
    result=json.loads(result)
    result=result[0]
    result=result.get('results')
    result=result[0]
    return result.replace("'","")

getPubChemID(query)
