from tkinter import *
from tkinter.font import Font
import tkinter as tk
from tkinter import messagebox
import csv

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
        
        # Configure the canvas to scroll the contact frame
        canvas.create_window((0, 0), window=contact_frame, anchor="nw")
        contact_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))
        
        # Base format of label
        label_font = Font(family="Arial Black", size=20, weight="bold", slant="italic")
        
        # Base format of label
        self.__label_font2 = Font(family="Helvetica", size=10, weight="bold", slant="italic")
       
        label_font3 = Font(family="Helvetica", size=8)
        self.__label_font4 = Font(family="Helvetica", size=10, weight="bold")
        self.__label_font5 = Font(family="Helvetica", size=12, weight="bold")
        
        
        # Create Labels
        title_label = Label(contact_frame, text="Contact Tracing Information", font=label_font, fg="black", bg="#c3e7fd")
        title_label.pack(anchor="w", padx=100, pady=20) 
        
        personal_info_label = Label(contact_frame, text="Personal Contact Information", fg="#00219f", bg="#c3e7fd", font=self.__label_font5)
        personal_info_label.pack(anchor="w", padx=15, pady=20)
        
        window_label = Label(contact_frame, text="_______________________________________________________________", fg="black", font=label_font, bg="#c3e7fd")
        window_label.place(x=20, y=55)
        
        # Link to def functions
        self.name(contact_frame)
        self.address(contact_frame)
        self.email(contact_frame)
        self.phone_number(contact_frame)
        self.emergency_name(contact_frame)
        self.emergency_email(contact_frame)
        self.emergency_phone(contact_frame)
        self.emergency_address(contact_frame)
        self.emergency_relationship(contact_frame)
        self.symptoms(contact_frame)
        self.condition_ques1(contact_frame)
        self.condition_ques2(contact_frame)
        self.data_privacy(contact_frame)

        # Error Labels
        self.__first_name_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__first_name_error_label.place(x=180, y=209)

        self.__middle_name_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__middle_name_error_label.place(x=170, y=271)

        self.__surname_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__surname_error_label.place(x=145, y=334)

        self.__street_address_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__street_address_error_label.place(x=175, y=516)

        self.__city_address_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__city_address_error_label.place(x=120, y=579)

        self.__province_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__province_error_label.place(x=145, y=643)

        self.__postal_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__postal_error_label.place(x=195, y=705)

        self.__email_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__email_error_label.place(x=100, y=780)
        
        self.__phone_number_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__phone_number_error_label.place(x=150, y=863)
        
        self.__emergency_name_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__emergency_name_error_label.place(x=95, y=1025)

        self.__emergency_email_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__emergency_email_error_label.place(x=100, y=1108)
        
        self.__emergency_phone_number_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__emergency_phone_number_error_label.place(x=150, y=1191)
        
        self.__emergency_address_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__emergency_address_error_label.place(x=112, y=1274)
        
        self.__emergency_relationship_error_label = Label(contact_frame, text="", fg="red", anchor="w", font=label_font3, bg="#c3e7fd")
        self.__emergency_relationship_error_label.place(x=135, y=1357)

        # Submit button
        submit_button = Button(contact_frame, text="Submit", width=10, command=self.submit_data)
        submit_button.pack(anchor="w", padx=50, pady=20)

        # Error label next to the submit button
        self.__submit_error_label = Label(contact_frame, text="", fg="red", anchor="w", bg="#c3e7fd")
        self.__submit_error_label.pack(anchor="w", padx=50, pady=5)
        
        back_button1 = Button(contact_frame, text="Exit",width=5, activebackground="white", bg="red", fg="white", command=window.destroy)
        back_button1.place(x=20, y=25)

        back_button2 = Button(contact_frame, text="Exit",width=10, activebackground="white", bg="red", fg="white", command=window.destroy)
        back_button2.place(x=200, y=1850)


    def save_data_to_file(self, filename):
        try:
            with open(filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    self.__first_name.get(),
                    self.__middle_name.get(),
                    self.__surname.get(),
                    self.__suffix.get(),
                    self.__email.get(),
                    self.__phone_number.get(),
                    self.__street_address.get(),
                    self.__city_address.get(),
                    self.__province.get(),
                    self.__postal.get(),
                    self.__emergency_name.get(),
                    self.__emergency_email.get(),
                    self.__emergency_phone_number.get(),
                    self.__emergency_address.get(),
                    self.__emergency_relationship.get(),
                    "Yes" if self.__radio3.get() == 1 else "No",
                    "Yes" if self.__radio1.get() == 1 else "No",
                    "Yes" if self.__radio2.get() == 1 else "No",
                    "Yes" if self.__data_privacy_var.get() else "No"
                ])
            tk.messagebox.showinfo("Success", "Data has been saved to the file.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to save data: {e}")


    def name(self, frame):
        
        self.__name_label = Label(frame, text="Name", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__name_label.pack(anchor="w", padx=50, pady=15) 
        
        # first name textbox
        self.__first_label = Label(frame, text="First Name", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__first_label.pack(anchor="w", padx=80, pady=5)
        self.__first_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__first_name.pack(anchor="w", padx=80, pady=5)
        
        # middle name textbox
        self.__middle_label = Label(frame, text="Middle Name", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__middle_label.pack(anchor="w", padx=80, pady=5)
        self.__middle_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__middle_name.pack(anchor="w", padx=80, pady=5)

        # surname textbox
        self.__surname_label = Label(frame, text="Surname", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__surname_label.pack(anchor="w", padx=80, pady=5)
        self.__surname = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__surname.pack(anchor="w", padx=80, pady=5)
        
        # suffix textbox
        self.__suffix_label = Label(frame, text="Suffix", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__suffix_label.pack(anchor="w", padx=80, pady=5)
        self.__suffix = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__suffix.pack(anchor="w", padx=80, pady=5)

    def email(self, frame):
        
        # email textbox
        self.__email_label = Label(frame, text="Email", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__email_label.pack(anchor="w", padx=50, pady=15) 
        self.__email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__email.pack(anchor="w", padx=50, pady=5)

    def phone_number(self, frame):
        
        # phone number textbox
        self.__phone_number_label = Label(frame, text="Phone Number", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__phone_number_label.pack(anchor="w", padx=50, pady=15) 
        self.__phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__phone_number.pack(anchor="w", padx=50, pady=5)
        
    def address(self, frame):
        
        self.__address_label = Label(frame, text="Address", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__address_label.pack(anchor="w", padx=50, pady=15) 
        
        # street address textbox
        self.__street_address_label = Label(frame, text="Street Line", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__street_address_label.pack(anchor="w", padx=80, pady=5) 
        self.__street_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__street_address.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        self.__city_address_label = Label(frame, text="City", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__city_address_label.pack(anchor="w", padx=80, pady=5)
        self.__city_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__city_address.pack(anchor="w", padx=80, pady=5)

        # street address textbox
        self.__province_label = Label(frame, text="Province", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__province_label.pack(anchor="w", padx=80, pady=5) 
        self.__province = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__province.pack(anchor="w", padx=80, pady=5)
 
        # city textbox
        self.__postal_label = Label(frame, text="Postal/Zip Code", fg="black", font=self.__label_font2, bg="#c3e7fd")
        self.__postal_label.pack(anchor="w", padx=80, pady=5)
        self.__postal = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__postal.pack(anchor="w", padx=80, pady=5)
        
    def emergency_name(self, frame):
        
        self.__emergency_contact_label = Label(frame, text="Emergency Contact Information", fg="#00219f", bg="#c3e7fd", font=self.__label_font5)
        self.__emergency_contact_label.pack(anchor="w", padx=15, pady=25) 
        
        # name textbox
        self.__name_label = Label(frame, text="Name", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__name_label.pack(anchor="w", padx=50, pady=15) 
        self.__emergency_name = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_name.pack(anchor="w", padx=50, pady=5)
 
    def emergency_email(self, frame):
        # email textbox
        self.__email_label = Label(frame, text="Email", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__email_label.pack(anchor="w", padx=50, pady=15) 
        self.__emergency_email = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_email.pack(anchor="w", padx=50, pady=5)
 
    def emergency_phone(self, frame):
         
        #  phone_number textbox
        self.__phone_number_label = Label(frame, text="Phone Number", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__phone_number_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_phone_number = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_phone_number.pack(anchor="w", padx=50, pady=5)
 
    def emergency_address(self, frame):
        # address textbox
        self.__address_label = Label(frame, text="Address", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__address_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_address = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_address.pack(anchor="w", padx=50, pady=5)
    
    def emergency_relationship(self, frame):
        # relationship textbox
        self.__relationship_label = Label(frame, text="Relationship", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__relationship_label.pack(anchor="w", padx=50, pady=15)
        self.__emergency_relationship = Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__emergency_relationship.pack(anchor="w", padx=50, pady=5)
        
    def symptoms(self, frame):

            
        self.__radio1 = IntVar()

        # Have you recently tested covid-19 radiobutton
        self.__quest1_label = Label(frame, text="Do you experience any symptoms related to Covid-19? Symptoms such as fever, cold, sore throat, cough, loss of smell/taste, etc.", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__quest1_label.pack(anchor="w", padx=50, pady=15)
        self.__option1_label = Radiobutton(frame, text="Yes", variable=self.__radio1, value=1, bg="#c3e7fd")
        self.__option1_label.pack(anchor="w", padx=50, pady=5)
        self.__option2_label = Radiobutton(frame, text="No", variable=self.__radio1, value=0, bg="#c3e7fd")
        self.__option2_label.pack(anchor="w", padx=50, pady=5)
        
    def condition_ques1(self, frame):
        
        self.__radio3 = IntVar()

        # Have you recently tested covid-19 radiobutton
        self.__quest1_label = Label(frame, text="Have you recently tested for Covid-19?", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__quest1_label.pack(anchor="w", padx=50, pady=15)
        self.__option1_label = Radiobutton(frame, text="Yes", variable=self.__radio3, value=1, bg="#c3e7fd")
        self.__option1_label.pack(anchor="w", padx=50, pady=5)
        self.__option2_label = Radiobutton(frame, text="No", variable=self.__radio3, value=0, bg="#c3e7fd")
        self.__option2_label.pack(anchor="w", padx=50, pady=5)
        
    def condition_ques2(self, frame):
        
        self.__radio2 = IntVar()

        # Are you recently exposed to someone with covid-19 radiobutton
        self.__quest2_label = Label(frame, text="Are you recently exposed to someone with Covid-19?", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__quest2_label.pack(anchor="w", padx=50, pady=15)
        self.__option3_label = Radiobutton(frame, text="Yes", variable=self.__radio2, value=1, bg="#c3e7fd")
        self.__option3_label.pack(anchor="w", padx=50, pady=5)
        self.__option4_label = Radiobutton(frame, text="No", variable=self.__radio2, value=0, bg="#c3e7fd")
        self.__option4_label.pack(anchor="w", padx=50, pady=5)

    def data_privacy(self, frame):

        self.__data_privacy_var = BooleanVar()

        self.__res_data_privacy = Checkbutton(frame, text="I hereby consent to the processing of my personal data under Data Privacy Act 10173.", bg="#c3e7fd", font=self.__label_font4, variable=self.__data_privacy_var)
        self.__res_data_privacy.pack(anchor="w", padx=50, pady=5)

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
        symptoms_value = self.__radio3.get()
        condition_ques1_value = self.__radio1.get()
        condition_ques2_value = self.__radio2.get()
        data_privacy_value = self.__data_privacy_var.get()
        
        # Clear all previous error messages
        self.clear_error_message()

        # Validate all input fields
        validation_passed = True

        # Validate the first name
        if not first_name_value.replace(" ", "").isalpha():
            error_message = "❗Please enter a valid first name."
            self.show_error_message(self.__first_name_error_label, error_message)

        # Validate the middle name
        if not middle_name_value.replace(" ", "").isalpha():
            error_message = "❗Please enter a valid middle name."
            self.show_error_message(self.__middle_name_error_label, error_message)

        # Validate the surname
        if not surname_value.replace(" ", "").isalpha():
            error_message = "❗Please enter a valid surname."
            self.show_error_message(self.__surname_error_label, error_message)

        # Validate the street address
        if not street_address_value.strip():
            error_message = "❗Please enter a street address."
            self.show_error_message(self.__street_address_error_label, error_message)

        # Validate the city address
        if not city_address_value.replace(" ", "").isalpha():
            error_message = "❗Please enter a valid city address."
            self.show_error_message(self.__city_address_error_label, error_message)

        # Validate the province
        if not province_value.replace(" ", "").isalpha():
            error_message = "❗Please enter a valid province."
            self.show_error_message(self.__province_error_label, error_message)

        # Validate the postal/zip code
        if not postal_value.isdigit() or len(postal_value) != 4:
            error_message = "❗Please enter a valid postal/zip code."
            self.show_error_message(self.__postal_error_label, error_message)
            
        # Validate the email
        if not email_value.endswith("@gmail.com"):
            error_message = "❗Please enter a valid email."
            self.show_error_message(self.__email_error_label, error_message)

        # Validate the phone number
        if not phone_number_value.isdigit() or len(phone_number_value) != 11 or not phone_number_value.startswith("09"):
            error_message = "❗Please enter a 11-digits phone number starting with '09'."
            self.show_error_message(self.__phone_number_error_label, error_message)
            
        # Validate the emergency contact name
        if not emergency_name_value.replace(" ", "").isalpha():
            error_message = "❗Please enter a valid emergency contact name."
            self.show_error_message(self.__emergency_name_error_label, error_message)
            
        # Validate the emergency contact email
        if not emergency_email_value.endswith("@gmail.com"):
            error_message = "❗Please enter a valid emergency contact email."
            self.show_error_message(self.__emergency_email_error_label, error_message)

        # Validate the emergency contact phone number
        if not emergency_phone_value.isdigit() or len(phone_number_value) != 11 or not phone_number_value.startswith("09"):
            error_message = "❗Please enter an emergency contact 11-digits phone number starting with '09'."
            self.show_error_message(self.__emergency_phone_number_error_label, error_message)
            
        # Validate the street address
        if not emergency_address_value.strip():
            error_message = "❗Please enter an emergency contact address."
            self.show_error_message(self.__emergency_address_error_label, error_message) 
        
        # Validate the emergency relationship
        if not emergency_relationship_value.strip():
            error_message = "❗Please state the relationship."
            self.show_error_message(self.__emergency_relationship_error_label, error_message)

        if not data_privacy_value:
            self.__submit_error_label.config(text="❗Please give consent to Data Privacy before submitting.", font=self.__label_font4)
            validation_passed = False

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
                self.__submit_error_label.config(text="❗Please fix the errors above before submitting.", font=self.__label_font4)
                validation_passed = False
                break

        if validation_passed:
            # Save data only if all fields pass validation checks
            self.save_data_to_file("contact_tracing_info.csv")
            self.__submit_error_label.config(text="Data has been saved to the file.", font=self.__label_font4)
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
        
        


