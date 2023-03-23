from tkinter import *

# Create a new window
window = Tk()
window.title("Broker Login Portal")

# Set the background color to black
window.configure(background="black")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y positions for centering the window
x = (screen_width // 2) - (400 // 2) # 400 is the width of the window
y = (screen_height // 2) - (400 // 2) + 200 # 400 is the height of the window and 200 is the offset

# Set the window to be centered and shifted downwards
window.geometry('400x400+{}+{}'.format(x, y))

# Set the logo image
logo = PhotoImage(file="new_logo.png").subsample(3)
logo_label = Label(window, image=logo, bg="black")
logo_label.pack(pady=20)

# Create the login form
form_frame = Frame(window, bg="black")

# Broker ID field
broker_id_label = Label(form_frame, text="Broker ID:", bg="black", fg="white")
broker_id_label.pack(side=TOP)

broker_id_entry = Entry(form_frame)
broker_id_entry.pack(side=TOP, padx=5)

# Password field
password_label = Label(form_frame, text="Password:", bg="black", fg="white")
password_label.pack(side=TOP)

password_entry = Entry(form_frame, show="*")
password_entry.pack(side=TOP, padx=5)

# Login button
login_button = Button(form_frame, text="Login", bg="white", fg="black", font=("Arial", 14))
login_button.pack(pady=15)

# Pack the login form
form_frame.pack(pady=40)

# Forgot password link
forgot_password_label = Label(window, text="Forgot password?", bg="black", fg="white")
forgot_password_label.pack()

# Contact us link
contact_us_label = Label(window, text="If you don't have a Broker ID, please contact us to get one.", bg="black", fg="white")
contact_us_label.pack(pady=10)

# Copyright information
copyright_label = Label(window, text="Copyright © 2023", bg="black", fg="white")
copyright_label.pack()

# Run the window
window.mainloop()