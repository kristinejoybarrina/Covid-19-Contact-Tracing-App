# user_interface.py
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from add_contact import AddContact

class UserInterface:

    def main():
        
        window = Tk()
        window.title("Trace Corona")
        window.geometry("1000x500")
        window.config(bg="#f0f0f0")
        window.resizable(False, False)

        # Create icon logo window 
        image_icon = Image.open("icon.png")
        window.iconphoto(False, ImageTk.PhotoImage(image_icon))

        # Create Labels and Texts

        label_font = Font(family="Arial", size=15, weight="bold", slant="italic")
        label_font1 = Font(family="Arial", size=12, weight="bold")

        window_label1 = Label(window, text="Hello there,", fg="black", font=label_font)
        window_label1.place(x=760, y=20)

        window_label2 = Label(window, text="Citizen!", fg="black", bg="#75bee4", font=label_font)
        window_label2.place(x=880, y=45)

        window_label3 = Label(window, text="SELECT AN OPTION", fg="black", font=label_font1)
        window_label3.place(x=795, y=170)

        window_label4 = Label(window, text="____________________", fg="black", font=label_font1)
        window_label4.place(x=770, y=75)

        # Open the image from files
        image = Image.open("background.png")

        # Resize the image to fit the window proportionally
        window_width = 750
        window_height = 500
        image = image.resize((window_width, window_height), Image.ANTIALIAS)

        # Convert the image to a Tkinter-compatible object
        background = ImageTk.PhotoImage(image)

        # Create a label with the resized image in window
        label_background = Label(window, image=background, bg="white", bd=0, borderwidth=0, highlightthickness=0)
        label_background.place(x=0, y=0)

        # Link the add_contact button
        UserInterface.add_contact(window)

        # Link the search_contact button
        UserInterface.search_contact(window)

        # Link the exit_contact button
        UserInterface.exit_contact(window)

        window.mainloop()

    # Create add contact button 
    def add_contact(window):
        button_img = Image.open("add_contact_button.png")
        button_png = ImageTk.PhotoImage(button_img)
        add_button = Button(window, image=button_png, border=0, borderwidth=0, command=lambda: AddContact(window))
        add_button.image = button_png
        add_button.place(x=803, y=210)

    def check_if_working():
        print("ITS WORKINGGG!!")

    # Create add contact button 
    def search_contact(window):
        button_img = Image.open("search_contact_button.png")
        button_png = ImageTk.PhotoImage(button_img)

        search_button = Button(window, image=button_png, border=0, borderwidth=0, command=UserInterface.check_if_working)
        search_button.image = button_png
        search_button.place(x=785, y=280)

    # Create exit button 
    def exit_contact(window):
        button_img = Image.open("exit_button.png")
        button_png = ImageTk.PhotoImage(button_img)

        exit_button = Button(window, image=button_png, border=0, borderwidth=0, command=window.destroy)
        exit_button.image = button_png
        exit_button.place(x=810, y=350)
