def apartmentCal():
    line = input("How much does the apartment cost?\n")
    cost = int(line)
    line = input("How much is your initial monthly salary?\n")
    salary = int(line)
    line = input("How many percent does your salary increase per year?\n")
    increase = int(line)
    line = input("And how many percent of your salary will you save?\n")
    savePercent = int(line)
    line = input("How much savings do you have?\n")
    save = int(line)
    while (cost <= 0) or (salary <= 0) or (increase < 0) or (savePercent < 0) or (save < 0) or (
            savePercent > 100) or increase > 100:
        print("Enter only positive values and percentages between 0 - 100!")
        line = input("How much does the apartment cost?\n")
        cost = int(line)
        line = input("How much is your initial monthly salary?\n")
        salary = int(line)
        line = input("How many percent does your salary increase per year?\n")
        increase = int(line)
        line = input("And how many percent of your salary will you save?\n")
        savePercent = int(line)
        line = input("How much savings do you have?\n")
        save = int(line)

    month = 0
    needMoney = cost - save
    newSalary = salary
    while needMoney > 0:
        needMoney = needMoney - savePercent / 100 * newSalary
        month += 1
        if month % 12 == 0:
            newSalary = newSalary * (1 + increase / 100)
    print("You need", cost - save, "euros for the apartment.")
    if month % 12 == 0:
        print("It will take you exactly", month // 12, "years to save the money for the apartment.")
    else:
        print("It will take you", month // 12, "years and", month % 12, "months to save the money for the apartment.")


apartmentCal()
