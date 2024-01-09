# Project work for Week 1 CSE 111, calculating the tire volume

import math

# Get the user to input all of the relevant information for the calcuation
print()
print('All of the following inputs should be integers.')
tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
tire_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
tire_diameter = int(input('Enter the diamater of the wheel in inches (ex 15): '))

# Calcuations to figure out the the volume

tire_volume = (math.pi * tire_width ** 2 * tire_ratio * (tire_width * tire_ratio + 2540 * tire_diameter)) / 10000000000

# Display the volume
print()
print(f'The approximate volume is {tire_volume:.2f} liters')
print()