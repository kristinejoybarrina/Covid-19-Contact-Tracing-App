from tkinter import *
from PIL import Image, ImageTk

class User_Interface:

    def main():
        
        window = Tk()
        window.title("Trace Corona")
        window.geometry("1000x500")
        window.config(bg="#f0f0f0")
        window.resizable(False,False)

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
        label_background.place(x=-2, y=-2)

        # Link the add_contact button
        User_Interface.add_contact(window)
        
        # Link the search_contact button
        User_Interface.search_contact(window)
        
        # Link the exit_contact button
        User_Interface.exit_contact(window)

        window.mainloop()

    # Create add contact button 
    def add_contact(window):
        
        button_img = Image.open("add_contact_button.png")
        button_png = ImageTk.PhotoImage(button_img)

        
        add_button = Button(window, image=button_png, border=0, borderwidth=0, command=User_Interface.check_if_working,)
        add_button.image = button_png
        add_button.place(x=803, y=180)
        
    def check_if_working():
        print ("ITS WORKINGGG!!")
        
    # Create add contact button 
    def search_contact(window):

        button_img = Image.open("search_contact_button.png")
        button_png = ImageTk.PhotoImage(button_img)

        search_button = Button(window, image=button_png, border=0, borderwidth=0, command=User_Interface.check_if_working,)
        search_button.image = button_png
        search_button.place(x=785, y=250) 
    
    # Create exit button 
    def exit_contact(window):
        
        button_img = Image.open("exit_button.png")
        button_png = ImageTk.PhotoImage(button_img)

        exit_button = Button(window, image=button_png, border=0, borderwidth=0, command=window.destroy)
        exit_button.image = button_png
        exit_button.place(x=810, y=320) 
        
    
        
        




        