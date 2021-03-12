def dart():
    print("Welcome to the darts calculator! I will keep track of your game of darts.")
    line = input("What is the start score of the game?\n\n")
    original = int(line)
    turn = 1
    remain = original
    while remain > 1:
        print("Enter the results of your throws for round {:1d}:".format(turn))
        turnR = remain
        for i in range(1, 4):
            newThrow = "Throw {:1d}:".format(i)
            line = input(newThrow)
            remain = remain - int(line)

        turn += 1
        if remain == 1 or remain < 0:
            print(
                "You have reduced your score to {:1d} . Score resetting to the initial score of the round.\nYou have {:1d} points remaining.\n".format(
                    remain, turnR))
            remain = turnR
        elif remain != 0:
            print("You have {:1d} points remaining.\n".format(remain))
    print("You have 0 points remaining.\nYou have won the game after", turn - 1, "rounds. Congratulations!")


dart()