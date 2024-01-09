# Team activity for Week 1, give discount if today is Wednesday and the order total is over $50

import datetime

# This grabs today's date to then run through the rest of the program
todays_date = datetime.datetime.now()

# This will convert today's date into a day of the week, this returns a 1-7
# 1 = Monday and 7 = Sunday.

day_of_week = todays_date.strftime("%u")
# day_of_week = 2.00

print(f"Today's date is {todays_date} and the day of the week is {day_of_week}")

items_cost = float(input('What is the cost of items, before tax? '))

sub_total = 0.00
discount_total = 0.00

if items_cost >= 50 and (day_of_week == 2 or day_of_week == 3):
    sub_total = items_cost * 0.9
    discount_total = items_cost * 0.1
else:
    sub_total = items_cost

tax = sub_total * .06
total = sub_total + tax

if items_cost >= 50 and (day_of_week == 2 or day_of_week == 3):
    print()
    print(f'The original cost:  ${items_cost:.2f}')
    print(f'The discount is:    ${discount_total:.2f}')
    print()
    print(f'The sub total is:   ${sub_total:.2f}')
    print(f'The tax is:         ${tax:.2f}')
    print(f'The total bill is:  ${total:.2f}')
    print()
else: 
    print()
    print(f'The sub total is:   ${sub_total:.2f}')
    print(f'The tax is:         ${tax:.2f}')
    print(f'The total bill is:  ${total:.2f}')
    print()

