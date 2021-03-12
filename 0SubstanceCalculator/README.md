# Problem description
The user wants to calculate amounts of substance for different substances. For this purpose the user has recorded molar masses of different substances in a file. The molar mass of a substance can be used to calculate the substance's amount of substance with the formula n = m / M, where n is the amount of substance, m is the mass of the substance and M is the molar mass of the substance.

Write a program that asks the user for the name of the file and reads the information from the file into a dictionary structure. Then the program asks the user for chemical formulas and masses of different substances and calculates the corresponding amounts of substance.
# Example
[execution of the program begins]\
Enter the name of the file with the molar masses:\
molar_masses_03.txt\
Invalid line: 'CuF:82.544:80.000'\
Invalid line: 'KrF2'\
Invalid molar mass on line: 'MgO:unknown'\
Invalid molar mass on line: 'NiS:ninety'\
Molar masses of 39 substances were successfully read from the file.

Enter the chemical formula of the substance. Stop by entering an empty line.\
NiS\
A molar mass for 'NiS' could not be found in the file.\

Enter the chemical formula of the substance. Stop by entering an empty line.\
KrF2\
A molar mass for 'KrF2' could not be found in the file.\

Enter the chemical formula of the substance. Stop by entering an empty line.\
NH4F\
Enter the mass of the substance (in grams):\
548.70\
548.700 grams of NH4F is equal to 14.815 moles.

Enter the chemical formula of the substance. Stop by entering an empty line.\
PbO4\
Enter the mass of the substance (in grams):\
8245.65\
8245.650 grams of PbO4 is equal to 30.405 moles.

Enter the chemical formula of the substance. Stop by entering an empty line.

Program terminating.\
[execution of the program ends]
