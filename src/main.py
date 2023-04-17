from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

from domains.Employee import Employee
from domains.Doctor import Doctor
from domains.Room import Room
from domains.Patient import Patient
import methods.DoctorMethods as DoctorMethods
import methods.PatientMethods as PatientMethods
import methods.RoomMethods as RoomMethods
import methods.EmployeeMethods as EmployeeMethods


import database

def on_GUI_loaded():
  database.unzip_data()
  global doctors_list
  doctors_list = database.load_doctors()
  global employee_list
  employee_list = database.load_employee()
  global patients_list
  patients_list = database.load_patients()
  global room_list
  room_list = database.load_room()
  global pa_doc_list
  pa_doc_list = database.load_pa_doc()
  global pa_room_list
  pa_room_list = database.load_pa_room()
  
def on_exit():
  global doctors_list
  database.save_doctors(doctors_list)
  global employee_list
  database.save_employee(employee_list)
  global patients_list
  database.save_patients(patients_list)
  global room_list
  database.save_room(room_list)
  global pa_doc_list
  database.save_pa_doc(pa_doc_list)
  global pa_room_list
  database.save_pa_room(pa_room_list)
  database.zip_data()
  window.destroy()
#   window.deiconify()

  
global doctors_list
doctors_list = []
global employee_list
employee_list = []
global patients_list
patients_list = []
global room_list
room_list = []
global pa_doc_list
pa_doc_list = []
global pa_room_list
pa_room_list = []

fulwidth = 1200
fulheight =800


def changeColor(button, colorEntry, colorLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorEntry))
        button.bind("<Leave>", func=lambda e: button.config(background=colorLeave))

def create_window(new_window):
    new_window = Toplevel()
    new_window.geometry("1000x800")
    new_window.minsize(1000, 800)
    new_window.maxsize(1000, 800)
    new_window.title("Hospital Infolmation Management System")
    new_window.config(bg="#319997")
    icon = PhotoImage(file="images\Hospital_icon2.png")
    new_window.iconphoto(False, icon)

    with Image.open("images\Hospital_icon2.png") as img:
        Hos_icon = ImageTk.PhotoImage(img.resize((144,144)))
    
    Frame(new_window, bg="#7C809B").place(x = 20, y = 20, width = 1000-40, height = 800-40)
    Frame(new_window, bg="#ceede8").place(x = 22, y = 22, width = 1000-44, height = 800-44)
    
    Label(new_window, image=Hos_icon, bg="#ceede8", anchor="center").place(x=1000/2-68, y=1000/10)
    Label.img = Hos_icon
    
    with Image.open("images\Doctor_icon.png") as img2:
        Doc_icon = ImageTk.PhotoImage(img2.resize((120,120)))
    Label(new_window, image=Doc_icon, bg="#ceede8", anchor="center").place(x=190, y=800-520)
    Label.img2 = Doc_icon
    
    with Image.open("images\Employee_icon.png") as img3:
        Emp_icon = ImageTk.PhotoImage(img3.resize((120,120)))
    Label(new_window, image=Emp_icon, bg="#ceede8", anchor="center").place(x=690, y=800-520)
    Label.img3 = Emp_icon
    
    with Image.open("images\Patient_icon.png") as img4:
        Patient_icon = ImageTk.PhotoImage(img4.resize((120,120)))
    Label(new_window, image=Patient_icon, bg="#ceede8", anchor="center").place(x=190, y=800-260)
    Label.img4 = Patient_icon
    
    with Image.open("images\Room_icon.png") as img5:
        Room_icon = ImageTk.PhotoImage(img5.resize((120,120)))
    Label(new_window, image=Room_icon, bg="#ceede8", anchor="center").place(x=690, y=800-260)
    Label.img5 = Room_icon
    
    
    doctors_button = Button(new_window, text="DOCTORS", anchor="center", font=("Work Sans", 20, 'bold'), bg="#99CCCD", fg="black", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white", command=lambda: DoctorMethods.doc_press(window, fulwidth, fulheight, doctors_list, patients_list, pa_doc_list))
    doctors_button.place(x=100/2, y=800-400, width=1000-600, height = 50)
    employee_button = Button(new_window, text="EMPLOYEES", anchor="center", font=("Work Sans", 20, 'bold'), bg="#99CCCD", fg="black", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white", command=lambda: EmployeeMethods.emp_press(window, fulwidth, fulheight, employee_list))
    employee_button.place(x=550, y=800-400, width=1000-600, height = 50)
    patients_button = Button(new_window, text="PATIENTS", anchor="center", font=("Work Sans", 20, 'bold'), bg="#99CCCD", fg="black", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white", command=lambda: PatientMethods.pat_press(window, fulwidth, fulheight, doctors_list, patients_list, room_list, pa_doc_list, pa_room_list))
    patients_button.place(x=100/2, y=800-140, width=1000-600, height = 50)
    room_button = Button(new_window, text="ROOM", anchor="center", font=("Work Sans", 20, 'bold'),  bg="#99CCCD", fg="black", relief="ridge", 
            activebackground="#88C1C2", activeforeground="white", command=lambda: RoomMethods.room_press(window, fulwidth, fulheight, room_list, patients_list, pa_room_list))
    room_button.place(x=550, y=800-140, width=1000-600, height = 50)

    changeColor(doctors_button, "#53cbdb", "#88C1C2")
    changeColor(employee_button, "#53cbdb", "#88C1C2")
    changeColor(patients_button, "#53cbdb", "#88C1C2")
    changeColor(room_button, "#53cbdb", "#88C1C2")
#     window.withdraw()
#     new_window.deiconify()
#     new_window.protocol('WM_DELETE_WINDOW', lambda: on_exit(window))

    
    
    

#main window
window = Tk()
window.geometry("1200x800")
window.minsize(1200, 800)
window.maxsize(1200, 800)

window.title("Hospital Infolmation Management System")
window.config(bg="#393b3a")
icon = PhotoImage(file="C:\\Users\\dang1\\Desktop\\Code\\OOP\\python-hospital-management\\src\\images\Hospital_icon2.png")
window.iconphoto(False, icon)

with Image.open("C:\\Users\\dang1\\Desktop\\Code\\OOP\\python-hospital-management\\src\\images\Hospital.png") as img:
    Hos_Image = ImageTk.PhotoImage(img.resize((600,600)))



window.bind("<Button-1>", create_window)

Label(window, image=Hos_Image, bg="#393b3a", anchor="center").pack()
Label(window, text="""HOSPITAL INFORMATION 
MANAGEMENT SYSTEM""", bg="#393b3a", fg="#e6edec", font=("Work Sans", 45, "bold")).pack()

def main():
    on_GUI_loaded()
    window.protocol("WM_DELETE_WINDOW", on_exit)
    window.mainloop()

if __name__ == "__main__":
    main()