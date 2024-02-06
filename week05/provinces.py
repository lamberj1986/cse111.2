import os

dir_path = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(dir_path, 'lprovinces.txt')

def main():
    dir_path = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(dir_path, 'provinces.txt')

        # Open a file named dentists.csv and store a reference
    # to the opened file in a variable named dentists_file.
    with open(filename, "rt") as provinces:

        alberta_count = 0
        provinces_list = []

        # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list.
        for line in provinces:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            provinces_list.append(clean_line)

            if clean_line == "AB":
                alberta_count += 1
        
    print(provinces_list)
    print()
    print(f"There were a total of {alberta_count} instances of 'AB'")

# Call main to start this program.
if __name__ == "__main__":
    main()