# Import the datetime class from the datetime module so that it can be used in this program.
from datetime import datetime
from datetime import date

# Import the os module to get the directory path setup, this keeps the program system agnostic.
import os

# Import the csv module to read the files associated with this program.
import csv

# Using the os module, grab the directory path of this file.
dir_path = os.path.dirname(os.path.abspath(__file__))

# Append the directory path to the two csv files that will be used in this program.
file_products = os.path.join(dir_path, 'products.csv')
file_request = os.path.join(dir_path, 'request.csv')

# Defining the index numbers for the product csv file.
PRODUCT_NUMBER = 0
PRODUCT_NAME = 1
PRODUCT_PRICE = 2

# Defining the index numbers for the receipt csv file.
RECEIPT_PRODUCT = 0
RECEIPT_QUANTITY = 1

# Defining the tax rate for the remainder of the program.
TAX_RATE = 0.06

# Using a variable for the store name in case it ever changes.
STORE_NAME = 'Spanish Inquisition Foods'

def main():
    try:
        products_dict = {}

        products_dict = read_dictionary(file_products, PRODUCT_NUMBER)

        # print(products_dict)

        sub_total = 0.0
        product_count = 0
        tax = 0.0
        total = 0.0

        print()
        print(STORE_NAME)
        print()

        with open(file_request, 'rt') as file:
        
            reader = csv.reader(file)
            values = []

            next(reader)

            for row_list in reader:

                product_on_receipt = row_list[RECEIPT_PRODUCT]
                quantity_on_receipt = int(row_list[RECEIPT_QUANTITY])

                # if product_on_receipt in products_dict:

                value = products_dict[product_on_receipt]
                product_name = value[PRODUCT_NAME]
                product_price = float(value[PRODUCT_PRICE])

                print(f'{product_name}: {quantity_on_receipt} @ {product_price}')

                sub_total += product_price * quantity_on_receipt
                product_count += quantity_on_receipt

        today = date.today()
        discount = 1.0

        if today.weekday() == 1 or today.weekday() == 2:
            discount = 0.9

        sub_total = sub_total * discount
        tax = sub_total * TAX_RATE
        total = sub_total + tax
        
        print()
        print(f'Number of items: {product_count}')
        print(f'Subtotal: {sub_total:.2f}')
        print(f'Sales Tax: {tax:.2f}')
        print(f'Total: {total:.2f}')

        print()
        print(f'Thank you for shopping at the {STORE_NAME}.')

        if today.weekday() == 1:
            savings = sub_total * (1 - discount)
            print(f'Thank you for shopping on discount Tuesday, you saved ${savings:.2f}')
        elif today.weekday() == 2:
            savings = sub_total * (1 - discount)
            print(f'Thank you for shopping on discount Wednesday, you saved ${savings:.2f}')

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
        print()

    except KeyError as key_error:
        print('ERROR: unknown product ID in the request.csv file')
        print(key_error)
    except FileNotFoundError as file_error:
        print('ERROR: missing file')
        print(file_error)

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    # Create a new dictionary that will be returned after the file is read into it
    dictionary = {}

    # Open the CSV file for reading and store a reference to the opened file
    # as file.
    with open(filename, 'rt') as file:
        
        # Using the csv module to create a new object from the opened csv file
        reader = csv.reader(file)
        
        # Skip the first row of the CSV file as it contains header information
        next(reader)

        # Read the rows of the CSV file one at a time. 
        for row_list in reader:

            # If the current row is not blank, then add it to the dictionary
            if len(row_list) != 0:

                # From the current row, pull the data from the column that contains
                # the key.
                key = row_list[key_column_index]

                # Store the data from the current row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary
    return dictionary

# If this file was executed like this: > python teach_solution.py
# then call the main function. However, if this file was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()