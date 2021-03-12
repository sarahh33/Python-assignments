import math


def calculate_cost(consumption, distance, gas_price, rent, time):
    money = math.ceil(time) * rent + gas_price * (consumption / 100) * distance
    return money


def main():
    gas_price = float(input("How much does gas cost (per litre)?\n"))
    rent = float(input("Enter the hourly rent for the big van:\n"))
    time = float(input("Enter the estimated rental time (hours) for the big van:\n"))

    distance = float(input("Enter estimated driving distance (km) for the big van:\n"))
    consumption = float(input("Enter fuel consumption (litres / 100 km) for the big van:\n"))
    bigvan = calculate_cost(consumption, distance, gas_price, rent, time)

    rent1 = float(input("Enter the hourly rent for the small van:\n"))
    time1 = float(input("Enter the estimated rental time (hours) for the small van:\n"))

    distance1 = float(input("Enter estimated driving distance (km) for the small van:\n"))
    consumption1 = float(input("Enter fuel consumption (litres / 100 km) for the small van:\n"))
    smallvan = calculate_cost(consumption1, distance1, gas_price, rent1, time1)
    print("Renting the bigger van would cost {:.2f} euros and renting the smaller van would cost {:.2f} euros.".format(
        bigvan, smallvan))
    if bigvan <= smallvan:
        print("You should rent the big van.")
    else:
        print("You should rent the small van.")


main()