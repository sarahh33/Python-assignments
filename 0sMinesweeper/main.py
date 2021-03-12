import math
def main():
    name = input('Enter the name of the file with the locations of the mines:\n')
    hori = []
    try:
        myFile = open(name, "r")


        line =(myFile.readline()).rstrip()
        h=0
        mines =0
        whole =[]
        after_tran= []
        while len(line) > 0:
            s = 0
            hori = line.split((' '))
            number_hori = []
            for value in hori:
                if int(value) != 1 and int(value) != 0:
                    print("Invalid integer '{:}' on line: {:s}\nProgram terminating.".format(value, line))
                    exit()
                else:
                    number_hori.append(int(value))
                    if int(value)==1:
                        mines +=1
                    s+=1
            whole.append(number_hori)
            line = (myFile.readline()).strip()
            h+=1

        myFile.close()
        print("This {:}x{:} grid has {:} mines.".format(s,h,mines))
        print("Mine grid:")
        print("-"*(s*2+3))
        print_ori(whole)
        print()




    except ValueError:
        print("Invalid value '{:}' on line: {:s}\nProgram terminating.".format(value, line))
        exit()
    except OSError:
        print("File could not be read.\nProgram terminating.")
        exit()
    for i in range(len(whole)):
        line_new = []
        for j in range(len(whole[i])):
            line_new.append(whole[i][j])
        after_tran.append(line_new)



    print('Complete grid:')
    print("-" * (s * 2 + 3))
    after_tran = transformation(whole, after_tran)



def print_ori(whole):
    for i in range(len(whole)):
        print("| ",end='')
        for j in range(len(whole[i])):
            print("{:} ".format(whole[i][j]),end='')
        print("|")
    print("-"*(len(whole[i])*2+3))

def transformation(old, new):
    for line in new:
        for index in range(len(line)):
            if line[index]== 1:
                line[index]="*"
            else:
                tem = [[0,0,0],[0,0,0],[0,0,0]]
                try:
                    tem[0][0] = old[new.index(line)-1][index-1]
                    tem[0][1] = old[new.index(line)-1][index]
                    tem[0][2] = old[new.index(line)-1][index+1]
                    tem[1][0] = old[new.index(line)][index-1]
                    tem[1][2] = old[new.index(line)][index+1]
                    tem[2][0] = old[new.index(line) + 1][index - 1]
                    tem[2][1] = old[new.index(line) + 1][index]
                    tem[2][2] = old[new.index(line) + 1][index + 1]
                    line[index] = tem[0][1]+tem[0][2]+tem[0][1]+tem[1][0]+tem[1][2]+tem[2][0]+tem[2][1]+tem[2][2]



                except IndexError:
                    continue
                for i in tem:
                    for j in i:
                        print(j)


    print_ori(new)
    return new



main()