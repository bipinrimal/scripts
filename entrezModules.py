from Bio import Entrez

Entrez.email = "bipinrimal@gmail.com"

#### Get ids based on search term; here is an example of searching assembly for string queries
def get_ids(query,db="assembly"):
    ids = []
    handle = Entrez.esearch(db=db, term=query)
    record = Entrez.read(handle)
    ids.append(record["IdList"])
    return ids[0]

### Get assembly summary for each ids found above
def get_raw_summary(id,db="assembly"):
    handle = Entrez.esummary(db=db,id=id,report="full")
    record = Entrez.read(handle)
    #return(record['DocumentSummarySet']['DocumentSummary'][0]['AssemblyName']) #This will return the Assembly name
    return(record)

### Get lineage of taxids are organism with taxonomical data
def get_lineage(taxid):
    tax_lineage=[]
    handle=Entrez.efetch(db="taxonomy", id=taxid,retmode="xml")
    record = Entrez.read(handle)
    tax_lineage = record[0]["LineageEx"]
    tax_lineage.append({'TaxId': record[0]['TaxId'], 'ScientificName':record[0]["ScientificName"], 'Rank':'FullName'})
    return(tax_lineage)

if __name__ == '__main__':
    get_ids()
    get_raw_summary()
    get_lineage()
