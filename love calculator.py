# Python Tkinter GUI based "LOVE CALCULATOR"

# import tkinter
from tkinter import *
# import random module
import random
# Creating GUI window
root = Tk()
# Defining the container size, width=400, height=240
root.geometry('400x240')
# Title of the container
root.title('Love Calculator<3<3')

# Function to calculate love percentage
def calculate_love():
    # Get names from input fields and clean spaces
    your_name = name1.get().strip()
    partner_name = name2.get().strip()
    
	 # Basic validation
    if not your_name or not partner_name:
        result.config(text="Please enter both names!")
        return


    # Make calculation a bit more meaningful (not fully random)
    combined = your_name.lower() + partner_name.lower()
    random.seed(combined)  # Seed the random generator for consistency
    love_score = random.randint(40, 100)  # More flattering range
    result.config(text=f"Love Percentage: {love_score}% <3")

# Heading on Top
heading = Label(root, text='Love Calculator - Find how much your loved one is into u<3')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

# Button to calculate
bt = Button(root, text="Calculate", height=2, width=20, command=calculate_love)
bt.pack(pady=10)

# Result display 
result = Label(root, text='Love Percentage between both of You:')
result.pack()

# Optional: Exit button
quit_btn = Button(root, text="Exit", command=root.quit)
quit_btn.pack(pady=5)

# Starting the GUI
root.mainloop()