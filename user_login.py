from tkinter import *
from PIL import Image, ImageTk

class User_Login:

    def main():

        window = Tk()
        window.title("Trace Corona")
        window.geometry("1000x500")
        window.config(bg="white")
        window.resizable(False, False)

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

        window.mainloop()

    # Call main to start window
    main()

    def login():
        username = username_entry.get()