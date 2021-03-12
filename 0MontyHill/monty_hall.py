import random


def initialize_doors(number_of_doors):
    boolean_list = [False] * number_of_doors
    car_index = random.randint(0, number_of_doors-1)
    boolean_list[car_index] = True

    return boolean_list

def remove_wrong_doors(chosen_door, doors):
    remained = []
    for i in range(len(doors)):
        if i != chosen_door:
            remained.append(i)
    if doors[chosen_door-1] == True:
        dont_open_number=remained[random.randint(0,len(remained)-1)]+1

    else:
        dont_open_number = doors.index(True)+1

    return dont_open_number

def print_doors(doors, dont_open):
    if dont_open == []:
        for i in range(len(doors)):
            print(" _ ", end=" ")
        print()
        for i in range(len(doors)):
            print("| |", end=" ")
        print()
        for i in range(len(doors)):
            print("|_|", end=" ")
        print()
        for i in range(len(doors)):
            if i < 9:
                print(" {:} ".format(i + 1), end=" ")
            elif 9 <= i < 99:
                print("{:} ".format(i + 1), end=" ")
            else:
                print("{:}".format(i + 1), end=" ")
        print()

        # door_parts = [" _ ", "| |", "|_|"]
        # for door_part in door_parts:
        #     for j in range(len(doors)):
        #         print(door_part, end=" ")
        #     print()
    else:
        for i in range(len(doors)):
            print(" _ ", end=" ")
        print()

        for i in range(len(doors)):
            if i+1 not in dont_open:
                print("|G|", end=" ")
                if doors[i]==True:
                    print("|C|", end=" ")
            else:
                print("| |", end=' ')
        print()
        for i in range(len(doors)):
            print("|_|", end=" ")
        print()
        for i in range(len(doors)):
            if i< 9:
                print(" {:} ".format(i + 1), end=" ")
            elif 9 <=i< 99:
                print("{:} ".format(i + 1), end=" ")
            else:
                print("{:}".format(i + 1), end=" ")
        print()



def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)
    number_of_doors = int(input("How many doors?\n"))
    while number_of_doors > 999 or number_of_doors<3:
        number_of_doors = int(input("The number of doors must be between 3-999!\nHow many doors?\n"))
    dont_open = []
    doors = initialize_doors(number_of_doors)
    print_doors(doors, dont_open)
    chosen_door= int(input("Choose a door 1-{:1}.\n".format(number_of_doors)))
    while not 0<=chosen_door<=number_of_doors:
        chosen_door = int(input("Choose a door 1-{:1}.\n".format(number_of_doors)))
    print("You chose the door number {:}.\n...".format(chosen_door))
    rest= remove_wrong_doors(chosen_door, doors)
    dont_open.append(rest)
    dont_open.append(chosen_door)
    print_doors(doors, dont_open)
    last_chance = int(input(("{:} certainly wrong doors were opened. The door number {:} was left.\nChoose {:} if you "
                             "want to keep the door you first chose and choose {:} if you want to change the door.\n")
                            .format((number_of_doors - 2), rest, chosen_door, rest)))
    while last_chance !=rest and last_chance!=chosen_door:
        last_chance = int(input("Choose {:} if you want to keep the door you first chose and choose {:} if you want to change the door.\n".format(chosen_door, rest)))
    for i in range(len(doors)):
        print(" _ ", end=" ")
    print()
    for i in range(len(doors)):
        if doors[i] == True:
            print("|C|",end=' ')
        else:
            print("|G|",end=' ')
    print()
    for i in range(len(doors)):
        print("|_|", end=" ")
    print()
    for i in range(len(doors)):
        if i < 9:
            print(" {:} ".format(i + 1), end=" ")
        elif 9 <= i < 99:
            print("{:} ".format(i + 1), end=" ")
        else:
            print("{:}".format(i + 1), end=" ")
    print()
    if last_chance-1 == doors.index(True):
        print("Congratulations! The car was behind the door you chose!")
    else:
        print("A goat emerged from the door you chose! The car was behind the other door :(")

   


main()