import pickle 
import os
import zipfile


def save_doctors(doctors_list):
    with open("doctors.pkl", "wb") as f:
        pickle.dump(doctors_list, f, pickle.HIGHEST_PROTOCOL)

def save_employee(employee_list):
    with open("employee.pkl", "wb") as f:
        pickle.dump(employee_list, f, pickle.HIGHEST_PROTOCOL)

def save_patients(patients_list):
    with open("patients.pkl", "wb") as f:
        pickle.dump(patients_list, f, pickle.HIGHEST_PROTOCOL)

def save_room(room_list):
    with open("room.pkl", "wb") as f:
        pickle.dump(room_list, f, pickle.HIGHEST_PROTOCOL)

def save_pa_doc(pa_doc_list):
    with open("pa_doc.pkl", "wb") as f:
        pickle.dump(pa_doc_list, f, pickle.HIGHEST_PROTOCOL)

def save_pa_room(pa_room_list):
    with open("pa_room.pkl", "wb") as f:
        pickle.dump(pa_room_list, f, pickle.HIGHEST_PROTOCOL)

def zip_data():
    with zipfile.ZipFile('hospital.dat', 'w', compression=zipfile.ZIP_DEFLATED) as zip:        
        zip.write('doctors.pkl')
        zip.write('employee.pkl')
        zip.write('patients.pkl')
        zip.write('room.pkl')
        zip.write('pa_doc.pkl')
    os.remove('doctors.pkl')
    os.remove('employee.pkl')
    os.remove('patients.pkl')
    os.remove('room.pkl')
    os.remove('pa_doc.pkl')

#===========================================================================

def load_doctors():
    doctor_list = []
    if(os.path.exists("doctors.pkl")):
        with open("doctors.pkl", "rb") as f:
            doctor_list = pickle.load(f)

    return (doctor_list)

def load_employee():
    employee_list = []
    if(os.path.exists("employee.pkl")):
        with open("employee.pkl", "rb") as f:
            employee_list = pickle.load(f)

    return (employee_list)

def load_patients():
    patients_list = []
    if(os.path.exists("patients.pkl")):
        with open("patients.pkl", "rb") as f:
            patients_list = pickle.load(f)

    return (patients_list)

def load_room():
    room_list = []
    if(os.path.exists("room.pkl")):
        with open("room.pkl", "rb") as f:
            room_list = pickle.load(f)

    return (room_list)

def load_pa_doc():
    pa_doc_list = []
    if(os.path.exists("pa_doc.pkl")):
        with open("pa_doc.pkl", "rb") as f:
            pa_doc_list = pickle.load(f)

    return (pa_doc_list)

def load_pa_room():
    pa_room_list = []
    if(os.path.exists("pa_room.pkl")):
        with open("pa_room.pkl", "rb") as f:
            pa_room_list = pickle.load(f)

    return (pa_room_list)

def unzip_data():
    if os.path.exists('hospital.dat'):
        with zipfile.ZipFile('hospital.dat', 'r') as zip:
            zip.extractall()
        os.remove("hospital.dat")
