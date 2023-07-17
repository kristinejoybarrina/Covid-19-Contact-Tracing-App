from tkinter import *
from tkinter.font import Font


class Add_Contact():
    
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
        
    