# Project work for Week 1 CSE 111, calculating the tire volume then storing it to a file.

# Import math for the function of pi, and import datetime to get today's date for writing to a file.
import math
import datetime

# Get the user to input all of the relevant information for the calcuation
print()
print('All of the following inputs should be integers.')
print()
tire_width = int(input('Enter the width of the tire in mm (ex 205): '))
tire_ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
tire_diameter = int(input('Enter the diamater of the wheel in inches (ex 15): '))

# Calcuations to figure out the the volume
tire_volume = (math.pi * tire_width ** 2 * tire_ratio * (tire_width * tire_ratio + 2540 * tire_diameter)) / 10000000000

# Grabbing the current date to be appended to the file
current_date = datetime.date.today()

# Display the volume
print()
print(f'The approximate volume is {tire_volume:.2f} liters')
print()

# Setting up the tire price for a variety of different tires:
tire_price = 0.0
set_o_4_tires = 0.0
purchase_cost = 0.0

if tire_width == 265 and tire_ratio == 50 and tire_diameter == 19:
    tire_price = 379.99
    set_o_4_tires = 1519.96
elif tire_width == 205 and tire_ratio == 65 and tire_diameter == 16:
    tire_price = 184.99
    set_o_4_tires = 739.96
elif tire_width == 165 and tire_ratio == 65 and tire_diameter == 14:
    tire_price = 162.99
    set_o_4_tires = 651.96
elif tire_width == 305 and tire_ratio == 50 and tire_diameter == 20:
    tire_price = 376.99
    set_o_4_tires = 1507.96
else:
    tire_price = 215.99
    set_o_4_tires = 863.96

print(f"The cost of a single tire is ${tire_price}, or a set of 4 can be purchased for ${set_o_4_tires:,.2f}")
print()
# Asking if the customer would like to purchase the tires
purchase_tires = input('Would the customer like to purchase the tires? (Y/N) ').lower()

if purchase_tires == 'y':
    print()
    quantity_of_tires = int(input('How many tires would the customer like? '))
    purchase_cost = quantity_of_tires * tire_price
    print()
    print(f'The cost of this purchase, before tax, will be ${purchase_cost:,.2f}')
    print()
    cust_phone_number = input("What is the customer's phone number? ")
    print()

# Opening up the file to then write the data to the new file
with open('volumes.txt', 'at') as tire_volumes:
    # Initial attempt at writing the info to the file
    # print(tire_width, tire_ratio, tire_diameter, current_date, sep=", ", end='\n', flush=False)
    
    # If/Else to handle adding the customer phone number if they want to purchase the tire
    if purchase_tires == 'y':
        tire_volumes.write(f'{current_date}, {tire_width}, {tire_ratio}, {tire_diameter}, {tire_volume:.2f}, {cust_phone_number}, {purchase_cost:,.2f}\n')
    else:
        tire_volumes.write(f'{current_date}, {tire_width}, {tire_ratio}, {tire_diameter}, {tire_volume:.2f}\n')
