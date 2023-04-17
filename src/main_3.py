from tkinter import *
from PIL import ImageTk, Image
import database

import methods.DoctorMethods as DoctorMethods
import methods.PatientMethods as PatientMethods
import methods.RoomMethods as RoomMethods
import methods.EmployeeMethods as EmployeeMethods

# Initialize the database
database.unzip_data()
doctors_list = database.load_doctors()
employee_list = database.load_employee()
patients_list = database.load_patients()
room_list = database.load_room()
pa_doc_list = database.load_pa_doc()
pa_rooom_list = []
database.zip_data()

# Create main window
window = Tk()

# Set title and icon
window.title("Hospital Information Management System")
window.iconbitmap("images/Hospital_icon.ico")

# Use full screen
window.attributes('-fullscreen', True)

# Define colors
PRIMARY_COLOR = "#c04e01"
SECONDARY_COLOR = "#f3a712"
BACKGROUND_COLOR = "#f7f7f7"

# Define fonts
HEADING_FONT = ("Arial", 30, "bold")
SUBHEADING_FONT = ("Arial", 25, "bold")
BUTTON_FONT = ("Arial", 20, "bold")

# Define image paths
HOSPITAL_ICON_PATH = "images/Hospital_icon.png"
HOSPITAL_LOGO_PATH = "images/Hospital.png"

#==========================================================================================
# Decorate Main Menu
with Image.open(HOSPITAL_ICON_PATH) as img:
    resized_image = img.resize((250, 250))
    HospitalImg = ImageTk.PhotoImage(resized_image)

with Image.open(HOSPITAL_LOGO_PATH) as img:
    resized_image = img.resize((400, 200))
    HospitalLogo = ImageTk.PhotoImage(resized_image)

# Create frames
left_frame = Frame(window, bg=PRIMARY_COLOR, height=window.winfo_screenheight())
left_frame.pack(side=LEFT, fill=Y)

right_frame = Frame(window, bg=BACKGROUND_COLOR, height=window.winfo_screenheight())
right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Left panel
Label(left_frame, image=HospitalImg, bg=PRIMARY_COLOR, anchor='center').place(relx=0.5, y=50, anchor=CENTER)

# Buttons
doctors_button = Button(left_frame, text="DOCTORS", font=BUTTON_FONT, bg=PRIMARY_COLOR, fg="white", relief='raised',
                         activebackground=SECONDARY_COLOR, activeforeground='white', command=lambda: DoctorMethods.doc_press(window, doctors_list, patients_list, pa_doc_list))

