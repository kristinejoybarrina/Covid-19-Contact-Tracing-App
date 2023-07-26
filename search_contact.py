from tkinter import *
from tkinter.font import Font

class SearchContact:

    def __init__(self, window):
        
        self.__window = window
        self.__window.title("Trace Corona")
        self.__window.geometry("1000x500")
        self.__window.config(bg="#c3e7fd")
        self.__window.resizable(False, False)
        
        # Create a frame 
        frame = Frame(window, bg="#c3e7fd")
        frame.pack(expand=True, fill=BOTH)
        
        # Create a scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Create a canvas
        canvas = Canvas(frame, bg="#c3e7fd", yscrollcommand=scrollbar.set)
        canvas.pack(side="left", expand=True, fill=BOTH)
        
        # Linked the scrollbar to canvas
        scrollbar.config(command=canvas.yview)
        
        # Create a frame inside the canvas for the contact information
        contact_frame = Frame(canvas, bg="#c3e7fd")
        contact_frame.pack(fill=BOTH, padx=1000, pady=1000)
        
        # Create a contact frame for arguments
        self.__contact_frame = contact_frame
        
        # Configure the canvas to scroll the contact frame
        canvas.create_window((0, 0), window=contact_frame, anchor="nw")
        contact_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))