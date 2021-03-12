# Problem description
This ia a program that finds the RNA string and protein (amino acid chain) corresponding to a given DNA string and prints the results.

A small part of human DNA codes proteins needed by the body. A DNA string includes four different bases, which are generally and also in this exercise represented by letters A (adenine), T (thymine), G (guanine) and C (cytosine). An RNA string, needed to create a protein, has the same bases except for T, which is replaced by U (uracil). In protein synthesis, where DNA codes a protein, the DNA is first copied into an RNA string in the following manner: the DNA string's A changes to U in the RNA, T to A, G to C and C to G. This happens because of chemical bonds that G and C form with each other, and A can form with either T or U. The resulting RNA codes a protein so that three successive bases in the string, or a codon, correspond to a single amino acid. These amino acids form a chain, which is a precursor of a protein.
# Examples
[execution of the program begins]\
Enter the DNA sequence:\
tacCGTCAGTCGATCGATCgctagctagAgtcagtcgtcatc\
DNA: TACCGTCAGTCGATCGATCGCTAGCTAGAGTCAGTCGTCATC\
RNA: AUGGCAGUCAGCUAGCUAGCGAUCGAUCUCAGUCAGCAGUAG\
Protein: Met-Ala-Val-Ser-*-Leu-Ala-Ile-Asp-Leu-Ser-Gln-Gln-*\
The protein has 14 amino acids in total.\
[execution of the program ends]
