SYSTOLIC_LIMITS = [0, 100, 120, 130, 140, 160, 180]
DIASTOLIC_LIMITS = [0, 60, 80, 85, 90, 100, 110]
BLOOD_PRESSURE_DESCRIPTIONS = ['low', 'optimal', 'normal', 'high normal', 'grade 1 hypertension', 'grade 2 hypertension', 'grade 3 hypertension']
def main():
    file_name = input("Enter the name of the data file:\n")
    count = 0
    count_valid=0
    count_un = 0
    ignore = 0
    list_cal = [0] * 7
    try:
        fileOpen = open(file_name, 'r')
        lines = fileOpen.readlines()


        if lines != "":

            for line in lines:
                one_person = (line.rstrip()).split('/')
                try:
                    if 0<int(one_person[0])<250 and 0<int(one_person[1]) <250 :
                        if int(one_person[0]) >= int(one_person[1]) and len(one_person)==2:
                            count += 1
                            index = category(int(one_person[0]),int(one_person[1]))
                            list_cal[index] += 1


                        else:
                            count_un += 1
                            print("Invalid line # {:}: {:}".format(lines.index(line) + 1, line.rstrip()))

                    else:
                        ignore += 1


                except IndexError:
                    print("Invalid line # {:}: {:}".format(lines.index(line) + 1, line.rstrip()))
                    count_un += 1
                except ValueError:
                    count_un += 1
                    print("Invalid line # {:}: {:}".format(lines.index(line)+1, line.rstrip()))
            if ignore != 0:
                print("Removed {:} measurements from data.".format(ignore))
            if count != 0:
                print("\n{:} valid data points read.".format(count))
                print("Blood pressure distribution among the patients:")
                per_list = percent(list_cal, count)
                per_list[6]= 100-per_list[0]-per_list[1]-per_list[2]-per_list[3]-per_list[4]-per_list[5]
                print_pattern(per_list)
                num_high = list_cal[4]+list_cal[5]+list_cal[6]
                per_high = round(per_list[4]+per_list[5]+per_list[6])
                num_low= list_cal[0]
                per_low= round(per_list[0])
                if num_high != 0:
                    print("{:} ({:}%) of the patients have high blood pressure!".format(num_high, per_high))

                if num_low != 0:
                    print("{:} ({:}%) of the patients have low blood pressure!".format(num_low, per_low))
            else:
                print("Not enough valid data.")
        else:
            print("Not enough valid data.")
    except OSError:
        print("Error in reading the file.")



def category(high,low):
    index = 0
    for value in SYSTOLIC_LIMITS:
        if high>= value:
            index_high = SYSTOLIC_LIMITS.index(value)
    for value in DIASTOLIC_LIMITS:
        if low >= value:
            index_low = DIASTOLIC_LIMITS.index(value)
    if index_low==0 and index_high==0:
        index = 0
    elif index_high>= index_low:
        index = index_high
    else:
        index = index_low


    return index

def percent(list,count):
    per_list = [0.0]*7
    for value in list:
        index = list.index(value)
        per_list[index] = (value/count*100)

    return per_list

def print_pattern(per_list):

    for i in range(len(per_list)):
        type = BLOOD_PRESSURE_DESCRIPTIONS[i]
        n = round(per_list[i]/5)
        str = '#'*n
        print("{:25} | {:20} ({:}%)".format(type,str, round(per_list[i])))

main()