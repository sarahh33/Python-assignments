def main():
    name = input("Enter the name of the file containing the recipe:\n")
    try:
        recipe = open(name, 'r')
        lines = recipe.readlines()
        name_recipe = lines[0].rstrip()
        print("This recipe of {:} makes {:}.".format(lines[0].rstrip(), lines[1].rstrip()))
        int_bol = False
        while int_bol == False:
            try:
                number = int(input("How many servings do you want to make with this recipe?\n"))
                if number <= 0:
                    print("The amount needs to be positive!")
                else:
                    int_bol = True
            except ValueError:
                print("The amount needs to be an integer!")
        print("For {:} servings of {:} you will need:".format(number, name_recipe))
        serve = int((lines[1].split(' '))[0])
        for line in lines:
            if lines.index(line) >2:
                try:
                    line_list = line.rstrip().split(' ',1)
                    line_list[0]= round(float(line_list[0])*number/serve,1)
                    for item in line_list:
                        if line_list.index(item) != len(line_list)-1:
                            print(item, end=' ')
                        else:
                            print(item)

                except ValueError:
                    print(line,end='')


    except OSError:
        print("File could not be read. Terminating program.")
main()