LOWER_LIMITS = [5000, 25000, 55000, 200000, 1000000]
TAX_PERCENTS_RELATIVES = [0.08, 0.10, 0.12, 0.15, 0.17]
TAX_PERCENTS_OTHERS = [0.19, 0.25, 0.29, 0.31, 0.33]
START_TAX = 100


def main():
    gift_value = int(input("Enter the value of the gift:\n"))
    relative = False
    rela = input("Is the receiver a close relative (yes/no)?\n")
    if rela == "yes":
        relative = True
    else:
        relative = False
    gift_tax = calculate_gift_tax(gift_value, relative)
    print("Gift tax is {:.2f} euros.\n".format(gift_tax))
    if gift_tax > 0:
        expectation = int(input("How much gift tax are you willing to pay at most?\n"))
        if gift_tax <= expectation:
            print("You can give the whole gift in one installment.")
        else:
            times, taxPayment = yearsCalculation(gift_value, relative, expectation)
            years = times * 3
            print(
                "Tax would be {:.2f} euros per part and {:.2f} euros in total.\nIt would take you {:} years to give away the whole gift.".format(
                    taxPayment, taxPayment * (times + 1), years))


def calculate_gift_tax(gift_value, relative):
    if gift_value % 100 != 0:
        gift_value = gift_value // 100 * 100

    if relative == False:
        taxList = TAX_PERCENTS_OTHERS
    else:
        taxList = TAX_PERCENTS_RELATIVES

    taxPer, level = taxCalculation(gift_value, taxList)
    rest, restList = restFunction(level, taxList)
    if gift_value > 5000:
        sum = (gift_value - LOWER_LIMITS[level]) * taxPer + rest
    elif gift_value == 5000:
        sum = 100.00
    else:
        sum = 0.0

    return sum


def taxCalculation(gift_value, taxList):
    taxPer = 0
    level = 0
    for i in range(5):
        if gift_value > LOWER_LIMITS[i]:
            taxPer = taxList[i]
            level = i
    return taxPer, level


def restFunction(level, taxList):
    rest = 100
    restList = [100]
    for i in range(1, level + 1):
        rest += (LOWER_LIMITS[i] - LOWER_LIMITS[i - 1]) * taxList[i - 1]
        restList.append(rest)
    return rest, restList


def yearsCalculation(gift_value, relative, expectation):
    i = 2
    while i < 10000:
        gift_value_new = gift_value // i

        taxPayment = calculate_gift_tax(gift_value_new, relative)

        if taxPayment * i < expectation:
            print("You would have to part the gift in {:} parts ({:.2f} euros per part).".format(i, gift_value_new))
            return i - 1, taxPayment
        else:
            i += 1


main()