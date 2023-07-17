from tkinter import *
from PIL import Image, ImageTk

class User_Interface:

    def main():
        
        window = Tk()
        window.title("Trace Corona")
        window.geometry("1000x500")
        window.config(bg="white")
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
        label_background = Label(window, image=background, bg="white")
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
        
        add_button = Button(window, text="ADD CONTACT")
        add_button.place(x=835, y=200)
        
    # Create add contact button 
    def search_contact(window):
        
        search_button = Button(window, text="SEARCH CONTACT")
        search_button.place(x=823, y=250) 
    
    # Create exit button 
    def exit_contact(window):
        search_button = Button(window, text="EXIT", command=window.destroy)
        search_button.place(x=860, y=300) 



        