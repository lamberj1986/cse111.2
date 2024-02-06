import os
import csv

dir_path = os.path.dirname(os.path.abspath(__file__))

file_products = os.path.join(dir_path, 'products.csv')
file_request = os.path.join(dir_path, 'request.csv')

PRODUCT_NUMBER = 0
PRODUCT_NAME = 1
PRODUCT_PRICE = 2

RECEIPT_PRODUCT = 0
RECEIPT_QUANTITY = 1

def main():
    product_dict = {}

    products_dict = read_dictionary(file_products, PRODUCT_NUMBER)

    print(products_dict)

    with open(file_request, 'rt') as file:
        
        reader = csv.reader(file)
        values = []

        next(reader)

        print('Requested Items:')

        for row_list in reader:
            product_on_receipt = row_list[RECEIPT_PRODUCT]
            quantity_on_receipt = row_list[RECEIPT_QUANTITY]

            if product_on_receipt in products_dict:

                value = products_dict[product_on_receipt]
                product_name = value[PRODUCT_NAME]
                product_price = value[PRODUCT_PRICE]

                print(f'{product_name}: {quantity_on_receipt} @ {product_price}')

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