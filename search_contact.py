import csv
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

class SearchContact:
    
    def __init__(self, window):

        self.__window = window
        self.__window.title("Search Contact")
        self.__window.geometry("1000x500")
        self.__window.config(bg="#c3e7fd")
        self.__window.resizable(False, False)

        # Base format of label
        label_font = Font(family="Arial Black", size=20, weight="bold", slant="italic")
        self.__label_font4 = Font(family="Helvetica", size=10, weight="bold")

        # Create a frame
        frame = tk.Frame(window, bg="#c3e7fd")
        frame.pack(expand=True, fill=tk.BOTH)

        # Create Labels
        title_label = tk.Label(frame, text="Search Contact Information", font=label_font, fg="black", bg="#c3e7fd")
        title_label.pack(anchor="w", padx=100, pady=20)

        # Search input label and entry box
        search_label = tk.Label(frame, text="Search by Name or Phone Number:", fg="black", font=self.__label_font4, bg="#c3e7fd")
        search_label.pack(anchor="w", padx=50, pady=15)
        self.__search_entry = tk.Entry(frame, fg="black", width=50, font=("Helvetica", 12), bg="#f3faff")
        self.__search_entry.pack(anchor="w", padx=50, pady=5)

        # Search button
        search_button = tk.Button(frame, text="Search", width=10, command=self.search_data)
        search_button.pack(anchor="w", padx=50, pady=20)

        # Create a canvas to add a scrollbar
        canvas = tk.Canvas(frame, bg="#c3e7fd")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar
        scrollbar = tk.Scrollbar(frame, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=scrollbar.set)

        # Create a frame to contain the search results
        self.__results_frame = tk.Frame(canvas, bg="#c3e7fd")
        self.__results_frame.pack(fill=tk.BOTH, padx=500, pady=500)

        canvas.create_window((0, 0), window=self.__results_frame, anchor="nw")
        self.__results_frame.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox("all")))

        # Results label
        self.__results_label = tk.Label(self.__results_frame, text="", fg="black", font=self.__label_font4, bg="#c3e7fd")
        self.__results_label.pack(anchor="w", padx=350, pady=10)

        self.__warning_label = tk.Label(window, text="", fg="red", font=self.__label_font4, bg="#c3e7fd")
        self.__warning_label.place(x=150, y=190)

        # Error label for file not found
        self.__error_label = tk.Label(frame, text="", fg="red", font=self.__label_font4, bg="#c3e7fd")
        self.__error_label.place(x=25, y=30)
        
        #Exit button
        exit_button = tk.Button(window, text="Exit",width=5, activebackground="white", bg="red", fg="white", command=window.destroy)
        exit_button.place(x=20, y=30)
    
    # Search data
    def search_data(self):
        
        self.__warning_label.config(text="")
        self.__error_label.config(text="")
        search_query = self.__search_entry.get()
        
        if not search_query.strip():
            self.__warning_label.config(text="Please enter a name or phone number to search.")
            return
        search_results = self.find_contact(search_query)
        
        if search_results:
            self.display_search_results(search_results)
        else:
            self.__results_label.config(text="No matching contact found.")

    # Find contact in csv file
    def find_contact(self, search_query):
        
        # Read the data from the CSV file
        search_results = []
        
        try:
            with open("contact_tracing_info.csv", "r") as file:
                reader = csv.reader(file)
                header = next(reader)  
                for row in reader:
                    name = f"{row[0]} {row[1]} {row[2]} {row[3]}"
                    phone_number = row[5]
                    if search_query.lower() in name.lower() or search_query in phone_number:
                        search_results.append(row) 
        except FileNotFoundError:
            messagebox.showerror("Error", "Contact file not found. Please save some data first.")

        return search_results

    # Display the file in window
    def display_search_results(self, results):
        
        # Display the search results
        result_text = ""
        
        for result in results:
            name = f"{result[0]} {result[1]} {result[2]} {result[3]}"
            email = result[4]
            phone_number = result[5]
            address = f"{result[6]}, {result[7]}, {result[8]}, {result[9]}"
            emergency_name = result[10]
            emergency_email = result[11]
            emergency_phone_number = result[12]
            emergency_address = result[13]
            emergency_relationship = result[14]
            symptoms = "Yes" if result[15] == "Yes" else "No"
            condition_ques1 = "Yes" if result[16] == "Yes" else "No"
            condition_ques2 = "Yes" if result[17] == "Yes" else "No"
            data_privacy = "Yes" if result[18] == "1" else "No"

            # Add label
            result_text += f"Name: {name}\n"
            result_text += f"Email: {email}\n"
            result_text += f"Phone Number: {phone_number}\n"
            result_text += f"Address: {address}\n"
            result_text += f"Emergency Contact Name: {emergency_name}\n"
            result_text += f"Emergency Contact Email: {emergency_email}\n"
            result_text += f"Emergency Phone Number: {emergency_phone_number}\n"
            result_text += f"Emergency Address: {emergency_address}\n"
            result_text += f"Emergency Relationship: {emergency_relationship}\n"
            result_text += f"Symptoms: {symptoms}\n"
            result_text += f"Recently Tested for Covid-19: {condition_ques1}\n"
            result_text += f"Recently Exposed to Covid-19: {condition_ques2}\n"
            result_text += f"Data Privacy Consent: {data_privacy}\n"
            result_text += "---------------------------------------------------\n"

        self.__results_label.config(text=result_text)