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

        self.__name_search_criteria = StringVar()
        self.__phone_search_criteria = StringVar()
        
        # Add the search bar and button for name search
        self.__name_search_label = Label(contact_frame, text="Search Name", fg="black", bg="#c3e7fd")
        self.__name_search_label.pack(anchor="w", padx=50, pady=15)
        self.__name_search_label = Label(contact_frame, text="First Name, Middle Name, Surname, Suffix", fg="black", bg="#c3e7fd")
        self.__name_search_label.pack(anchor="w", padx=50, pady=15)
        self.__name_search_entry = Entry(contact_frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff", textvariable=self.__name_search_criteria)
        self.__name_search_entry.pack(anchor="w", padx=50, pady=5)
        self.__name_search_button = Button(contact_frame, text="Search", command=self.search_contact_by_name)
        self.__name_search_button.pack(anchor="w", padx=50, pady=5)

        # Add the search bar and button for phone number search
        self.__phone_search_label = Label(contact_frame, text="Search Phone Number", fg="black", bg="#c3e7fd")
        self.__phone_search_label.pack(anchor="w", padx=50, pady=15)
        self.__phone_search_label = Label(contact_frame, text="Enter an 11-digits phone number starting with '09'", fg="black", bg="#c3e7fd")
        self.__phone_search_label.pack(anchor="w", padx=50, pady=15)
        self.__phone_search_entry = Entry(contact_frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff", textvariable=self.__phone_search_criteria)
        self.__phone_search_entry.pack(anchor="w", padx=50, pady=5)
        self.__phone_search_button = Button(contact_frame, text="Search", command=self.search_contact_by_phone_number)
        self.__phone_search_button.pack(anchor="w", padx=50, pady=5)
    
        self.__results_displayed = False
    

