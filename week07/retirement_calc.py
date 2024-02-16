import math

actions = ['Calculate Future Value', 'Calculate Projected Shortfall', 'Calculate Projected Retirement Spend', 'Calculate Monthly Savings Need', 'Exit']

def main():
    action_choice = True

    while action_choice:

        # This section iterates through the menu creation, 
        # it is written this way to allow for future expansion
        print()
        print('Please select one of the following: ')
        for i in range(len(actions)):
            action = actions[i]
            action_index = i + 1
            print(f'{action_index}. {action}')
        print()

        action_choice = input('Please enter an action: ')

        if action_choice == '1': # Calculate future value
            
            future_value = 0.0

            # Collect necessary information for calculations
            current_age = int(input('What is your current age? (in whole years) '))
            retire_age = int(input('At what age do you want to retire? (in whole years) '))
            current_value = float(input('What is the current value of your retirement accounts? $'))
            
            # Checking to see if the user knows their rate of return
            rate_of_return_known = input('Do you know your estimated annual rate of return? (Y/N) ')
            rate_of_return_known = rate_of_return_known.lower()
            
            if rate_of_return_known == 'y': # If the rate of return is known, add it into the calculation
                rate_of_return = float(input('What is your annual rate of return? '))
                
                if rate_of_return > 1: # Converting the rate of return if the user gives a whole number. 
                                       # Calculations need to be a decimal to work.
                    rate_of_return = rate_of_return / 100
            
                future_value = get_future_value(current_age, retire_age, current_value, rate_of_return)

            else: # If the rate of return is not known, use the default
                future_value = get_future_value(current_age, retire_age, current_value)

            print()
            print(f'The projected future value of your retirement accounts is ${future_value:,.2f}')


        elif action_choice == '2': # Calcualte projected shortfall
            projected_shortfall = 0.0

            # Collect necessary information for calculations
            current_age = int(input('What is your current age? (in whole years) '))
            retire_age = int(input('At what age do you want to retire? (in whole years) '))
            current_value = float(input('What is the current value of your retirement accounts? $'))
            monthly_spend = float(input('What is your projected monthly spend while retired? $'))

            projected_shortfall = calculate_current_shortfall(current_age, retire_age, current_value, monthly_spend)

            print()
            if projected_shortfall <= 0:
                projected_shortfall = -1 * projected_shortfall
                print(f'Congrats! You have a projected excess of ${projected_shortfall:,.2f}')
            else:
                print(f'Unfortunately, you will have a projected shortfall at the beginning of retirement of ${projected_shortfall:,.2f}')
                print()
                calc_extra_save = input('Would you like to calculate your projected monthly savings need to hit your goals? (Y/N) ').lower()

                if calc_extra_save == 'y':
                    future_value = get_future_value(current_age, retire_age, current_value)
                    extra_deposit = calculate_monthly_deposit(current_age, retire_age, future_value)

                    print()
                    print(f'To reach your goal, it is estimated that you need to save an additional ${extra_deposit:,.2f} each month to meet your retirement goals.')

        elif action_choice == '3': # Calculate projected spend
            projected_spend = 0.0

            future_value = float(input('What is the projecte future value of your retirement savings? $'))

            projected_spend = calculate_projected_spend(future_value)

            print()
            print(f'Your projected monthly spend in retirement is ${projected_spend:,.2f} each month.')
            print()

        elif action_choice == '4': # Calculate necessary monthly save
            savings_need = 0.0

            # Collect necessary information for calculations
            current_age = int(input('What is your current age? (in whole years) '))
            retire_age = int(input('At what age do you want to retire? (in whole years) '))
            future_value = float(input('What is the future value of your retirement accounts? $'))
            
            # Checking to see if the user knows their rate of return
            rate_of_return_known = input('Do you know your estimated annual rate of return? (Y/N) ')
            rate_of_return_known = rate_of_return_known.lower()
            
            if rate_of_return_known == 'y': # If the rate of return is known, add it into the calculation
                rate_of_return = float(input('What is your annual rate of return? '))
                
                if rate_of_return > 1: # Converting the rate of return if the user gives a whole number. 
                                       # Calculations need to be a decimal to work.
                    rate_of_return = rate_of_return / 100
            
                savings_need = calculate_monthly_deposit(current_age, retire_age, current_value, rate_of_return)

            else: # If the rate of return is not known, use the default
                savings_need = calculate_monthly_deposit(current_age, retire_age, current_value)

            print()
            print(f'To reach your desired goals, you will need to save at least ${savings_need:,.2f} each month.')
            print()

        elif action_choice == '5': # Exit program
            print()
            print('Thank you for using this calculator.')
            print()

            action_choice = False

        else: # Catch for misformatted input, either a number larger than menu options or string
            print()
            print('Please select from one of the menu options above.')

def get_future_value(current_age, retire_age, current_value, annual_return=0.06):
    """Calculate the future value of the investment, assuming no additional deposits.
    Will assume an annual rate of return of 6%, based on current portfolio theory, unless
    a different RoR is provided.

    Parameter
        current_age: The current age of the person in question
        retire_age: The projected age of retirement
        current_value: The current value of any retirement accounts
        annual_return: The annual rate of return for the current investments,
                        will default to 6% unless another value is provided.
    Return: future_value is returned as a calculated value
    """
    years_to_retire = retire_age - current_age

    # The previous calculation that I used to get this value, before using the math.pow():
    #       future_value = current_value * ((1 + annual_return) ** years_to_retire)
    
    future_value = current_value * math.pow(1 + annual_return, years_to_retire)

    return future_value

def calculate_current_shortfall(current_age, retire_age, current_value, desired_monthly_retirement_spend):
    """Calculate the current shortfall of investments. This calculation will take the 
    projected future value of the account and remove that from their projected need in retirement.

    Parameter
        current_age: The current age of the person in question
        retire_age: The projected age of retirement
        current_value: The current value of any retirement accounts
        desired_minthly_retirement_spend: The estimated montly spend that will be needed in retirement
    Return: shortfall is returned, if it is negative there is a shortfall otherwise its an excess
    """

    future_value = get_future_value(current_age, retire_age, current_value)
    
    future_need = calculate_projected_need(desired_monthly_retirement_spend)

    shortfall = future_need - future_value

    return shortfall

def calculate_projected_spend(future_value):
    """Calculate the projected monthly spend for a given future value on a balance.
    This is calculated by assuming an average of 25 years in retirement. 

    Parameter
        future_value: The projected future value of a given retirement account
    Return: monthly_max_spend is returned, this will show how much a person can spend each month in retirement
    """

    years_in_retirement = 25 # This is a general assumption in retirement planning

    monthly_max_spend = future_value / (years_in_retirement * 12)

    return monthly_max_spend

def calculate_projected_need(future_monthly_spend):
    """Calculate the projected need in future dollars needed for their retirement.
    Calculated using the assumption of a person being retired for 25 years.

    Parameter
        future_monthly_spend: The projected amount that will be spent in retirement each month.
    Return: future_need is returned
    """

    years_in_retirement = 25 # This is a general assumption in retirement planning

    future_need = future_monthly_spend * years_in_retirement * 12

    return future_need

def calculate_monthly_deposit(current_age, retire_age, future_value, annual_return=0.06):
    """Calculate the projected monthly deposits needed to reach a given retirment value.

    Parameter
        current_age: The current age of the person in question
        retire_age: The projected age of retirement
        future_value: The amount needed in future dollars for retiement
        annual_return: The annual rate of return for the current investments,
                        will default to 6% unless another value is provided.
    Return: monthly_save_amount is returned
    """

    # Formula for this is fairly complex, but in summmary it can be put as:
    # 
    # A = (PMT * ((1 + r / n) ^ (n * t) - 1)) / (r / n)
    # 
    # A = Desired future balance of the account
    # PMT = Required payment
    # r = Annual rate of return, for these calculations we will assume 6%
    # n = Number of compounding events in a given year, here we will assume thie to be 12
    # t = Number of years that we can save
    #
    # To find the monthly payment we will use the following formula:
    #
    # PMT = (A * (r / n)) / ((1 + r / n) ^ (n * t) - 1)

    years_to_retire = retire_age - current_age

    # For some reason the following line of code didn't want to work for me,
    # my guess is that it has something to do with the ** function.
    # I have commnted it out and broken out the denominator to ge things to work.
    # monthly_payment_need = (future_value * (annual_return / 12)) 
    #                         / ((1 + (annual_return / 12) ** (12 * years_to_retire) - 1))
    
    part_one = 1 + (annual_return / 12) # First half of the denominator
    part_two = (12 * years_to_retire) - 1 # Second hald of the denominator

    # The previous calculation used to create the denominator, replaced with math.pow():
    #       denominator = part_one ** part_two
    # denominator = math.pow(part_one, part_two) # Creating the denominator

    monthly_payment_need = (future_value * (annual_return / 12)) / math.pow(part_one, part_two) 

    return monthly_payment_need

# If this file was executed like this:
# > python retirement_calc.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()