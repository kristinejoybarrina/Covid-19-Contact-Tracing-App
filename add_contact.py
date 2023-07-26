from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk


class AddContact:
    
    def __init__(self, window):

        self.__window = window
        self.__window.title("Trace Corona")
        self.__window.geometry("1000x500")
        self.__window.config(bg="#ECECEC")
        self.__window.resizable(False, False)
        
        # Create a frame 
        frame = Frame(window, bg="#ffffff")
        frame.pack(expand=True, fill=BOTH)
        
        # Create a scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Create a canvas
        canvas = Canvas(frame, bg="#ffffff", yscrollcommand=scrollbar.set)
        canvas.pack(side="left", expand=True, fill=BOTH)
        
        # Linked the scrollbar to canvas
        scrollbar.config(command=canvas.yview)
        
        # Create a frame inside the canvas for the contact information
        contact_frame = Frame(canvas, bg="#ffffff")
        contact_frame.pack(fill=BOTH, padx=1000, pady=1000)
        
        # Create a contact frame for arguments
        self.__contact_frame = contact_frame
        
        # Configure the canvas to scroll the contact frame
        canvas.create_window((0, 0), window=contact_frame, anchor="nw")
        contact_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))
        
        # Base format of label
        label_font = Font(family="Helvetica", size=15, weight="bold")
        
        # Create Labels
        title_label = Label(contact_frame, text="Contact Tracing Information", fg="black", font=label_font)
        title_label.pack(anchor="w", padx=100, pady=20) 
        
        personal_info_label = Label(contact_frame, text="Personal Contact Information", fg="black")
        personal_info_label.pack(anchor="w", padx=15, pady=20)
        
        # Link to def functions
        self.name(contact_frame)
        self.address(contact_frame)
        self.email(contact_frame)
        self.phone_number(contact_frame)
        self.emergency_name(contact_frame)
        self.emergency_phone(contact_frame)
        self.emergency_email(contact_frame)
        self.emergency_address(contact_frame)
        self.emergency_relationship(contact_frame)
        self.condition_ques1(contact_frame)
        self.condition_ques2(contact_frame)

        # Submit button
        submit_button = Button(contact_frame, text="Submit", command=self.submit_data)
        submit_button.pack(anchor="w", padx=50, pady=20)


    def name(self, frame):
        
        self.__name_label = Label(frame, text="Name", fg="black")
        self.__name_label.pack(anchor="w", padx=50, pady=15) 
        
        # first name textbox
        self.__first_label = Label(frame, text="First Name", fg="black")
        self.__first_label.pack(anchor="w", padx=80, pady=5)
        self.__first_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__first_name.pack(anchor="w", padx=80, pady=5)
        
        # middle name textbox
        self.__middle_label = Label(frame, text="Middle Name", fg="black")
        self.__middle_label.pack(anchor="w", padx=80, pady=5)
        self.__middle_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__middle_name.pack(anchor="w", padx=80, pady=5)

        # surname textbox
        self.__surname_label = Label(frame, text="Surname", fg="black")
        self.__surname_label.pack(anchor="w", padx=80, pady=5)
        self.__surname = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__surname.pack(anchor="w", padx=80, pady=5)
        
        # suffix textbox
        self.__suffix_label = Label(frame, text="Suffix", fg="black")
        self.__suffix_label.pack(anchor="w", padx=80, pady=5)
        self.__suffix = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__suffix.pack(anchor="w", padx=80, pady=5)

    def email(self, frame):
        
        # email textbox
        self.__email_label = Label(frame, text="Email", fg="black")
        self.__email_label.pack(anchor="w", padx=50, pady=15) 
        self.__email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__email.pack(anchor="w", padx=50, pady=5)

    def phone_number(self, frame):
        
        # phone number textbox
        self.__phone_number_label = Label(frame, text="Phone Number", fg="black")
        self.__phone_number_label.pack(anchor="w", padx=50, pady=15) 
        self.__phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__phone_number.pack(anchor="w", padx=50, pady=5)
        
    def address(self, frame):
        
        self.__address_label = Label(frame, text="Address", fg="black")
        self.__address_label.pack(anchor="w", padx=50, pady=15) 
        
        # street address textbox
        self.__street_address_label = Label(frame, text="Street Address", fg="black")
        self.__street_address_label.pack(anchor="w", padx=80, pady=5) 
        self.__street_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__street_address.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        self.__city_address_label = Label(frame, text="City", fg="black")
        self.__city_address_label.pack(anchor="w", padx=80, pady=5)
        self.__city_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__city_address.pack(anchor="w", padx=80, pady=5)

        # street address textbox
        self.__province_label = Label(frame, text="Province", fg="black")
        self.__province_label.pack(anchor="w", padx=80, pady=5) 
        self.__province = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__province.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        self.__postal_label = Label(frame, text="Postal/Zip Code", fg="black")
        self.__postal_label.pack(anchor="w", padx=80, pady=5)
        self.__postal = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__postal.pack(anchor="w", padx=80, pady=5)
        
    def emergency_name(self, frame):
        
        self.__emergency_contact_label = Label(frame, text="Emergency Contact Information", fg="black")
        self.__emergency_contact_label.pack(anchor="w", padx=15, pady=25) 
        
        # name textbox
        self.__name_label = Label(frame, text="Name", fg="black")
        self.__name_label.pack(anchor="w", padx=50, pady=15) 
        self.__emergency_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__emergency_name.pack(anchor="w", padx=50, pady=5)
 
    def emergency_phone(self, frame):
         
        #  phone_number textbox
        self.__phone_number_label = Label(frame, text="Phone Number", fg="black")
        self.__phone_number_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__emergency_phone_number.pack(anchor="w", padx=50, pady=5)

    def emergency_email(self, frame):
        # email textbox
        self.__email_label = Label(frame, text="Email", fg="black")
        self.__email_label.pack(anchor="w", padx=50, pady=15) 
        self.__emergency_email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__emergency_email.pack(anchor="w", padx=50, pady=5)
 
    def emergency_address(self, frame):
        # address textbox
        self.__address_label = Label(frame, text="Address", fg="black")
        self.__address_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__emergency_address.pack(anchor="w", padx=50, pady=5)
    
    def emergency_relationship(self, frame):
        # relationship textbox
        self.__relationship_label = Label(frame, text="Relationship", fg="black")
        self.__relationship_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_relationship = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#ECECEC")
        self.__emergency_relationship.pack(anchor="w", padx=50, pady=5)
        
    def condition_ques1(self, frame):
        
        self.__radio1 = IntVar()

        # Have you recently tested covid-19 textbox
        self.__quest1_label = Label(frame, text="Have you recently tested for Covid-19?", fg="black")
        self.__quest1_label.pack(anchor="w", padx=50, pady=15)
        self.__option1_label = Radiobutton(frame, text="Yes", variable=self.__radio1, value=1)
        self.__option1_label.pack(anchor="w", padx=50, pady=5)
        self.__option2_label = Radiobutton(frame, text="No", variable=self.__radio1, value=0)
        self.__option2_label.pack(anchor="w", padx=50, pady=5)
        
    def condition_ques2(self, frame):
        
        self.__radio2 = IntVar()

        # Are you recently exposed to someone with covid-19 textbox
        self.__quest2_label = Label(frame, text="Are you recently exposed to someone with Covid-19?", fg="black")
        self.__quest2_label.pack(anchor="w", padx=50, pady=15)
        self.__option3_label = Radiobutton(frame, text="Yes", variable=self.__radio2, value=1)
        self.__option3_label.pack(anchor="w", padx=50, pady=5)
        self.__option4_label = Radiobutton(frame, text="No", variable=self.__radio2, value=0)
        self.__option4_label.pack(anchor="w", padx=50, pady=5)

    def submit_data(self):
        # Get values from entry buttons
        first_name_value = self.__first_name.get()
        middle_name_value = self.__middle_name.get()
        surname_value = self.__surname.get()
        suffix_value = self.__suffix.get()
        email_value = self.__email.get()
        phone_number_value = self.__phone_number.get()
        street_address_value = self.__street_address.get()
        city_address_value = self.__city_address.get()
        province_value = self.__province.get()
        postal_value = self.__postal.get()
        emergency_name_value = self.__emergency_name.get()
        emergency_phone_value = self.__emergency_phone_number.get()
        emergency_email_value = self.__emergency_email.get()
        emergency_address_value = self.__emergency_address.get()
        relationship_value = self.__emergency_relationship.get()
        condition_ques1_value = self.__radio1.get()
        condition_ques2_value = self.__radio2.get()

        # Validate the first name
        if not first_name_value.isalpha():

            error_message = "Please enter a valid first name."
            self.show_error_message(error_message)
            self.__error_label.place(x=160, y=187)
            self.__first_name.delete(0, END)
            return
        
        else:
            pass

        self.__error_label.destroy()
        
    # Show error message
    def show_error_message(self, message):

        self.__error_label = Label(self.__contact_frame, text=message, fg="red", anchor="e")