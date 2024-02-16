def calculate_monthly_deposit(current_age, retire_age, future_value, annual_return=0.06):
    years_to_retire = retire_age - current_age

    denominator = ((1 + (annual_return / 12) ** (12 * years_to_retire) - 1))
    
    print()
    print(denominator)
    print()
    
    part_one = (1 + (annual_return / 12))
                
    print()
    print(part_one)
    print()

    part_two = (12 * years_to_retire) - 1

    print()
    print(part_two)
    print()

    combo = part_one ** part_two

    print()
    print(combo)
    print()

    month_test = (future_value * (annual_return / 12))/ combo

    print()
    print(month_test)
    print()

    

    return month_test

def main():
    retire = 70
    current = 35
    future = 750000
    ror = 0.08

    print(calculate_monthly_deposit(current, retire, future, ror))

if __name__ == "__main__":
    main()