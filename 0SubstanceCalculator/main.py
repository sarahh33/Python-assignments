def main():
    name = input("Enter the name of the file with the molar masses:\n")
    line_number = 0
    try:
        dictionary ={}
        myFile = open(name,'r')
        file_line = myFile.readline()
        file_line = file_line.rstrip()



        while file_line != '':
            try:
                parts = (file_line).split(':')
                try:
                    if len(parts)>2:
                        print("Invalid line: '{:}'".format(file_line))


                    elif parts[0] in dictionary:
                        decision = input(
                            'A molar mass for {:} has already been saved in the dictionary ({:.3f} g/mol).\nShould it be replaced by the value {:.3f} g/mol (y/n)?\n'.format(
                                parts[0], dictionary[parts[0]],float(parts[1])))
                        if decision == 'y':
                            dictionary[parts[0]] = round(float(parts[1]), 3)
                    else:
                        dictionary[parts[0]] = round(float(parts[1]), 3)
                        line_number += 1
                except ValueError:
                    print("Invalid molar mass on line: '{:}'".format(file_line))

            except IndexError:
                print("Invalid line: '{:}'".format(file_line))



            except OSError:
                print("Invalid line: '{:}'".format(file_line))

            file_line = myFile.readline()
            file_line = file_line.rstrip()
        myFile.close()
        print('Molar masses of {:} substances were successfully read from the file.\n'.format(line_number))
        ele = input('Enter the chemical formula of the substance. Stop by entering an empty line.\n')
        result = calculation(ele, dictionary)

    except OSError:
        print('File could not be read.')
        print('Program terminating.')




def calculation(ele,dictionary):
    result = 0
    while len(ele)>0:
        if ele in dictionary:
            line = input('Enter the mass of the substance (in grams):\n')

            while len(line) >0:
                try:
                    sub = round(float(line),3)

                    if sub < 0.000:
                        line = input('The mass needs to be positive or zero!\nEnter the mass of the substance (in grams):\n')
                    else:
                        result = sub /dictionary[ele]
                        print("{:.3f} grams of {:} is equal to {:.3f} moles.\n".format(sub, ele, result))
                        ele = input('Enter the chemical formula of the substance. Stop by entering an empty line.\n')
                        if ele != '':
                            line = input('Enter the mass of the substance (in grams):\n')
                        else:
                            line = ''


                except ValueError:
                    line = input('The mass needs to be a number!\nEnter the mass of the substance (in grams):\n')


        else:
            ele =input("A molar mass for '{:}' could not be found in the file.\n\nEnter the chemical formula of the substance. Stop by entering an empty line.\n".format(ele))
    if ele =='':
       print('Program terminating.')
    return result
main()