dna_to_rna_bases = {"G": "C", "C": "G", "A": "U", "T": "A"}
amino_acids = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
               "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
               "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
               "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
               "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
               "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
               "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
               "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
               "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP",
               "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
               "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
               "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
               "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp",
               "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
               "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
               "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
               }


# Your code here
def check_dna(dna):
    dna_boolean = True
    for letter in dna:
        if letter not in dna_to_rna_bases or len(dna) % 3 != 0:
            dna_boolean = False
    return dna_boolean


def dna_to_rna(dna):
    rna = ''
    for dna_parts in dna:
        rna += dna_to_rna_bases[dna_parts]

    return rna


def rna_to_protein(rna):
    protein = ''
    protein_text = ''
    for index in range(len(rna)):
        protein_text += rna[index]
        if (index + 1) % 3 == 0:
            protein_text += '-'
    protein_text = protein_text.rstrip()
    protein_list = protein_text.split('-')
    del protein_list[len(protein_list) - 1]

    for element in protein_list:
        if amino_acids[element] == 'STOP':
            protein += '*-'

        else:
            protein += amino_acids[element] + '-'
    protein = protein[0:len(protein) - 1]
    return protein


def main():
    line = input("Enter the DNA sequence:\n").upper()
    dna_boolean = check_dna(line)
    if dna_boolean == False:
        print("Sorry, {:} is not a valid DNA sequence for protein synthesis.".format(line))
    else:
        print("DNA: {:}".format(line))
        rna = dna_to_rna(line)
        print("RNA: {:}".format(rna))
        protein = rna_to_protein(rna)
        print("Protein: {:}".format(protein))
        num = 1
        for syn in protein:
            if syn == '-':
                num += 1

        print("The protein has {:} amino acids in total.".format(num))


main()