from tkinter import *
from tkinter.font import Font

#try if git bash is working

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
        title_label = Label(contact_frame, text="Contact Tracing Information", fg="black", font=label_font)
        title_label.pack(anchor="w", padx=15, pady=20) 
        
        personal_info_label = Label(contact_frame, text="Personal Contact Information", fg="black")
        personal_info_label.pack(anchor="w", padx=15, pady=20)
        
        # Link to add contact name def
        AddContact.name(contact_frame)
        
        # Link to email def
        AddContact.email(contact_frame)
        
        # Link to phone number def
        AddContact.phone_number(contact_frame)
        
        # Link to address def
        AddContact.address(contact_frame)
        
        # Link to emergency contact def
        AddContact.emergency_name(contact_frame)
        
        # Link to emergency contact def
        AddContact.condition_ques1(contact_frame)
        
        # Link to emergency contact def
        AddContact.condition_ques2(contact_frame)
        
    def name(frame):
        
        # first name textbox
        first_label = Label(frame, text="First Name", fg="black")
        first_label.pack(anchor="w", padx=50, pady=5)
        first_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        first_name.pack(anchor="w", padx=50, pady=5)
        
        # middle name textbox
        middle_label = Label(frame, text="Middle Name", fg="black")
        middle_label.pack(anchor="w", padx=50, pady=5)
        middle_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        middle_name.pack(anchor="w", padx=50, pady=5)

        # surname textbox
        surname_label = Label(frame, text="Surname", fg="black")
        surname_label.pack(anchor="w", padx=50, pady=5)
        surname = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        surname.pack(anchor="w", padx=50, pady=5)
        
        # suffix textbox
        suffix_label = Label(frame, text="Suffix", fg="black")
        suffix_label.pack(anchor="w", padx=50, pady=5)
        suffix = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        suffix.pack(anchor="w", padx=50, pady=5)

    def email(frame):
        
        # email textbox
        email_label = Label(frame, text="Email", fg="black")
        email_label.pack(anchor="w", padx=50, pady=5) 
        email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        email.pack(anchor="w", padx=50, pady=5)

    def phone_number(frame):
        
        # phone number textbox
        phone_number_label = Label(frame, text="Phone Number", fg="black")
        phone_number_label.pack(anchor="w", padx=50, pady=5) 
        phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        phone_number.pack(anchor="w", padx=50, pady=5)
        
    def address(frame):
        
        address_label = Label(frame, text="Address", fg="black")
        address_label.pack(anchor="w", padx=50, pady=15) 
        
        # street address textbox
        street_address_label = Label(frame, text="Street Address", fg="black")
        street_address_label.pack(anchor="w", padx=80, pady=5) 
        street_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        street_address.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        city_address_label = Label(frame, text="City", fg="black")
        city_address_label.pack(anchor="w", padx=80, pady=5)
        city_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        city_address.pack(anchor="w", padx=80, pady=5)

        # street address textbox
        province_label = Label(frame, text="Province", fg="black")
        province_label.pack(anchor="w", padx=80, pady=5) 
        province = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        province.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        postal_label = Label(frame, text="Postal/Zip Code", fg="black")
        postal_label.pack(anchor="w", padx=80, pady=5)
        postal = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        postal.pack(anchor="w", padx=80, pady=5)
        
    def emergency_name(frame):
        
        emergency_contact_label = Label(frame, text="Emergency Contact Information", fg="black")
        emergency_contact_label.pack(anchor="w", padx=15, pady=20) 
        
        # name textbox
        name_label = Label(frame, text="Name", fg="black")
        name_label.pack(anchor="w", padx=50, pady=5) 
        name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        name.pack(anchor="w", padx=50, pady=5)
 
        #  phone_number textbox
        phone_number_label = Label(frame, text="Phone Number", fg="black")
        phone_number_label.pack(anchor="w", padx=50, pady=5)
        phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        phone_number.pack(anchor="w", padx=50, pady=5)

        # email textbox
        email_label = Label(frame, text="Email", fg="black")
        email_label.pack(anchor="w", padx=50, pady=5) 
        email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        email.pack(anchor="w", padx=50, pady=5)
 
        # address textbox
        address_label = Label(frame, text="Address", fg="black")
        address_label.pack(anchor="w", padx=50, pady=5)
        address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        address.pack(anchor="w", padx=50, pady=5)
        
        # relationship textbox
        relationship_label = Label(frame, text="Relationship", fg="black")
        relationship_label.pack(anchor="w", padx=50, pady=5)
        relationship = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        relationship.pack(anchor="w", padx=50, pady=5)
        
    def condition_ques1(frame):
        
        radio1 = IntVar()

        # Have you recently tested covid-19 textbox
        quest1_label = Label(frame, text="Have you recently tested for Covid-19?", fg="black")
        quest1_label.pack(anchor="w", padx=50, pady=5)
        option1_label = Radiobutton(frame, text="Yes", variable=radio1, value=1)
        option1_label.pack(anchor="w", padx=50, pady=5)
        option2_label = Radiobutton(frame, text="No", variable=radio1, value=2)
        option2_label.pack(anchor="w", padx=50, pady=5)

    def condition_ques2(frame):
        
        radio2 = IntVar()

        # Are you recently exposed to someone with covid-19 textbox
        quest2_label = Label(frame, text="Are you recently exposed to someone with Covid-19?", fg="black")
        quest2_label.pack(anchor="w", padx=50, pady=5)
        option3_label = Radiobutton(frame, text="Yes", variable=radio2, value=1)
        option3_label.pack(anchor="w", padx=50, pady=5)
        option4_label = Radiobutton(frame, text="No", variable=radio2, value=2)
        option4_label.pack(anchor="w", padx=50, pady=5)

        
