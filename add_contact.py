from tkinter import *
from tkinter.font import Font
import tkinter as tk
from tkinter import messagebox

class AddContact:
    
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
        
        # Base format of label
        label_font = Font(family="Helvetica", size=15, weight="bold")
        
        # Create Labels
        title_label = Label(contact_frame, text="Contact Tracing Information", fg="black", font=label_font, bg="#c3e7fd")
        title_label.pack(anchor="w", padx=100, pady=20) 
        
        personal_info_label = Label(contact_frame, text="Personal Contact Information", fg="black", bg="#c3e7fd")
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
        self.symptoms(contact_frame)
        self.condition_ques1(contact_frame)
        self.condition_ques2(contact_frame)

        # Error Labels
        self.__first_name_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__first_name_error_label.place(x=160, y=188)

        self.__middle_name_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__middle_name_error_label.place(x=170, y=250)

        self.__surname_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__surname_error_label.place(x=145, y=312)

        self.__street_address_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__street_address_error_label.place(x=175, y=492)

        self.__city_address_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__city_address_error_label.place(x=120, y=555)

        self.__province_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__province_error_label.place(x=145, y=620)

        self.__postal_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__postal_error_label.place(x=195, y=680)

        self.__email_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__email_error_label.place(x=100, y=753)
        
        self.__phone_number_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__phone_number_error_label.place(x=150, y=835)
        
        self.__emergency_name_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__emergency_name_error_label.place(x=95, y=990)

        self.__emergency_email_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__emergency_email_error_label.place(x=150, y=1070)
        
        self.__emergency_phone_number_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__emergency_phone_number_error_label.place(x=100, y=1155)
        
        self.__emergency_address_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__emergency_address_error_label.place(x=112, y=1238)
        
        self.__emergency_relationship_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__emergency_relationship_error_label.place(x=135, y=1320)

        # Submit button
        submit_button = Button(contact_frame, text="Submit", command=self.submit_data)
        submit_button.pack(anchor="w", padx=50, pady=20)

        # Error label next to the submit button
        self.__submit_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__submit_error_label.pack(anchor="w", padx=50, pady=5)
        
        
        back_button1 = Button(contact_frame, text="Back", command=window.destroy)
        back_button1.place(x=25, y=50)

        back_button2 = Button(contact_frame, text="Back", command=window.destroy)
        back_button2.pack(anchor="w", padx=100, pady=0)


    def save_data_to_file(self, filename):
        try:
            with open(filename, "a") as file:
                file.write("Contact Tracing Information\n")
                file.write("--------------------------\n")
                file.write("Personal Contact Information\n")
                file.write("                                  \n")
                file.write(f"Name: {self.__first_name.get()} {self.__middle_name.get()} {self.__surname.get()} {self.__suffix.get()}\n")
                file.write(f"Email: {self.__email.get()}\n")
                file.write(f"Phone Number: {self.__phone_number.get()}\n")
                file.write(f"Street Address: {self.__street_address.get()}\n")
                file.write(f"City: {self.__city_address.get()}\n")
                file.write(f"Province: {self.__province.get()}\n")
                file.write(f"Postal/Zip Code: {self.__postal.get()}\n")
                file.write("                            \n")
                file.write("Emergency Contact Information\n")
                file.write("                                  \n")
                file.write(f"Name: {self.__emergency_name.get()}\n")
                file.write(f"Email: {self.__emergency_email.get()}\n")
                file.write(f"Phone Number: {self.__emergency_phone_number.get()}\n")
                file.write(f"Address: {self.__emergency_address.get()}\n")
                file.write(f"Relationship: {self.__emergency_relationship.get()}\n")
                file.write("                       \n")
                file.write("Symptoms\n")
                selected_symptoms = [symptom for symptom in self.__checklist.get().split(", ") if symptom]
                if "None" in selected_symptoms:
                    file.write("None\n")
                else:
                    file.write(", ".join(selected_symptoms) + "\n")
                file.write("                                    \n")
                if self.__radio1.get() == 1:
                    file.write("Recently tested for Covid-19: Yes\n")
                else:
                    file.write("Recently tested for Covid-19: No\n")
                file.write("                                     \n")
                if self.__radio2.get() == 1:
                    file.write("Recently exposed to someone with Covid-19: Yes\n")
                else:
                    file.write("Recently exposed to someone with Covid-19: No\n")
                file.write("                         \n")
            tk.messagebox.showinfo("Success", "Data has been saved to the file.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to save data: {e}")


    def name(self, frame):
        
        self.__name_label = Label(frame, text="Name", fg="black", bg="#c3e7fd")
        self.__name_label.pack(anchor="w", padx=50, pady=15) 
        
        # first name textbox
        self.__first_label = Label(frame, text="First Name", fg="black", bg="#c3e7fd")
        self.__first_label.pack(anchor="w", padx=80, pady=5)
        self.__first_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__first_name.pack(anchor="w", padx=80, pady=5)
        
        # middle name textbox
        self.__middle_label = Label(frame, text="Middle Name", fg="black", bg="#c3e7fd")
        self.__middle_label.pack(anchor="w", padx=80, pady=5)
        self.__middle_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__middle_name.pack(anchor="w", padx=80, pady=5)

        # surname textbox
        self.__surname_label = Label(frame, text="Surname", fg="black", bg="#c3e7fd")
        self.__surname_label.pack(anchor="w", padx=80, pady=5)
        self.__surname = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__surname.pack(anchor="w", padx=80, pady=5)
        
        # suffix textbox
        self.__suffix_label = Label(frame, text="Suffix", fg="black", bg="#c3e7fd")
        self.__suffix_label.pack(anchor="w", padx=80, pady=5)
        self.__suffix = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__suffix.pack(anchor="w", padx=80, pady=5)

    def email(self, frame):
        
        # email textbox
        self.__email_label = Label(frame, text="Email", fg="black", bg="#c3e7fd")
        self.__email_label.pack(anchor="w", padx=50, pady=15) 
        self.__email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__email.pack(anchor="w", padx=50, pady=5)

    def phone_number(self, frame):
        
        # phone number textbox
        self.__phone_number_label = Label(frame, text="Phone Number", fg="black", bg="#c3e7fd")
        self.__phone_number_label.pack(anchor="w", padx=50, pady=15) 
        self.__phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__phone_number.pack(anchor="w", padx=50, pady=5)
        
    def address(self, frame):
        
        self.__address_label = Label(frame, text="Address", fg="black", bg="#c3e7fd")
        self.__address_label.pack(anchor="w", padx=50, pady=15) 
        
        # street address textbox
        self.__street_address_label = Label(frame, text="Street Address", fg="black", bg="#c3e7fd")
        self.__street_address_label.pack(anchor="w", padx=80, pady=5) 
        self.__street_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__street_address.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        self.__city_address_label = Label(frame, text="City", fg="black", bg="#c3e7fd")
        self.__city_address_label.pack(anchor="w", padx=80, pady=5)
        self.__city_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__city_address.pack(anchor="w", padx=80, pady=5)

        # street address textbox
        self.__province_label = Label(frame, text="Province", fg="black", bg="#c3e7fd")
        self.__province_label.pack(anchor="w", padx=80, pady=5) 
        self.__province = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__province.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        self.__postal_label = Label(frame, text="Postal/Zip Code", fg="black", bg="#c3e7fd")
        self.__postal_label.pack(anchor="w", padx=80, pady=5)
        self.__postal = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__postal.pack(anchor="w", padx=80, pady=5)
        
    def emergency_name(self, frame):
        
        self.__emergency_contact_label = Label(frame, text="Emergency Contact Information", fg="black", bg="#c3e7fd")
        self.__emergency_contact_label.pack(anchor="w", padx=15, pady=25) 
        
        # name textbox
        self.__name_label = Label(frame, text="Name", fg="black", bg="#c3e7fd")
        self.__name_label.pack(anchor="w", padx=50, pady=15) 
        self.__emergency_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_name.pack(anchor="w", padx=50, pady=5)
 
    def emergency_phone(self, frame):
         
        #  phone_number textbox
        self.__phone_number_label = Label(frame, text="Phone Number", fg="black", bg="#c3e7fd")
        self.__phone_number_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_phone_number.pack(anchor="w", padx=50, pady=5)

    def emergency_email(self, frame):
        # email textbox
        self.__email_label = Label(frame, text="Email", fg="black", bg="#c3e7fd")
        self.__email_label.pack(anchor="w", padx=50, pady=15) 
        self.__emergency_email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_email.pack(anchor="w", padx=50, pady=5)
 
    def emergency_address(self, frame):
        # address textbox
        self.__address_label = Label(frame, text="Address", fg="black", bg="#c3e7fd")
        self.__address_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_address.pack(anchor="w", padx=50, pady=5)
    
    def emergency_relationship(self, frame):
        # relationship textbox
        self.__relationship_label = Label(frame, text="Relationship", fg="black", bg="#c3e7fd")
        self.__relationship_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_relationship = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_relationship.pack(anchor="w", padx=50, pady=5)
        
        
    def symptoms(self, frame):
        
        self.__checklist = StringVar()

        # Do you experience any symptoms related to Covid-19 checklist
        self.__quest1_label = Label(frame, text="Do you experience any symptoms related to Covid-19? Check all that apply.", fg="black", bg="#c3e7fd")
        self.__quest1_label.pack(anchor="w", padx=50, pady=15)

        # Create a list of Checkbutton widgets
        symptoms_list = [
            "Fever", "Cough", "Shortness of Breath", "Fatigue",
            "Muscle Ache", "Headache", "Loss of Smell", "Loss of Taste",
            "Nausea/Vomiting", "Sore Throat", "Diarrhea", "None"
        ]
        checkbuttons = []
        for symptom in symptoms_list:
            checkbutton = Checkbutton(frame, text=symptom, variable=self.__checklist, onvalue=symptom, offvalue="")
            checkbutton.pack(anchor="w", padx=50, pady=5)
            checkbuttons.append(checkbutton)

    def condition_ques1(self, frame):
        
        self.__radio1 = IntVar()

        # Have you recently tested covid-19 radiobutton
        self.__quest1_label = Label(frame, text="Have you recently tested for Covid-19?", fg="black", bg="#c3e7fd")
        self.__quest1_label.pack(anchor="w", padx=50, pady=15)
        self.__option1_label = Radiobutton(frame, text="Yes", variable=self.__radio1, value=1, bg="#c3e7fd")
        self.__option1_label.pack(anchor="w", padx=50, pady=5)
        self.__option2_label = Radiobutton(frame, text="No", variable=self.__radio1, value=0, bg="#c3e7fd")
        self.__option2_label.pack(anchor="w", padx=50, pady=5)
        
    def condition_ques2(self, frame):
        
        self.__radio2 = IntVar()

        # Are you recently exposed to someone with covid-19 radiobutton
        self.__quest2_label = Label(frame, text="Are you recently exposed to someone with Covid-19?", fg="black", bg="#c3e7fd")
        self.__quest2_label.pack(anchor="w", padx=50, pady=15)
        self.__option3_label = Radiobutton(frame, text="Yes", variable=self.__radio2, value=1, bg="#c3e7fd")
        self.__option3_label.pack(anchor="w", padx=50, pady=5)
        self.__option4_label = Radiobutton(frame, text="No", variable=self.__radio2, value=0, bg="#c3e7fd")
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
        emergency_relationship_value = self.__emergency_relationship.get()
        symptoms_value = self.__checklist.get()
        condition_ques1_value = self.__radio1.get()
        condition_ques2_value = self.__radio2.get()
        
        # Clear all previous error messages
        self.clear_error_message()

        # Validate the first name
        if not first_name_value.replace(" ", "").isalpha():
            error_message = "Please enter a valid first name."
            self.show_error_message(self.__first_name_error_label, error_message)

        # Validate the middle name
        if not middle_name_value.replace(" ", "").isalpha():
            error_message = "Please enter a valid middle name."
            self.show_error_message(self.__middle_name_error_label, error_message)

        # Validate the surname
        if not surname_value.replace(" ", "").isalpha():
            error_message = "Please enter a valid surname."
            self.show_error_message(self.__surname_error_label, error_message)

        # Validate the street address
        if not street_address_value.strip():
            error_message = "Please enter a street address."
            self.show_error_message(self.__street_address_error_label, error_message)

        # Validate the city address
        if not city_address_value.replace(" ", "").isalpha():
            error_message = "Please enter a valid city address."
            self.show_error_message(self.__city_address_error_label, error_message)

        # Validate the province
        if not province_value.replace(" ", "").isalpha():
            error_message = "Please enter a valid province."
            self.show_error_message(self.__province_error_label, error_message)

        # Validate the postal/zip code
        if not postal_value.isdigit() or len(postal_value) != 4:
            error_message = "Please enter a valid postal/zip code."
            self.show_error_message(self.__postal_error_label, error_message)
            
        # Validate the email
        if not email_value.endswith("@gmail.com"):
            error_message = "Please enter a valid email."
            self.show_error_message(self.__email_error_label, error_message)

        # Validate the phone number
        if not phone_number_value.isdigit() or len(phone_number_value) != 11 or not phone_number_value.startswith("09"):
            error_message = "Please enter a 11-digits phone number starting with '09'."
            self.show_error_message(self.__phone_number_error_label, error_message)
            
        # Validate the emergency contact name
        if not emergency_name_value.replace(" ", "").isalpha():
            error_message = "Please enter a valid emergency contact name."
            self.show_error_message(self.__emergency_name_error_label, error_message)
            
        # Validate the emergency contact email
        if not emergency_email_value.endswith("@gmail.com"):
            error_message = "Please enter a valid emergency contact email."
            self.show_error_message(self.__emergency_email_error_label, error_message)

        # Validate the emergency contact phone number
        if not emergency_phone_value.isdigit() or len(phone_number_value) != 11 or not phone_number_value.startswith("09"):
            error_message = "Please enter an emergency contact 11-digits phone number starting with '09'."
            self.show_error_message(self.__emergency_phone_number_error_label, error_message)
            
        # Validate the street address
        if not emergency_address_value.strip():
            error_message = "Please enter an emergency contact address."
            self.show_error_message(self.__emergency_address_error_label, error_message) 
        
        # Validate the emergency relationship
        if not emergency_relationship_value.strip():
            error_message = "Please state the relationship."
            self.show_error_message(self.__emergency_relationship_error_label, error_message)
        
            error_labels = [
                self.__first_name_error_label,
                self.__middle_name_error_label,
                self.__surname_error_label,
                self.__street_address_error_label,
                self.__city_address_error_label,
                self.__province_error_label,
                self.__postal_error_label,
                self.__email_error_label,
                self.__phone_number_error_label,
                self.__emergency_name_error_label,
                self.__emergency_email_error_label,
                self.__emergency_phone_number_error_label,
                self.__emergency_address_error_label,
                self.__emergency_relationship_error_label
            ]

            for label in error_labels:
                if label.cget("text") != "":
                    # If any error message is displayed, show error next to the submit button
                    self.__submit_error_label.config(text="Please fix the errors above before submitting.")
                    return

        # Save data only if all fields pass validation checks
        self.save_data_to_file("contact_tracing_info.txt")
        self.__submit_error_label.config(text="Data has been saved to the file.")
        self.clear_all_inputs()
        
    # Method to show error message
    def show_error_message(self, label, message):
        label.config(text=message)

    # Method to clear error messages
    def clear_error_message(self):
        self.__first_name_error_label.config(text="")
        self.__middle_name_error_label.config(text="")
        self.__surname_error_label.config(text="")
        self.__street_address_error_label.config(text="")
        self.__city_address_error_label.config(text="")
        self.__province_error_label.config(text="")
        self.__postal_error_label.config(text="")
        self.__email_error_label.config(text="")
        self.__phone_number_error_label.config(text="")
        self.__emergency_name_error_label.config(text="")
        self.__emergency_email_error_label.config(text="")
        self.__emergency_phone_number_error_label.config(text="")
        self.__emergency_address_error_label.config(text="")
        self.__emergency_relationship_error_label.config(text="")
        
        self.__submit_error_label.config(text="")
      
    # Method to clear all inputs in entries
    def clear_all_inputs(self):
        self.__first_name.delete(0, END)
        self.__middle_name.delete(0, END)
        self.__surname.delete(0, END)
        self.__suffix.delete(0, END)
        self.__email.delete(0, END)
        self.__phone_number.delete(0, END)
        self.__street_address.delete(0, END)
        self.__city_address.delete(0, END)
        self.__province.delete(0, END)
        self.__postal.delete(0, END)
        self.__emergency_name.delete(0, END)
        self.__emergency_phone_number.delete(0, END)
        self.__emergency_email.delete(0, END)
        self.__emergency_address.delete(0, END)
        self.__emergency_relationship.delete(0, END)