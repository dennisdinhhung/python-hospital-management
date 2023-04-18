from domains.Patient import Patient
from domains.Person import *
from domains.classConnection import *
from domains.Room import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')
    
    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gender_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    illness_entry.delete(0, END)
    debt_entry.delete(0, END)

    # Set selected_patient to -1
    global selected_patient
    selected_patient = -1

def pat_add(patients_list, pat_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry):
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')

    id = id_entry.get()
    name = name_entry.get()
    gender = gender_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    illness = illness_entry.get()
    debt = debt_entry.get()

    # Validation
    valid_check = 0

    # Validate ID
    if len(id) == 0:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "P-") == 1:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for patient in patients_list:
            if patient.get_id() == id:
                Label(entry_frame, bg='#88C1C2', fg='crimson', text='ID already exist', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break
    
    # Validate Name
    if len(name) == 0:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1

    # Validate Gender
    if len(gender) == 0:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_gender(gender) == 1:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1

    # Validate Date of Birth
    if len(dob) == 0:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(dob) == 1:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1

    # Validate Phone:
    if len(phone) != 0 and phone != '_':
        if utils.invalid_phone(phone) == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1

    # Validate Debt
    if len(debt) != 0:
        if utils.invalid_salary(debt) == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1

    # If All Valid
    if valid_check == 0:
        # Add to patients_list
        new_pat = Patient(id, name, gender, dob)
        if len(phone) > 0:
            new_pat.set_phone(phone)
        if len(email) > 0:
            new_pat.set_email(email)
        if len(illness) > 0:
            new_pat.set_illness(illness)
        if len(debt) > 0:
            new_pat.set_debt(debt)
        patients_list.append(new_pat)

        # Display on Treeview
        pat_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name, gender, dob))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gender_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        illness_entry.delete(0, END)
        debt_entry.delete(0, END)

def pat_remove(patients_list, pat_tree, pa_doc_list, pa_room_list):
    if len(pat_tree.selection())>0:
        selected_pat = pat_tree.selection()[0]
        patient_id = pat_tree.item(selected_pat, 'values')[0]

        for relation in pa_doc_list:
            if relation.get_PatientID() == patient_id:
                pa_doc_list.remove(relation)

        for relation in pa_room_list:
            if relation.get_PatientID() == patient_id:
                pa_room_list.remove(relation)

        for patient in patients_list:
            if patient.get_id()== patient_id:
                patients_list.remove(patient)
                break

        pat_tree.delete(selected_pat)

def all_pat_remove(pat_tree, patients_list, pa_doc_list, pa_room_list):
    for patient in pat_tree.get_children():
        pat_tree.delete(patient)
    pa_doc_list.clear()
    pa_room_list.clear()
    patients_list.clear()

def pat_select(patients_list, pat_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gender_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    illness_entry.delete(0, END)
    debt_entry.delete(0, END)

    # Show Selected Patient Info
    if len(pat_tree.selection())>0:
        global selected_patient
        selected_patient = pat_tree.selection()[0]
        patient_id = pat_tree.item(selected_patient, 'values')[0]

        for patient in patients_list:
            if patient.get_id()== patient_id:
                id_entry.insert(0, patient.get_id())
                name_entry.insert(0, patient.get_name())
                gender_entry.insert(0, patient.get_gender())
                dob_entry.insert(0, patient.get_dob())
                phone_entry.insert(0, patient.get_phone())
                email_entry.insert(0, patient.get_email())
                illness_entry.insert(0, patient.get_illness())
                debt_entry.insert(0, patient.get_debt())
                break

def pat_update(patients_list, pa_doc_list, pa_room_list, pat_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry):
    global selected_patient
    if selected_patient != -1:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=4,sticky='w')
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=5,sticky='w')
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=6,sticky='w')
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')

        id = id_entry.get()
        name = name_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        illness = illness_entry.get()
        debt = debt_entry.get()

        # Validation
        valid_check = 0

        # Validate ID
        if len(id) == 0:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "P-") == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            if id != pat_tree.item(selected_patient, 'values')[0]:
                for patient in patients_list:
                    if patient.get_id() == id:
                        Label(entry_frame, bg='#88C1C2', fg='crimson', text='ID already exist', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
        
        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Gender
        if len(gender) == 0:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_gender(gender) == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1

        # Validate Date of Birth
        if len(dob) == 0:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(dob) == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1

        # Validate Phone:
        if len(phone) != 0 and phone != '_':
            if utils.invalid_phone(phone) == 1:
                Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=4,sticky='w')
                valid_check += 1

        # Validate Debt
        if len(debt) != 0:
            if utils.invalid_salary(debt) == 1:
                Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')
                valid_check += 1

        # If All Valid
        if valid_check == 0:
            for patient in patients_list:
                if patient.get_id() == pat_tree.item(selected_patient, 'values')[0]:
                    patient.set_id(id)
                    patient.set_name(name)
                    patient.set_gender(gender)
                    patient.set_dob(dob)
                    if len(phone) > 0:
                        patient.set_phone(phone)
                    elif len(phone) == 0:
                        patient.set_phone('_')
                    if len(email) > 0:
                        patient.set_email(email)
                    elif len(email) == 0:
                        patient.set_email('_')
                    if len(illness) > 0:
                        patient.set_illness(illness)
                    elif len(illness) == 0:
                        patient.set_illness('_')
                    if len(debt) > 0:
                        patient.set_debt(debt)
                    elif len(debt) == 0:
                        patient.set_debt(0)
                    break

            for relation in pa_doc_list:
                if relation.get_PatientID() == pat_tree.item(selected_patient, 'values')[0]:
                    relation.set_PatientID(id)

            for relation in pa_room_list:
                if relation.get_PatientID() == pat_tree.item(selected_patient, 'values')[0]:
                    relation.set_PatientID(id)

            pat_tree.item(selected_patient, text="", values = (id, name, gender, dob))
            selected_patient = -1

            id_entry.delete(0, END)
            name_entry.delete(0, END)
            gender_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            illness_entry.delete(0, END)
            debt_entry.delete(0, END)

def doctors_assignment(pat_subwin, pat_tree, fulwidth, fulheight, pa_doc_list, doctors_list, assigned_doctors_list, unassigned_doctors_list):
    if selected_patient != -1:    
        patda_subwin = Toplevel(pat_subwin)
        patda_subwin.geometry("%dx%d" % (fulwidth, fulheight))
        icon = PhotoImage(file = "images/Hospital_icon.png")
        patda_subwin.iconphoto(False, icon)
        patda_subwin.title("Doctors Assignment")
        Frame(patda_subwin, bg='#88C1C2').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
        Label(patda_subwin, text='ASSIGNED DOCTORS', bg='#88C1C2', fg='white', font=("Work Sans", 20, 'bold')).place(x=50,y=50,width=fulwidth/2-100,height=50)
        Label(patda_subwin, text='UNASSIGNED DOCTORS', fg='#88C1C2', font=("Work Sans", 20, 'bold')).place(x=fulwidth/2+50,y=50,width=fulwidth/2-100,height=50)

        # Create list of assigned and unassigned patients for selected doctor
        assigned_doctors_list.clear()
        unassigned_doctors_list.clear()

        patient_id = pat_tree.item(selected_patient, 'values')[0]
        temp_list = []

        for relation in pa_doc_list:
            if relation.get_PatientID() == patient_id:
                temp_list.append(relation)

        for doctor in doctors_list:
            check = 0
            for relation in temp_list:
                if doctor.get_id() == relation.get_DoctorID():
                    check += 1
                    break
            if check == 0:
                unassigned_doctors_list.append(doctor)
            else:
                assigned_doctors_list.append(doctor)
        temp_list.clear()

        #============================================================================
        # Unassigned doctors tree
        unassigned_doctors_tree = ttk.Treeview(patda_subwin, selectmode='browse', show='headings')

        # define columns
        unassigned_doctors_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

        # Format columns
        unassigned_doctors_tree.column("#0", width=0, stretch=NO)
        unassigned_doctors_tree.column("ID", anchor='center', width=75)
        unassigned_doctors_tree.column("Name",anchor='w', width=150)
        unassigned_doctors_tree.column("Gender",anchor='center', width=75)
        unassigned_doctors_tree.column("Date of Birth",anchor='center', width=125)

        # Create Headings
        unassigned_doctors_tree.heading("#0", text="")
        unassigned_doctors_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_doctors_tree, unassigned_doctors_list, "ID", False))
        unassigned_doctors_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_doctors_tree, unassigned_doctors_list, "Name", False))
        unassigned_doctors_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_doctors_tree, unassigned_doctors_list, "Gender", False))
        unassigned_doctors_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_doctors_tree, unassigned_doctors_list, "Date of Birth", False))

        unassigned_doctors_tree.bind('<Motion>', 'break')

        # Insert Data
        global unassigned_doctors_count
        unassigned_doctors_count = 0
        for doctor in unassigned_doctors_list:
            unassigned_doctors_tree.insert(parent='', index = 'end', iid=doctor.get_id(), text='', values=(doctor.get_id(), doctor.get_name(), doctor.get_gender(), doctor.get_dob()))
            unassigned_doctors_count += 1

        unassigned_doctors_tree.place(x=fulwidth/2+50, y=100, height=fulheight-300, width=fulwidth/2-100)

        #============================================================================
        # assigned doctors tree
        assigned_doctors_tree = ttk.Treeview(patda_subwin, selectmode='browse', show='headings')

        # define columns
        assigned_doctors_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

        # Format columns
        assigned_doctors_tree.column("#0", width=0, stretch=NO)
        assigned_doctors_tree.column("ID", anchor='center', width=75)
        assigned_doctors_tree.column("Name",anchor='w', width=150)
        assigned_doctors_tree.column("Gender",anchor='center', width=75)
        assigned_doctors_tree.column("Date of Birth",anchor='center', width=125)

        # Create Headings
        assigned_doctors_tree.heading("#0", text="")
        assigned_doctors_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_doctors_tree, assigned_doctors_list, "ID", False))
        assigned_doctors_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_doctors_tree, assigned_doctors_list, "Name", False))
        assigned_doctors_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_doctors_tree, assigned_doctors_list, "Gender", False))
        assigned_doctors_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_doctors_tree, assigned_doctors_list, "Date of Birth", False))

        assigned_doctors_tree.bind('<Motion>', 'break')

        # Insert Data
        global assigned_doctors_count
        assigned_doctors_count = 0
        for doctor in assigned_doctors_list:
            assigned_doctors_tree.insert(parent='', index = 'end', iid=doctor.get_id(), text='', values=(doctor.get_id(), doctor.get_name(), doctor.get_gender(), doctor.get_dob()))
            assigned_doctors_count += 1

        assigned_doctors_tree.place(x=50, y=100, height=fulheight-300, width=fulwidth/2-100)

        # ===============================================================================

        Label(patda_subwin, text=f"COUNT: {assigned_doctors_count}", anchor='e', bg='#88C1C2', fg='white', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(patda_subwin, text=f"COUNT: {unassigned_doctors_count}", anchor='e',fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)


        # Buttons
        assign_doctor_button = Button(patda_subwin, text='ASSIGN DOCTOR', font=("Work Sans", 16, 'bold'), fg='white', bg='#88C1C2', relief='ridge',
            activebackground='#88C1C2', activeforeground='white', command=lambda: assign_doctor(patda_subwin,fulwidth, fulheight, unassigned_doctors_tree, assigned_doctors_tree, unassigned_doctors_list, assigned_doctors_list, doctors_list, pa_doc_list, patient_id))
        assign_doctor_button.place(x=fulwidth/2+50, y=fulheight-150, width=250, height=50)

        unassign_doctor_button = Button(patda_subwin, text='UNASSIGN DOCTOR', font=("Work Sans", 16, 'bold'), fg='#88C1C2', relief='ridge',
            activebackground='#88C1C2', activeforeground='white', command=lambda: unassign_doctor(patda_subwin, fulwidth, fulheight, assigned_doctors_tree, unassigned_doctors_tree, assigned_doctors_list, unassigned_doctors_list, doctors_list, patient_id, pa_doc_list))
        unassign_doctor_button.place(x=50, y=fulheight-150, width=250, height=50)

def assign_doctor(patda_subwin, fulwidth, fulheight, unassigned_doctors_tree, assigned_doctors_tree, unassigned_doctors_list, assigned_doctors_list, doctors_list, pa_doc_list, patient_id):
    if len(unassigned_doctors_tree.selection())>0:
        selected_unassigned_doctor = unassigned_doctors_tree.selection()[0]
        doctor_id = unassigned_doctors_tree.item(selected_unassigned_doctor, 'values')[0]

        pa_doc_list.append(PatientAndDoctor(patient_id, doctor_id))
        global unassigned_doctors_count
        global assigned_doctors_count

        assigned_doctors_tree.insert(parent='', index = 'end', iid=doctor_id, text='', values=(unassigned_doctors_tree.item(selected_unassigned_doctor, 'values')))
        unassigned_doctors_tree.delete(selected_unassigned_doctor)

        for doctor in doctors_list:
            if doctor.get_id()==doctor_id:
                assigned_doctors_list.append(doctor)
                break

        for doctor in unassigned_doctors_list:
            if doctor.get_id()==doctor_id:
                unassigned_doctors_list.remove(doctor)
                break
        unassigned_doctors_count -= 1
        assigned_doctors_count += 1
        Label(patda_subwin, text=f"COUNT: {assigned_doctors_count}", anchor='e', bg='#88C1C2', fg='white', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(patda_subwin, text=f"COUNT: {unassigned_doctors_count}", anchor='e',fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def unassign_doctor(patda_subwin, fulwidth, fulheight, assigned_doctors_tree, unassigned_doctors_tree, assigned_doctors_list, unassigned_doctors_list, doctors_list, patient_id, pa_doc_list):
    if len(assigned_doctors_tree.selection())>0:
        selected_assigned_doctor = assigned_doctors_tree.selection()[0]
        doctor_id = assigned_doctors_tree.item(selected_assigned_doctor, 'values')[0]

        for relation in pa_doc_list:
            if relation.get_PatientID() == patient_id and relation.get_DoctorID() == doctor_id:
                pa_doc_list.remove(relation)

        global unassigned_doctors_count
        global assigned_doctors_count

        unassigned_doctors_tree.insert(parent='', index = 'end', iid=doctor_id, text='', values=(assigned_doctors_tree.item(selected_assigned_doctor, 'values')))
        assigned_doctors_tree.delete(selected_assigned_doctor)
        
        for doctor in doctors_list:
            if doctor.get_id()==doctor_id:
                unassigned_doctors_list.append(doctor)
                break

        for doctor in assigned_doctors_list:
            if doctor.get_id()==doctor_id:
                assigned_doctors_list.remove(doctor)
                break

        unassigned_doctors_count += 1
        assigned_doctors_count -= 1

        Label(patda_subwin, text=f"COUNT: {assigned_doctors_count}", anchor='e', bg='#88C1C2', fg='white', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(patda_subwin, text=f"COUNT: {unassigned_doctors_count}", anchor='e',fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def changeColor(button, colorEntry, colorLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorEntry))
        button.bind("<Leave>", func=lambda e: button.config(background=colorLeave))

def pat_press(window, fulwidth, fulheight, doctors_list, patients_list, room_list, pa_doc_list, pa_room_list):
    global selected_patient
    selected_patient = -1

    pat_subwin = Toplevel()
    pat_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/Hospital_icon.png")
    pat_subwin.iconphoto(False, icon)
    pat_subwin.title("Patients Information Management")
    Frame(pat_subwin, bg='#88C1C2').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)

    assigned_doctors_list = []
    unassigned_doctors_list = []
    assigned_room_list = []
    unassigned_room_list = []

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview",
        background = "silver",
        foreground = "black",
        rowheight = 25,
        font=("Work Sans", 12),
        fieldbackground = "silver"
        )
    style.configure("Treeview.Heading", font=("Work Sans", 16,'bold'))
    
    style.map('Treeview', background=[('selected', '#88C1C2')])

    # Create TreeView List
    pat_tree = ttk.Treeview(pat_subwin, selectmode='browse', show='headings')

    # Define columns
    pat_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

    # Format columns
    pat_tree.column("#0", width=0, stretch=NO)
    pat_tree.column("ID", anchor='center', width=75)
    pat_tree.column("Name",anchor='w', width=150)
    pat_tree.column("Gender",anchor='center', width=75)
    pat_tree.column("Date of Birth",anchor='center', width=125)

    # Create Headings
    pat_tree.heading("#0", text="")
    pat_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(pat_tree, patients_list, "ID", False))
    pat_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(pat_tree, patients_list, "Name", False))
    pat_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(pat_tree, patients_list, "Gender", False))
    pat_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(pat_tree, patients_list, "Date of Birth", False))

    pat_tree.bind('<Motion>', 'break')

    # Insert Data
    for patient in patients_list:
        pat_tree.insert(parent='', index = 'end', iid=patient.get_id(), text='', values=(patient.get_id(), patient.get_name(), patient.get_gender(), patient.get_dob()))
        
    pat_tree.place(x=fulwidth/2+50, y=50, height=fulheight-250, width=fulwidth/2-100)

    #=========================================================================================

    Label(pat_subwin, bg='#88C1C2', fg='white', text='PATIENTS MANAGEMENT', font=("Work Sans", 20, 'bold')).place(x=50, y=25, width=fulwidth/2-100, height=50)
    Frame(pat_subwin, bg='crimson').place(x=50, y=85, width=fulwidth/2-100, height=2)
    entry_frame = Frame(pat_subwin, bg='#88C1C2')
    entry_frame.place(x=50, y=100, width=fulwidth/2-100, height=fulheight/2)
    Frame(pat_subwin, bg='crimson').place(x=50, y=350, width=fulwidth/2-100, height=2)
    Label(pat_subwin, text=' - Entries marked with " * " must not be empty ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=360, height=30)
    Label(pat_subwin, text=' - ID must be " P-xxx " ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=385, height=30)
    Label(pat_subwin, text=' - Gender must be " M " or " F " ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=410, height=30)
    Label(pat_subwin, text=' - Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=435, height=30)
    Label(pat_subwin, text=' - Phone & Debt must be numbers ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=460, height=30)

    # Column 0: ( * )
    Label(entry_frame, bg='#88C1C2', fg='red', text='( * )', font=("Work Sans", 14, 'bold')).grid(column=0, row=0)
    Label(entry_frame, bg='#88C1C2', fg='red', text='( * )', font=("Work Sans", 14, 'bold')).grid(column=0, row=1)
    Label(entry_frame, bg='#88C1C2', fg='red', text='( * )', font=("Work Sans", 14, 'bold')).grid(column=0, row=2)
    Label(entry_frame, bg='#88C1C2', fg='red', text='( * )', font=("Work Sans", 14, 'bold')).grid(column=0, row=3)
    
    # Column 1: |
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=0)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=1)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=2)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=3)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=4)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=5)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=6)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=7)

    # Column 2: Atribute
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - ID - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Name - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Gender - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - DoB - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Phone - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=4)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Email - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=5)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Illness - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=6)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Debt - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=7)

    # Column 3: |
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=0)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=1)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=2)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=3)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=4)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=5)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=6)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=7)
    
    # Column 4: Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    name_entry = Entry(entry_frame)
    name_entry.grid(column=4,row=1)

    gender_entry = Entry(entry_frame)
    gender_entry.grid(column=4,row=2)

    dob_entry = Entry(entry_frame)
    dob_entry.grid(column=4,row=3)

    phone_entry = Entry(entry_frame)
    phone_entry.grid(column=4,row=4)

    email_entry = Entry(entry_frame)
    email_entry.grid(column=4,row=5)

    illness_entry = Entry(entry_frame)
    illness_entry.grid(column=4,row=6)

    debt_entry = Entry(entry_frame)
    debt_entry.grid(column=4,row=7)

    # Column 5: |
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=3)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=4)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=5)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=6)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=7)

    #==============================================================================

    # Buttons
    add_patient_button = Button(pat_subwin, text='ADD PATIENT',anchor='center',font=("Work Sans", 12,'bold'), fg='#88C1C2', relief='ridge',
        activebackground='#88C1C2', activeforeground='white', command=lambda: pat_add(patients_list, pat_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry))
    add_patient_button.place(x=50, y=fulheight-75-85-10-50, width=150, height=50)
    changeColor(add_patient_button, "#c5ede2", "white")

    update_patient_button = Button(pat_subwin, text='UPDATE',anchor='center',font=("Work Sans", 12,'bold'), fg='#88C1C2', relief='ridge',
        activebackground='#88C1C2', activeforeground='white', command=lambda: pat_update(patients_list, pa_doc_list, pa_room_list, pat_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry))
    update_patient_button.place(x=fulwidth/2-50-150, y=fulheight-75-85-10-50, width=150, height=50)
    changeColor(update_patient_button, "#c5ede2", "white")

    clear_button = Button(pat_subwin, text='CLEAR',anchor='center',font=("Work Sans", 12,'bold'), fg='red', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry))
    clear_button.place(x=fulwidth/4*1-100, y=fulheight-75-85-10-50, width=200, height=50)
    changeColor(clear_button, "#f2dada", "white")

    remove_patient_button = Button(pat_subwin, text='REMOVE SELECTED',anchor='center',font=("Work Sans", 12,'bold'),bg='white', fg='red', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: pat_remove(patients_list, pat_tree, pa_doc_list, pa_room_list))
    remove_patient_button.place(x=fulwidth/4*3-100, y=fulheight-75-85, width=200, height=50)
    changeColor(remove_patient_button, "#f2dada", "white")

    remove_all_patient_button = Button(pat_subwin, text='REMOVE ALL',anchor='center',font=("Work Sans", 12,'bold'),bg='white', fg='red', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda:all_pat_remove(pat_tree, patients_list, pa_doc_list, pa_room_list))
    remove_all_patient_button.place(x=fulwidth-50-150, y=fulheight-75-85, width=150, height=50)
    changeColor(remove_all_patient_button, "#f2dada", "white")

    select_patient_button = Button(pat_subwin, text='SELECT',anchor='center',font=("Work Sans", 12,'bold'), bg='white',fg='#88C1C2', relief='ridge',
        activebackground='#88C1C2', activeforeground='white', command=lambda: pat_select(patients_list, pat_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry, illness_entry, debt_entry))
    select_patient_button.place(x=fulwidth/2+50, y=fulheight-75-85, width=150, height=50)
    changeColor(select_patient_button, "#c5ede2", "white")

    # doctors_assignment_button = Button(pat_subwin, text='DOCTORS ASSIGNMENT',anchor='center',font=("Work Sans", 12,'bold'), bg='white',fg='#88C1C2', relief='ridge',
    #     activebackground='#88C1C2', activeforeground='white', command=lambda: doctors_assignment(pat_subwin, pat_tree, fulwidth, fulheight, pa_doc_list, doctors_list, assigned_doctors_list, unassigned_doctors_list))
    # doctors_assignment_button.place(x=50,y=fulheight-75-85, width=fulwidth/4-60, height=50)
    # changeColor(doctors_assignment_button, "#c5ede2", "white")

    # room_assignment_button = Button(pat_subwin, text='ROOMS ASSIGNMENT',anchor='center',font=("Work Sans", 12,'bold'), bg='white',fg='#88C1C2', relief='ridge',
    #     activebackground='#88C1C2', activeforeground='white', command=lambda: room_asignment(pat_subwin, pat_tree, fulwidth, fulheight, pa_room_list, room_list, assigned_room_list, unassigned_room_list))
    # room_assignment_button.place(x=fulwidth/4+10,y=fulheight-75-85, width=fulwidth/4-60, height=50)
    # changeColor(room_assignment_button, "#c5ede2", "white")

    doctors_assignment_button = Button(pat_subwin, text='DOCTORS ASSIGNMENT',anchor='center',font=("Work Sans", 12,'bold'), bg='white',fg='#88C1C2', relief='ridge',
        activebackground='#88C1C2', activeforeground='white', command=lambda: doctors_assignment(pat_subwin, pat_tree, fulwidth, fulheight, pa_doc_list, doctors_list, assigned_doctors_list, unassigned_doctors_list))
    doctors_assignment_button.place(x=50,y=fulheight-75-85, width=fulwidth/2-100, height=50)
    changeColor(doctors_assignment_button, "#c5ede2", "white")