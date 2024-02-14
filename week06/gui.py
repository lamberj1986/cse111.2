import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()
    root.configure(background = "green")
    
    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of Your Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()
    

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_radius = Label(frm_main, text="The Circle's Radius: ")

    # Create an integer entry box where the user will enter the radius of your circle.
    ent_rad = IntEntry(frm_main, width=4, lower_bound=20, upper_bound=90)

    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Circle's Area:")

    # Create labels that will display the results.
    lbl_area_num = Label(frm_main, width=15) 

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    ent_rad.grid(      row=0, column=1, padx=3, pady=3)
    
    lbl_area.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_area_num.grid(      row=1, column=1, padx=25, pady=25)
    

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    

    def find_area(event):

        try:
            radius = ent_rad.get()
            area_circle = math.pi * (radius ** 2)

            lbl_area_num.config(text=f"{area_circle:.2f}") 

        except ValueError: 
            lbl_area_num.config(" ")
    
    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_rad.clear()
        lbl_area_num.config(text="")
        ent_rad.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_rad.bind("<KeyRelease>", find_area)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_rad.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()




