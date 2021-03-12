SPECIFIC_HEAT_CAPACITY_ICE = 2.09 # specific heat capacity c for ice, unit kJ / (kg * °C)
SPECIFIC_HEAT_CAPACITY_WATER = 4.1819 # specific heat capacity c for water, unit kJ / (kg * °C)
SPECIFIC_HEAT_OF_FUSION_WATER = 333 # specific heat of fusion s, unit kJ / kg
SPECIFIC_HEAT_OF_VAPORIZATION_WATER = 2260 # specific heat of vaporization, unit kJ / kg

# Implement the function ice_cube_heating here
def ice_cube_heating(energy_total, mass, temp_init, end_temp):
    if temp_init < 0.0:
        if energy_total < mass * (end_temp-temp_init) * SPECIFIC_HEAT_CAPACITY_ICE:
            energy_remaining = 0.0
            end_temp = energy_total / mass / SPECIFIC_HEAT_CAPACITY_ICE + temp_init
        else:
            energy_remaining = energy_total - mass * (end_temp- temp_init) * SPECIFIC_HEAT_CAPACITY_ICE

    else:
        if energy_total < mass * (end_temp-temp_init) * SPECIFIC_HEAT_CAPACITY_WATER:
            energy_remaining = 0.0
            end_temp = energy_total / mass / SPECIFIC_HEAT_CAPACITY_WATER +temp_init
        else:
            energy_remaining = energy_total - mass * (end_temp - temp_init) * SPECIFIC_HEAT_CAPACITY_WATER

    return energy_remaining, end_temp
# Implement the function ice_cube_melting here
def ice_cube_melting(energy_remaining, mass):
    melted = False
    if energy_remaining >= mass * SPECIFIC_HEAT_OF_FUSION_WATER:
        melted = True
        energy_remaining = energy_remaining - mass* SPECIFIC_HEAT_OF_FUSION_WATER
    else:
        energy_remaining = 0.0
    return energy_remaining,melted
# Implement the function ice_cube_vaporization here
def ice_cube_vaporization(energy_remaining, mass):
    vaporized = False
    if energy_remaining < mass* SPECIFIC_HEAT_OF_VAPORIZATION_WATER:
        energy_remaining = 0.0
    else:
        vaporized= True
        energy_remaining = energy_remaining - mass * SPECIFIC_HEAT_OF_VAPORIZATION_WATER

    return energy_remaining, vaporized
def print_heating_result(energy_total, mass, temp_init, temp_end, melted, vaporized):
    print("With {:.2f} kJ, an ice cube weighing {:.2f} kg heats from {:.2f} °C to {:.2f} °C."
          .format(energy_total, mass, temp_init, temp_end))
    if not melted and not vaporized:
        print("The ice cube stays solid.")
    elif melted and not vaporized:
        print("The ice cube has melted into fluid water.")
    else:
        print("The ice cube has vaporized and is now water vapor.")

def main():
    print("Welcome to the ice cube simulator! I will tell you stats about heating your ice cube.")
    mass = float(input("What is the mass of the ice cube (in kg)?\n"))
    while mass <= 0.0:
        print("Mass cannot be zero or negative!")
        mass = float(input("What is the mass of the ice cube?\n"))
    temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    while temp_init < -273.15 or temp_init > 0.0:
        print("The ice cube's temperature can't be under the absolute zero or above 0 degrees!")
        temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))
    while energy_total < 0.0:
        print("Energy cannot be negative!")
        energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))

    melted = False
    vaporized = False
    energy_remaining, end_temp = ice_cube_heating(energy_total, mass, temp_init, 0.0)
    if energy_remaining != 0.0:
        energy_remaining, melted = ice_cube_melting(energy_remaining, mass)
        if energy_remaining != 0.0:
            energy_remaining, end_temp = ice_cube_heating(energy_remaining, mass, 0.0, 100.0)
            if energy_remaining != 0.0:
                energy_remaining, vaporized = ice_cube_vaporization(energy_remaining, mass)

    print_heating_result(energy_total, mass, temp_init, end_temp, melted, vaporized)

main()