def main():
    peopleNum = int(input("Enter the number of the participants.\n"))
    while peopleNum < 2:
        print("The number must be at least 2!")
        peopleNum = int(input("Enter the number of the participants."))

    paymentList = moneyInput(peopleNum)
    totalMoney = moneyCalculation(paymentList)
    print_totalMoney(totalMoney)
    averageMoney = totalMoney / peopleNum
    eachone = eachPayment(averageMoney, paymentList)
    printFinal(eachone)


def moneyInput(peopleNum):
    payment = []
    for i in range(peopleNum):
        payment.append(float(input("Enter the sum (eur) paid by participant no {:1}.\n".format(i + 1))))
    return payment


def moneyCalculation(list):
    sum = 0
    for money in list:
        sum += money
    return sum


def eachPayment(averageMoney, paymentList):
    eachoneList = []
    for i in range(len(paymentList)):
        eachoneList.append(averageMoney - paymentList[i])
    return eachoneList


def print_totalMoney(totalMoney):
    print("Total costs are {:.2f} eur.".format(totalMoney))


def printFinal(eachone):
    for i in range(len(eachone)):
        if eachone[i] > 0:
            print("Participant no {:1} should pay {:.2f} eur.".format(i+1, eachone[i]))
        else:
            print("Participant no {:1} should receive {:.2f} eur.".format(i+1, abs(eachone[i])))


main()