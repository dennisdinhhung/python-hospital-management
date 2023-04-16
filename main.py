from tkinter import *
from PIL import ImageTk, Image

from src.domains.Employee import Employee
from src.domains.Doctor import Doctor
from src.domains.Room import Room
from src.domains.Patient import Patient
from src.methods.DoctorMethods import DoctorMethods
from src.methods.PatientMethods import PatientMethods
from src.methods.RoomMethods import RoomMethods
from src.methods.EmployeeMethods import EmployeeMethods


import database

def on_GUI_loaded():
  database.unzip_data()
  global doctors_list
  doctors_list = database.load_doctors()
  global employees_list
  employees_list = database.load_employees()
  global patients_list
  patients_list = database.load_patients()
  # global medicines_list
  # medicines_list = database.load_medicines()
  global pa_doc_list
  pa_doc_list = database.load_pa_doc()
  # global pa_med_list
  # pa_med_list = database.load_pa_med()
  
def on_exit():
  global doctors_list
  database.save_doctors(doctors_list)
  global employees_list
  database.save_employees(employees_list)
  global patients_list
  database.save_patients(patients_list)
  global medicines_list
  database.save_rooms(rooms_list)
  global pa_doc_list
  database.save_pa_doc(pa_doc_list)
  global pa_roo_list
  database.save_pa_roo(pa_roo_list)
  database.zip_data()
  window.destroy()
  
global doctors_list
doctors_list = []
global employees_list
employees_list = []
global patients_list
patients_list = []
global medicines_list
rooms_list = []
global pa_doc_list
pa_doc_list = []
global pa_roo_list
pa_roo_list = []


def create_window(window):
    new_window = Toplevel()
    new_window.geometry("1000x800")
    # new_window.minsize(1000, 800)
    # new_window.maxsize(1000, 800)
    new_window.title("Hospital Infolmation Management System")
    new_window.config(bg="#319997")
    icon = PhotoImage(file="C:\\Users\\dang1\\Pictures\\Presentation\Hospital_icon.png")
    new_window.iconphoto(False, icon)
    
    with Image.open("C:\\Users\\dang1\\Pictures\\Presentation\Hospital_icon.png") as img:
        Hos_icon = ImageTk.PhotoImage(img.resize((144,144)))


    Frame(new_window, bg="#7C809B").place(x = 20, y = 20, width = 1000-40, height = 800-40)
    Frame(new_window, bg="#ceede8").place(x = 22, y = 22, width = 1000-44, height = 800-44)
    
    Label(new_window, image=Hos_icon, bg="#ceede8", anchor="center").place(x=1000/2-68, y=1000/10)
    Label.img = Hos_icon
    
    doctors_button = Button(new_window, text="DOCTORS", anchor="center", font=("Work Sans", 20), bg="#99CCCD", fg="white", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white", command=lambda: DoctorMethods.doc_press(window, doctors_list, patients_list, pa_doc_list))
    doctors_button.place(x=100, y=800-500, width=1000-200, height = 50)
    employees_button = Button(new_window, text="EMPLOYEES", anchor="center", font=("Work Sans", 20), bg="#99CCCD", fg="white", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white")
    employees_button.place(x=100, y=800-440, width=1000-200, height = 50)
    patients_button = Button(new_window, text="PATIENTS", anchor="center", font=("Work Sans", 20), bg="#99CCCD", fg="white", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white")
    patients_button.place(x=100, y=800-380, width=1000-200, height = 50)
    room_button = Button(new_window, text="ROOM", anchor="center", font=("Work Sans", 20),  bg="#99CCCD", fg="white", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white")
    room_button.place(x=100, y=800-320, width=1000-200, height = 50)

    
    
    

#main window
window = Tk()
window.geometry("1200x800")
window.minsize(1200, 800)
window.maxsize(1200, 800)

window.title("Hospital Infolmation Management System")
window.config(bg="#319997")
icon = PhotoImage(file="C:\\Users\\dang1\\Pictures\\Presentation\Hospital_icon.png")
window.iconphoto(False, icon)

with Image.open("C:\\Users\\dang1\\Pictures\\Presentation\Hospital.png") as img:
    Hos_Image = ImageTk.PhotoImage(img.resize((600,600)))


    
window.bind("<Button-1>", create_window)

Label(window, image=Hos_Image, bg="#319997", anchor="center").pack()
Label(window, text="""HOSPITAL INFORMATION 
MANAGEMENT SYSTEM""", bg="#319997", fg="#e6edec", font=("Work Sans", 45, "bold")).pack()


window.mainloop()

# def main():
#     on_GUI_loaded()
#     window.protocol("WM_DELETE_WINDOW", on_exit)
#     window.mainloop()

# if __name__ == "__main__":
#     main()