from tkinter import *
from tkinter.font import Font


class AddContact():
    
    def add_contact_main():
        
        window = Tk()
        window.title("Trace Corona")
        window.geometry("1000x500")
        window.config(bg="#f0f0f0")
        window.resizable(False,False)
        
        # Add scrollbar
        add_scrollbar = Scrollbar(window)
        add_scrollbar.pack(side=RIGHT, fill=Y)
        
        label_font = Font(family="Helvetica", size=15, weight="bold")
        
        # Create Labels
        window_label1 = Label(window, text="Contact Tracing Information", fg="black", font=label_font)
        window_label1.place(x=15, y=20) 
        
        # Link to add contact name def
        AddContact.name(window)
        
        # Link to email def
        AddContact.email(window)
        
        # Link to phone number def
        AddContact.phone_number(window)
        
    def name(window):
        
        # first name textbox
        first_name = Entry(window, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        first_name.place(x=50, y=100)
        first_label = Label(window, text="First Name", fg="black")
        first_label.place(x=50, y=70) 
        
        # middle name textbox
        middle_name = Entry(window, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        middle_name.place(x=50, y=155)
        middle_label = Label(window, text="Middle Name", fg="black")
        middle_label.place(x=50, y=130) 
        
        # surname textbox
        surname = Entry(window, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        surname.place(x=50, y=205)
        surname_label = Label(window, text="Surname", fg="black")
        surname_label.place(x=50, y=183) 
        
        # suffix textbox
        suffix = Entry(window, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        suffix.place(x=50, y=255)
        suffix_label = Label(window, text="Suffix", fg="black")
        suffix_label.place(x=50, y=233) 
        
    def email(window):
        
        # phone number textbox
        email = Entry(window, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        email.place(x=50, y=310)
        email_label = Label(window, text="Email", fg="black")
        email_label.place(x=50, y=285) 

    def phone_number(window):
        
        phone_number = Entry(window, fg="black", width=30, font=("Helvetica", 12), bg="#ECECEC")
        phone_number.place(x=50, y=365)
        phone_number_label = Label(window, text="Phone Number", fg="black")
        phone_number_label.place(x=50, y=340) 
        
 
        
        
        

    