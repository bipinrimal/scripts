#Importing sys to take in arguments
import sys

#Protein file is the first one. 
protein_file=sys.argv[1]
print("Protein file: %s" % (str(protein_file)))

#Ligand file is the second one
ligand_file=sys.argv[2]
print("Ligand file: %s" % (str(ligand_file)))

# This function generates the output file name by combining
# protein and ligand names in format {protein}_{ligand}.pdbqt
def outputname(protein_file,ligand_file):
    out=protein_file.split('.')[0]+'_'+ligand_file.split('.')[0]+'.pdbqt'
    outfile=open(out,'w')
    print("The merged file will be saved as %s" % (out))
    return(outfile)

# This function generates identifiers dict file. It cuts the atom, amino acid and
# location and obtains line number where they are located. Only the lines 
# which start with 'ATOM' are used. Also, everything above 'ENDMDL' line 
# is used. This will only pick up lines from MODEL1. 
def get_identifiers(ligand_file):
    identifiers={}
    with open(ligand_file) as ligand:
        for num, line in enumerate(ligand, 0):
            if line.startswith('ATOM'):
                identifiers.update({num: line[13:26]})
            elif line.startswith('ENDMDL'):
                break
    return(identifiers)

# This is needed for later. Just opening the file, geting the lines and closing the file. 
def get_ligandlines(ligand_file):
    ligand = open(ligand_file, 'r')
    ligand_lines = ligand.readlines()
    ligand.close()
    return(ligand_lines)

# This is main script. 
def generate_output(protein_file,ligand_file):
    # Get the ligand lines
    ligand_lines=get_ligandlines(ligand_file)
    # Generate the output name
    outfile=outputname(protein_file,ligand_file)
    # Generate the dictionary of identifiers. {line_number:amino_acid_identifier}
    identifiers=get_identifiers(ligand_file)
    #Open protein file, find where the identifier are located, replace them with
    #corresponding line in ligand file. Write output of the lines and replaced 
    #lines if matched.
    with open(protein_file) as protein:
        for line in protein:
            for key,value in identifiers.items():
                if value in line:
                    line=line.replace(line,ligand_lines[key])
            outfile.write(line)
    outfile.close()
    print("File generated \n")

# Main script
def main():
    generate_output(protein_file,ligand_file)

if __name__ == "__main__":
    main()
