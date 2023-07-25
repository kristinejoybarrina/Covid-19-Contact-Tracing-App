from tkinter import *
from tkinter.font import Font


class AddContact:
    
    def add_contact_main():
        
        window = Tk()
        window.title("Trace Corona")
        window.geometry("1000x500")
        window.config(bg="#ECECEC")
        window.resizable(False, False)
        
        # Create a frame 
        frame = Frame(window, bg="#ffffff")
        frame.pack(expand=True, fill=BOTH)
        
        # Create a scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Create a canvas
        canvas = Canvas(frame, bg="#ffffff", yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)
        
        # Linked the scrollbar to canvas
        scrollbar.config(command=canvas.yview)
        
        # Create a frame inside the canvas for the contact information
        contact_frame = Frame(canvas, bg="#ffffff")
        contact_frame.pack(fill=BOTH, padx=50, pady=20)
        
        # Configure the canvas to scroll the contact frame
        canvas.create_window((0, 0), window=contact_frame, anchor="nw")
        contact_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))
        
        label_font = Font(family="Helvetica", size=15, weight="bold")
        
        # Create Labels
        window_label1 = Label(contact_frame, text="Contact Tracing Information", fg="black", font=label_font)
        window_label1.pack(anchor="w", padx=15, pady=20) 
        
        # Link to add contact name def
        AddContact.name(contact_frame)
        
        # Link to email def
        AddContact.email(contact_frame)
        
        # Link to phone number def
        AddContact.phone_number(contact_frame)
        
        # Link to phone number def
        AddContact.address(contact_frame)
        
    def name(frame):
        
        # first name textbox
        first_name = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        first_name.pack(anchor="w", padx=50, pady=5)
        first_label = Label(frame, text="First Name", fg="black")
        first_label.pack(anchor="w", padx=50, pady=5)
        
        # middle name textbox
        middle_name = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        middle_name.pack(anchor="w", padx=50, pady=5)
        middle_label = Label(frame, text="Middle Name", fg="black")
        middle_label.pack(anchor="w", padx=50, pady=5)
        
        # surname textbox
        surname = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        surname.pack(anchor="w", padx=50, pady=5)
        surname_label = Label(frame, text="Surname", fg="black")
        surname_label.pack(anchor="w", padx=50, pady=5)
        
        # suffix textbox
        suffix = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        suffix.pack(anchor="w", padx=50, pady=5)
        suffix_label = Label(frame, text="Suffix", fg="black")
        suffix_label.pack(anchor="w", padx=50, pady=5)
        
    def email(frame):
        
        # email textbox
        email = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        email.pack(anchor="w", padx=50, pady=5)
        email_label = Label(frame, text="Email", fg="black")
        email_label.pack(anchor="w", padx=50, pady=5) 
        
    def phone_number(frame):
        
        # phone number textbox
        phone_number = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        phone_number.pack(anchor="w", padx=50, pady=5)
        phone_number_label = Label(frame, text="Phone Number", fg="black")
        phone_number_label.pack(anchor="w", padx=50, pady=5) 
        
    def address(frame):
        
        # street address textbox
        street_address = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        street_address.pack(anchor="w", padx=80, pady=5)
        street_address_label = Label(frame, text="Street Address", fg="black")
        street_address_label.pack(anchor="w", padx=80, pady=5) 
 
        # city textbox
        city_address = Entry(frame, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        city_address.pack(anchor="w", padx=80, pady=5)
        city_address_label = Label(frame, text="City", fg="black")
        city_address_label.pack(anchor="w", padx=80, pady=5)