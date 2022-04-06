### Gets a list of all possible primer pairs when the primer sequences have degenerate symbols
### There will be forward and reverse primers

### Input primers
FWD="GTGYCAGCMGCCGCGGTAA"
RVE="GGACTACNVGGGTWTCTAAT"

import itertools


def consensus_to_possible(input):
### Making a dictionary of the degenerate symbols
    iupac={
        'A' : ["A"],
        'C' : ["C"],
        'G' : ["G"],
        'T' : ["T"],
        'U' : ["U"],
        'R' : ["A","G"],
        'Y' : ["C","T"],
        'S' : ["G","C"],
        'W' : ["A","T"],
        'K' : ["G","T"],
        'M' : ["A","C"],
        'B' : ["C","G","T"],
        'D' : ["A","G","T"],
        'H' : ["A","C","T"],
        'V' : ["A","C","G"],
        'N' : ["A","C","T","G"]}
### Empty sequence		
    sequences=['']
### For each sequence, the loop will go through each letter; add it to the temp list, get the corresponding symbol(s) 
### from the dictionary and append to the empty list
    for i in input:
        temp=[]
        for l in list(itertools.product(sequences,iupac[i])):
            t=l[0]+l[1]
            temp.append(t)
        sequences=temp
    return(sequences)

FWD_seqs=consensus_to_possible(FWD)
RVR_seqs=consensus_to_possible(RVE)

unique_combinations = []

permut = itertools.permutations(FWD_seqs, len(RVR_seqs))

for comb in permut:
    zipped = zip(comb, RVR_seqs)
    unique_combinations.append(list(zipped))

print(unique_combinations)

all_sequences=list(itertools.product(RVR_seqs,FWD_seqs))
for sequence in all_sequences:
    print(sequence)
