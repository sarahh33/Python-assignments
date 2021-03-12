# Problem description
A group of students are going on an excursion. The group members decide to split the costs of the trip so that, for example, one member pays for the bus tickets and another pays for the food. Your task is to create a program that asks for how much each member in the group has paid for the excursion costs, and then calculates how much each member should pay to or receive from others so that the costs would be distributed evenly.

The program does not have to check who has to pay or receive money from whom (this would make the program notably more complicated). It is only supposed to find out how much each group member has to pay to or receive from other members.

# Progression of the program
First, the program asks how many members there are in the group. If the user enters a number less than 2, the program should inform of an error and keep asking for a new value until the user enters a value that is greater than or equal to 2.

Next, the program asks for the amounts of money each member has paid for the trip. The user enters the expenses as decimal numbers. The program saves the values in a list so, that the sum paid by the first member is in the index 0, the sum paid by the second member in the index 1, and so on.

The program then calculates the total sum of the expenses, as well as the average of the expenses paid by the members (the total sum divided by the amount of group members) which should not be printed. After this, the program goes through the list and prints how much each member should pay or receive from other members. If a member's expenses are greater than or equal to the average, the program prints Participant no X should receive YY.YY eur., where X is the name of the group member and YY.YY the amount of money the other group members should pay them. If a member's expenses are less than the average, the program prints Participant no X should pay YY.YY eur.. Refer to the example runs below for details.
