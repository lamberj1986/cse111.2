import random

def main():
    numbers = []

    print(numbers)

    append_random_numbers(numbers)

    print()
    print(numbers)

    append_random_numbers(numbers, 3)

    print()
    print(numbers)

def append_random_numbers(numbers_list, quantity=1):
    i = 0
    while i < quantity:
        i += 1
        new_number = random.uniform(0,100)
        new_number = round(new_number, 1)
        numbers_list.append(new_number)

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()