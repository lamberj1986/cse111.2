def main():
    # Get a chemical formula for a molecule from the user.
    user_formula = input("What is the chemical formula for your given molecule? ")

    # Call the make_known-dict function and
    # store the data in a variable.
    known_element_data = make_known_dict()

    # print(known_element_data)

    # Call the get_formula_name function to 
    # search for the formula in the known list
    common_name = get_formula_name(user_formula, known_element_data)
    
    # Print the known name if known.
    if common_name != 'none':
        print()
        print(f'The common name for your given formula is: {common_name}')

def make_known_dict():
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }

    return known_molecules_dict

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".

    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    if formula in known_molecules_dict:
        formula_name = known_molecules_dict[formula]
    else:
        formula_name = "none"

    return formula_name

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()