# Python Tkinter GUI based "LOVE CALCULATOR"

from tkinter import *
import random

# Creating GUI window
root = Tk()
root.geometry('400x240')
root.title('Love Calculator <3 <3')
root.configure(bg='#fff0f5')  # Light pink background

# Function to animate the result
def animate_result(score):
    result.config(text="Calculating", fg='deeppink')
    result.after(500, lambda: result.config(text="Calculating.", fg='deeppink'))
    result.after(1000, lambda: result.config(text="Calculating..", fg='deeppink'))
    result.after(1500, lambda: result.config(text="Calculating...", fg='deeppink'))
    result.after(2000, lambda: result.config(
        text=f" Love Percentage between both of You: {score}% ", fg='purple'))

# Function to calculate love percentage
def calculate_love():
    your_name = name1.get().strip()
    partner_name = name2.get().strip()
    
    if not your_name or not partner_name:
        result.config(text="Please enter both names!", fg='red')
        return

    combined = your_name.lower() + partner_name.lower()
    random.seed(combined)
    love_score = random.randint(40, 100)

    animate_result(love_score)

# Heading on Top
heading = Label(root, text='Love Calculator - Find how much your loved one is into u <3',
                font=('Helvetica', 10, 'bold'), bg='#fff0f5', fg='deeppink')
heading.pack(pady=5)

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:", font=('Helvetica', 10, 'bold'), bg='#fff0f5')
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:", font=('Helvetica', 10, 'bold'), bg='#fff0f5')
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

# Button to calculate
bt = Button(
    root,
    text="<3 Calculate <3",
    font=('Helvetica', 10, 'bold'),
    bg='hotpink',
    fg='white',
    height=1,
    width=18,
    command=calculate_love
)
bt.pack(pady=10)

# Result display
result = Label(root, text='Love Percentage between both of You', font=('Helvetica', 10), bg='#fff0f5', fg='purple')
result.pack(pady=5)

# Exit button
quit_btn = Button(root, text="Exit", font=('Helvetica', 9), command=root.quit)
quit_btn.pack(pady=5)

# Starting the GUI
root.mainloop()
