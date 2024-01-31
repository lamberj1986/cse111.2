import random

def main():
    numbers = [16.2, 75.1, 52.3]

    print(numbers)

    append_random_numbers()

def append_random_numbers(numbers_list, quantity=1):
    quantity = random.uniform()

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()