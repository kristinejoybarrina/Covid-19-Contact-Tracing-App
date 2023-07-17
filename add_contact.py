from tkinter import *
from tkinter.font import Font


class AddContact():
    
    def add_contact_main():
        window = Tk()
        window.title("Trace Corona")
        window.geometry("1000x500")
        window.config(bg="#f0f0f0")
        window.resizable(False,False)
        
        label_font = Font(family="Helvetica", size=15, weight="bold")
        
        # Create Labels
        window_label1 = Label(window, text="Contact Tracing Information", fg="black", font=label_font)
        window_label1.place(x=15, y=20) 
        
        AddContact.name(window)
        
        
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
        
        
    
    