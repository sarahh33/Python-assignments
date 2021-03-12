# Problem description
Monty Hall problem is a famous puzzle related to probability calculus. The problem is based on a tv-show called Let's make a deal that was hosted by Monty Hall. In Monty Hall problem, three doors are presented to the player and one of the doors hides a price car behind it while the other doors hide goats. The player must choose one of the doors. After the players decision, the host opens one door out of the two doors left. There is always a goat behind the door the host opens. At this point, the player must choose whether they want to keep the door they originally chose or change their decision to the other door left. If the player chooses a door with the car behind it, they win the game and get to keep the car.

The problem is interesting because (against the intuition of many) the probability of winning increases if the player decides to change their original decision to the opther door left. If there are more than three doors, the probability to win by changing the door increases even more.
# Examples
Set seed:\
42\
How many doors?\
10\
 _   _   _   _   _   _   _   _   _   _  \
| | | | | | | | | | | | | | | | | | | | \
|_| |_| |_| |_| |_| |_| |_| |_| |_| |_| \
 1   2   3   4   5   6   7   8   9  10  \
Choose a door 1-10.\
4\
You chose the door number 4.\
...\
 _   _   _   _   _   _   _   _   _   _  \
|G| | | |G| | | |G| |G| |G| |G| |G| |G| \
|_| |_| |_| |_| |_| |_| |_| |_| |_| |_| \
 1   2   3   4   5   6   7   8   9  10  \
8 certainly wrong doors were opened. The door number 2 was left.\
Choose 4 if you want to keep the door you first chose and choose 2 if you want to change the door.\
2\
 _   _   _   _   _   _   _   _   _   _  \
|G| |C| |G| |G| |G| |G| |G| |G| |G| |G| \
|_| |_| |_| |_| |_| |_| |_| |_| |_| |_| \
 1   2   3   4   5   6   7   8   9  10  \
Congratulations! The car was behind the door you chose!\
