import random

WIN = 60
SINGLE_PIG = ["Side (no dot)", "Side (dot)", "Razorback", "Trotter", "Snouter", "Leaning Jowler"]
PROBS = [0.35, 0.65, 0.87, 0.96, 0.99, 1]
SINGLE_PIG_POINTS = {"Side (no dot)": 0, "Side (dot)": 0, "Razorback": 5, "Trotter": 5, "Snouter": 10,
                     "Leaning Jowler": 15}
BOTH_PIGS = {"Side (no dot)": "Sider", "Side (dot)": "Sider", "Razorback": "Double Razorback",
             "Trotter": "Double Trotter", "Snouter": "Double Snouter", "Leaning Jowler": "Double Leaning Jowler"}
BOTH_PIGS_POINTS = {"Sider": 1, "Double Razorback": 20, "Double Trotter": 20, "Double Snouter": 40,
                    "Double Leaning Jowler": 60}


def throw_pig():
    """
    The function returns the outcome (string) of tossing one pig.
    """
    # Write your code here

    outcome = ''
    possibility = random.random()

    for i in range(len(PROBS)):
        if PROBS[i] > possibility:
            outcome = SINGLE_PIG[i]
            return outcome


def throw_two_pigs():
    """
    The function throws two pigs and returns the name (string) and points (int) of the combo.
    """
    # Write your code here
    turn_outcome = ''
    turn_points = 0
    outcome_one = throw_pig()

    outcome_two = throw_pig()

    if outcome_one == outcome_two:

        turn_outcome = BOTH_PIGS[outcome_one]

        turn_points = BOTH_PIGS_POINTS[turn_outcome]
    elif outcome_one == "Side (no dot)" and outcome_two == "Side (dot)":
        turn_outcome = 'Pig out'
        turn_points = 0

    elif outcome_one == "Side (dot)" and outcome_two == "Side (no dot)":
        turn_outcome = 'Pig out'
        turn_points = 0

    else:
        turn_outcome = 'Other combo: ' + outcome_one + ' + ' + outcome_two
        turn_points = SINGLE_PIG_POINTS[outcome_one] + SINGLE_PIG_POINTS[outcome_two]

    return turn_outcome, turn_points


def one_turn(sum_former):
    i = 0
    sum = 0
    new_sum = sum_former
    continue_value = 'yes'
    while new_sum < 60 and continue_value == 'yes':
        turn_outcome, turn_points = throw_two_pigs()
        i += 1
        if turn_points == 0:
            sum = 0
            new_sum = 0
            continue_value = 'no'
            print('{:}. Pig out, 0 points\nThe turn ended. Points from this turn were set to 0.'.format(i))


        else:
            print("{:}. {:}, {:} points".format(i, turn_outcome, turn_points))
            sum += turn_points
            print('{:} points gathered this round!'.format(sum))
            new_sum += turn_points

            if new_sum >= 60:
                print('The total score of {:} (>= 60) points reached! The turn ends.'.format(new_sum))

            else:
                continue_value = input("Enter \"yes\" if you want to continue your turn.\n")
    return sum


def com_turn(com_former, human_points):
    i = 1
    new_sum = com_former
    round_sum = 0
    turn_outcome, turn_points = throw_two_pigs()
    continue_value = True
    while turn_points != 0 and continue_value == True:
        round_sum += turn_points
        new_sum += turn_points
        if human_points >= 60:
            if new_sum <= human_points:

                print("{:}. {:}, {:} points".format(i, turn_outcome, turn_points))
                print('{:} points gathered this round!'.format(round_sum))
                turn_outcome, turn_points = throw_two_pigs()
                i += 1
            else:
                continue_value = False
                print("{:}. {:}, {:} points".format(i, turn_outcome, turn_points))
                print('{:} points gathered this round!'.format(round_sum))
                print('The total score of {:} (>= {:}) points reached! The turn ends.'.format(new_sum, human_points+1))
        else:
            print("{:}. {:}, {:} points".format(i, turn_outcome, turn_points))
            print('{:} points gathered this round!'.format(round_sum))
            if 0 < round_sum < 10 and new_sum < 60:
                turn_outcome, turn_points = throw_two_pigs()
                i += 1
            elif round_sum >= 10:
                continue_value = False
            elif new_sum >= 60:
                continue_value = False
                print('The total score of {:} (>= 60) points reached! The turn ends.\n'.format(new_sum))

    if turn_points == 0:
        print("{:}. Pig out, 0 points\nThe turn ended. Points from this turn were set to 0.".format(i))
        round_sum = 0

    return round_sum


def main():
    print("Play a game of pass the pigs against the computer!")
    seed = int(input("Set seed:\n"))
    random.seed(seed)

    # Write your code here

    human_sum = 0
    com_sum = -1
    sum = -1
    print("\n------------------------------\nIt's your turn to pass the pigs!")
    human_sum = one_turn(human_sum)
    line = input("Press enter to continue.\n")
    print("------------------------------\nIt's computer's turn to pass the pigs!")
    com_sum = com_turn(com_sum, human_sum)

    line = input("Press enter to continue.\n")
    print("------------------------------\nYour score: {:}\nComputer's score: {:}".format(human_sum, com_sum))

    while human_sum < 60 and com_sum < 60:
        print("------------------------------\nIt's your turn to pass the pigs!")
        human_sum += one_turn(human_sum)

        line = input("Press enter to continue.\n")
        print("------------------------------\nIt's computer's turn to pass the pigs!")

        sum = com_turn(com_sum, human_sum)
        com_sum += sum
        line = input("Press enter to continue.\n")
        print("------------------------------\nYour score: {:}\nComputer's score: {:}".format(human_sum, com_sum))

    if human_sum >= 60 and sum == 0:
        print("\nYou won! Congratulations!")
    elif human_sum >= 60 and 0 < com_sum < human_sum:

        line = input("Press enter to continue.\n")
        sum = com_turn(com_sum, human_sum) + com_sum

        print("------------------------------\nYour score: {:}\nComputer's score: {:}".format(human_sum, com_sum))
        if human_sum > com_sum:
            print("\nYou won! Congratulations!")
        else:
            print("\nComputer won!")
    else:
        if human_sum > com_sum:
            print("\nYou won! Congratulations!")
        else:
            print("\nComputer won!")


main()
