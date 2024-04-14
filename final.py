#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rushika
#
# Created:     27-03-2024
# Copyright:   (c) Rushika 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox, simpledialog

contact_names = ["Riya-daughter", "Rakesh - son", "Harinath-caretaker", "Hospital", "Ambulance"]
contact_numbers = {}

class SignupPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Signup Page")
        self.create_signup_options()

    def create_signup_options(self):
        signup_frame = tk.Frame(self.master)
        signup_frame.pack(pady=20)

        # Adding Sahara title
        tk.Label(signup_frame, text="SAHARA", font=("Font_tuple", 30)).pack()  # Adjust font size as needed

        tk.Label(signup_frame, text="Select Signup Option:", font=("Font_tuple", 14)).pack()

        senior_button = tk.Button(signup_frame, text="Signup for Senior Citizen", command=self.signup_as_senior)
        senior_button.pack(pady=10)

        guardian_button = tk.Button(signup_frame, text="Signup for Guardians or Caretakers", command=self.signup_as_guardian)
        guardian_button.pack(pady=10)

    def signup_as_senior(self):
        self.master.destroy()
        root = tk.Tk()
        app = SeniorSafetyApp(root, user_type="senior")
        root.mainloop()

    def signup_as_guardian(self):
        username = simpledialog.askstring("Guardian Username", "Enter Guardian Username:")
        if username:
            password = simpledialog.askstring("Guardian Password", "Enter Guardian Password:", show='*')
            if password == "rushika":  # Replace "your_password" with the actual password
                self.master.destroy()
                root = tk.Tk()
                app = SeniorSafetyApp(root, user_type="guardian")
                root.mainloop()
            else:
                messagebox.showerror("Invalid Password", "Incorrect password! Please try again.")
        else:
            messagebox.showerror("Invalid Username", "Please enter a valid username.")

class SeniorSafetyApp:
    def __init__(self, master, user_type):
        self.master = master
        self.master.title("Senior Safety App")
        self.user_type = user_type

        # Initialize variables
        self.emergency_contacts = []
        self.check_in_button = None
        self.check_in_thread = None
        self.medication_reminders = {}  # Dictionary to store medication reminders

        # Create GUI elements based on user type
        if self.user_type == "senior":
            self.create_emergency_sos_button()
            self.create_emergency_contacts()
            self.create_medication_reminders()  # New method call
        elif self.user_type == "guardian":
            self.create_check_in_feature()
            self.create_medication_reminders()

    def create_emergency_sos_button(self):
        sos_button = tk.Button(self.master, text="Emergency SOS", command=self.trigger_emergency_alert,
                                bg="red", fg="white", font=("Helvetica", 16))
        sos_button.pack(pady=5)

    def create_medication_reminders(self):
        medication_button = tk.Button(self.master, text="Medication Reminders", command=self.open_medication_reminders,
                                      bg="blue", fg="white", font=("Helvetica", 16))
        medication_button.pack(pady=5)

    def create_check_in_feature(self):
        check_in_frame = tk.Frame(self.master)
        check_in_frame.pack(pady=20)

        self.check_in_button = tk.Button(check_in_frame, text="Schedule Appointment", command=self.schedule_appointment,
                                         bg="green", fg="white", font=("Helvetica", 16))
        self.check_in_button.pack(pady=5)

        update_contacts_button = tk.Button(check_in_frame, text="Update Contacts", command=self.update_contacts,
                                           bg="orange", fg="white", font=("Helvetica", 16))
        update_contacts_button.pack(pady=5)

        update_medication_button = tk.Button(check_in_frame, text="Update Medication Reminders", command=self.update_medication_reminders,
                                             bg="purple", fg="white", font=("Helvetica", 16))
        update_medication_button.pack(pady=5)

    def create_emergency_contacts(self):
        contacts_button = tk.Button(self.master, text="Emergency Contacts", command=self.open_emergency_contacts,
                                    bg="orange", fg="white", font=("Helvetica", 16))
        contacts_button.pack(pady=5)

    def trigger_emergency_alert(self):
        messagebox.showinfo("Emergency Alert", "Emergency SOS signal sent to contacts!")

    def open_medication_reminders(self):
        reminder_message = ""
        if self.user_type == "senior":
            if self.medication_reminders:
                for name, reminder in self.medication_reminders.items():
                    reminder_message += f"\n{name}:\n{reminder}"
            else:
                reminder_message = "No medication reminders set."
            messagebox.showinfo("Medication Reminders", reminder_message)
        elif self.user_type == "guardian":
            ailment_name = simpledialog.askstring("Medication Reminder", "Enter Ailment Name:")
            medicine_name = simpledialog.askstring("Medication Reminder", "Enter Medicine Name:")
            dosage_per_day = simpledialog.askinteger("Medication Reminder", "Enter Dosage per Day:")
            quantity = simpledialog.askinteger("Medication Reminder", "Enter Quantity:")
            reminder_everyday = messagebox.askyesno("Medication Reminder", "Set Reminder for Everyday?")
            if ailment_name and medicine_name and dosage_per_day and quantity:
                reminder_message = f"Ailment: {ailment_name}\nMedicine: {medicine_name}\nDosage per Day: {dosage_per_day}\nQuantity: {quantity}"
                if reminder_everyday:
                    reminder_message += "\nReminder set for everyday."
                else:
                    reminder_message += "\nReminder not set for everyday."
                self.medication_reminders[medicine_name] = reminder_message
                messagebox.showinfo("Medication Reminder", "Medication reminder set successfully.")

    def open_emergency_contacts(self):
        contact_window = tk.Toplevel(self.master)
        contact_window.title("Emergency Contacts")

        for contact_name in contact_names:
            contact_button = tk.Button(contact_window, text=contact_name, command=lambda name=contact_name: self.call_contact(name))
            contact_button.pack(pady=5)

    def call_contact(self, name):
        messagebox.showinfo("Calling", f"Calling {name}")

    def schedule_appointment(self):
        appointment_window = tk.Toplevel(self.master)
        appointment_window.title("Schedule Appointment")

        tk.Label(appointment_window, text="Select Timing Slot:", font=("Helvetica", 12)).pack()
        timing_options = ["9:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM" , "12:00PM - 1:00PM"]
        timing_var = tk.StringVar(value=timing_options[0])
        timing_menu = tk.OptionMenu(appointment_window, timing_var, *timing_options)
        timing_menu.pack(pady=5)

        tk.Label(appointment_window, text="Select Doctor:", font=("Helvetica", 12)).pack()
        doctor_options = ["Dr.Kiran - cardiologist", "Dr.Samar - physician", "Dr.Sunita - Neurologist" , "Dr. rahul - Dentist" , "Dr. Tilak - Ophthalmologist"]
        doctor_var = tk.StringVar(value=doctor_options[0])
        doctor_menu = tk.OptionMenu(appointment_window, doctor_var, *doctor_options)
        doctor_menu.pack(pady=5)

        confirm_button = tk.Button(appointment_window, text="Confirm Appointment", command=lambda: self.confirm_appointment(timing_var.get(), doctor_var.get()))
        confirm_button.pack(pady=10)

    def confirm_appointment(self, timing, doctor):
        messagebox.showinfo("Appointment Scheduled", f"Appointment scheduled for {timing} with {doctor}.")

    def update_contacts(self):
        update_contacts_window = tk.Toplevel(self.master)
        update_contacts_window.title("Update Contacts")

        add_contact_button = tk.Button(update_contacts_window, text="Add Contact", command=self.add_contact)
        add_contact_button.pack(pady=5)

        delete_contact_button = tk.Button(update_contacts_window, text="Delete Contact", command=self.delete_contact)
        delete_contact_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter Contact Name:")
        number = simpledialog.askstring("Add Contact", "Enter Contact Number:")
        if name and number:
            contact_names.append(name)
            contact_numbers[name] = number
            messagebox.showinfo("Add Contact", "Contact added.")

    def delete_contact(self):
        def confirm_delete():
            selected_index = contact_listbox.curselection()
            if selected_index:
                index = selected_index[0]
                contact_name = contact_listbox.get(index)
                contact_listbox.delete(index)
                contact_names.remove(contact_name)
                messagebox.showinfo("Delete Contact", f"Contact '{contact_name}' deleted.")
                contact_window.destroy()

        contact_window = tk.Toplevel(self.master)
        contact_window.title("Delete Contact")

        tk.Label(contact_window, text="Select Contact to Delete:", font=("Helvetica", 12)).pack()
        contact_listbox = tk.Listbox(contact_window, selectmode=tk.SINGLE)
        for contact_name in contact_names:
            contact_listbox.insert(tk.END, contact_name)
        contact_listbox.pack(pady=5)

        confirm_button = tk.Button(contact_window, text="Confirm Delete", command=confirm_delete)
        confirm_button.pack(pady=5)

    def update_medication_reminders(self):
        # Add functionality to update medication reminders
        pass

def main():
    root = tk.Tk()
    app = SignupPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
