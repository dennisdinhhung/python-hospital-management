from src.domains.Person import *
from src.domains.classConnection import *
from src.domains.Room import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, name_entry, description_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#ceede8', fg='white', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    description_entry.delete('1.0', END)

    # Set selected_patient to -1
    global selected_room
    selected_room = -1

def room_add(room_list, room_tree, entry_frame, id_entry, name_entry, description_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#ceede8', fg='white', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Read Inputs
    id = id_entry.get()
    name = name_entry.get()
    description = description_entry.get("1.0",'end-1c')

    # Validation
    valid_check = 0

    # Validate ID
    if len(id) == 0:
        Label(entry_frame, bg='#ceede8', fg='white', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "M-") == 1:
        Label(entry_frame, bg='#ceede8', fg='white', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for room in room_list:
            if room.get_id() == id:
                Label(entry_frame, bg='#ceede8', fg='white', text='ID already exist', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break

    # Validate Name
    if len(name) == 0:
        Label(entry_frame, bg='#ceede8', fg='white', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1


        # Display on Treeview
        room_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        description_entry.delete('1.0', END)

def room_remove(room_list, room_tree, pa_room_list):
    if len(room_tree.selection())>0:
        selected_room = room_tree.selection()[0]
        room_id = room_tree.item(selected_room, 'values')[0]

        for relation in pa_room_list:
            if relation.get_roomID() == room_id:
                pa_room_list.remove(relation)

        for room in room_list:
            if room.get_id()== room_id:
                room_list.remove(room)
                break

        room_tree.delete(selected_room)

def all_room_remove(room_tree, room_list, pa_room_list):
    for room in room_tree.get_children():
        room_tree.delete(room)
    pa_room_list.clear()
    room_list.clear()

def room_select(room_list, room_tree, entry_frame, id_entry, name_entry, description_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#ceede8', fg='white', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    description_entry.delete('1.0', END)

    # Show Selected Patient Info
    if len(room_tree.selection())>0:
        global selected_room
        selected_room = room_tree.selection()[0]
        room_id = room_tree.item(selected_room, 'values')[0]

        for room in room_list:
            if room.get_id()== room_id:
                id_entry.insert(0, room.get_id())
                name_entry.insert(0, room.get_name())
                description_entry.insert('0.1', room.get_description())
                break

def room_update(room_list, pa_room_list, room_tree, entry_frame, id_entry, name_entry, description_entry):
    global selected_room
    if selected_room != -1:
        # Delete all Warnings
        Label(entry_frame, bg='#ceede8', fg='white', text='                                  ', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#ceede8', fg='white', text='                   ', font=("Work Sans", 14, 'bold')).grid(column=6,row=3,sticky='w')

        # Read Inputs
        id = id_entry.get()
        name = name_entry.get()
        description = description_entry.get("1.0",'end-1c')

        # Validation
        valid_check = 0

        # Validate ID
        if len(id) == 0:
            Label(entry_frame, bg='#ceede8', fg='white', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "M-") == 1:
            Label(entry_frame, bg='#ceede8', fg='white', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            if id != room_tree.item(selected_room, 'values')[0]:
                for room in room_list:
                    if room.get_id() == id:
                        Label(entry_frame, bg='#ceede8', fg='white', text='ID already exist', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break

        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg='#ceede8', fg='white', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

 
        # If ALL Valid
        if valid_check == 0:
            for room in room_list:
                if room.get_id() == room_tree.item(selected_room, 'values')[0]:
                    room.set_id(id)
                    room.set_name(name)
                    room.set_description(description)
            for relation in pa_room_list:
                if relation.get_roomID() == room_tree.item(selected_room, 'values')[0]:
                    relation.set_roomID(id)

            room_tree.item(selected_room, text="", values = (id, name))
            selected_room = -1

            # Empty Entry boxes
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            description_entry.delete('1.0', END)

def patients_assignment(room_subwin, room_tree, fulwidth, fulheight, pa_room_list, patients_list, assigned_patients_list, unassigned_patients_list):
    if selected_room != -1:    
        roompa_subwin = Toplevel(room_subwin)
        roompa_subwin.geometry("%dx%d" % (fulwidth, fulheight))
        icon = PhotoImage(file = "images/HIMS Icon.png")
        roompa_subwin.iconphoto(False, icon)
        roompa_subwin.title("room _ Patients Assignment")
        Frame(roompa_subwin, bg='#ceede8').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
        Label(roompa_subwin, text='ASSIGNED PATIENTS', bg='#ceede8', fg='white', font=("Work Sans", 20, 'bold')).place(x=50,y=50,width=fulwidth/2-100,height=50)
        Label(roompa_subwin, text='UNASSIGNED PATIENTS', fg='#ceede8', font=("Work Sans", 20, 'bold')).place(x=fulwidth/2+50,y=50,width=fulwidth/2-100,height=50)

        # Create list of assigned and unassigned patients for selected doctor
        assigned_patients_list.clear()
        unassigned_patients_list.clear()

        room_id = room_tree.item(selected_room, 'values')[0]
        temp_list = []
        for relation in pa_room_list:
            if relation.get_roomID() == room_id:
                temp_list.append(relation)
        for patient in patients_list:
            check = 0
            for relation in temp_list:
                if patient.get_id() == relation.get_PatientID():
                    check += 1
                    break
            if check == 0:
                unassigned_patients_list.append(patient)
            else:
                assigned_patients_list.append(patient)
        temp_list.clear()

        # Unassigned treeview
        # create Treeview
        unassigned_patients_tree = ttk.Treeview(roompa_subwin, selectmode='browse', show='headings')

        # define columns
        unassigned_patients_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

        # Format columns
        unassigned_patients_tree.column("#0", width=0, stretch=NO)
        unassigned_patients_tree.column("ID", anchor='center', width=75)
        unassigned_patients_tree.column("Name",anchor='w', width=150)
        unassigned_patients_tree.column("Gender",anchor='center', width=75)
        unassigned_patients_tree.column("Date of Birth",anchor='center', width=125)

        # Create Headings
        unassigned_patients_tree.heading("#0", text="")
        unassigned_patients_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "ID", False))
        unassigned_patients_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Name", False))
        unassigned_patients_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Gender", False))
        unassigned_patients_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Date of Birth", False))

        unassigned_patients_tree.bind('<Motion>', 'break')

        # Insert Data
        global unassigned_patients_count
        unassigned_patients_count = 0
        for patient in unassigned_patients_list:
            unassigned_patients_tree.insert(parent='', index = 'end', iid=patient.get_id(), text='', values=(patient.get_id(), patient.get_name(), patient.get_gend(), patient.get_dob()))
            unassigned_patients_count += 1

        unassigned_patients_tree.place(x=fulwidth/2+50, y=100, height=fulheight-300, width=fulwidth/2-100)

        #==========================================================================================
        # Assigned treeview
        assigned_patients_tree = ttk.Treeview(roompa_subwin, selectmode='browse', show='headings')

        # define columns
        assigned_patients_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

        # Format columns
        assigned_patients_tree.column("#0", width=0, stretch=NO)
        assigned_patients_tree.column("ID", anchor='center', width=75)
        assigned_patients_tree.column("Name",anchor='w', width=150)
        assigned_patients_tree.column("Gender",anchor='center', width=75)
        assigned_patients_tree.column("Date of Birth",anchor='center', width=125)

        # Create Headings
        assigned_patients_tree.heading("#0", text="")
        assigned_patients_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "ID", False))
        assigned_patients_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Name", False))
        assigned_patients_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Gender", False))
        assigned_patients_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Date of Birth", False))

        assigned_patients_tree.bind('<Motion>', 'break')

        # Insert Data
        global assigned_patients_count
        assigned_patients_count = 0
        for patient in assigned_patients_list:
            assigned_patients_tree.insert(parent='', index = 'end', iid=patient.get_id(), text='', values=(patient.get_id(), patient.get_name(), patient.get_gend(), patient.get_dob()))
            assigned_patients_count += 1

        assigned_patients_tree.place(x=50, y=100, height=fulheight-300, width=fulwidth/2-100)

        # ===============================================================================

        Label(roompa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='#ceede8', fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(roompa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

        # Buttons
        assign_patient_button = Button(roompa_subwin, text='ASSIGN PATIENT', font=("Work Sans", 16, 'bold'), fg='white', bg='#ceede8', relief='ridge',
            activebackground='dark blue', activeforeground='white', command=lambda: assign_patient(roompa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, room_id, pa_room_list))
        assign_patient_button.place(x=fulwidth/2+50, y=fulheight-150, width=250, height=50)

        unassign_patient_button = Button(roompa_subwin, text='UNASSIGN PATIENT', font=("Work Sans", 16, 'bold'), fg='#ceede8', relief='ridge',
            activebackground='dark blue', activeforeground='white', command=lambda: unassign_patient(roompa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, room_id, pa_room_list))
        unassign_patient_button.place(x=50, y=fulheight-150, width=250, height=50)

def assign_patient(roompa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, room_id, pa_room_list):
    if len(unassigned_patients_tree.selection())>0:
        selected_unassigned_patient = unassigned_patients_tree.selection()[0]
        patient_id = unassigned_patients_tree.item(selected_unassigned_patient, 'values')[0]

        pa_room_list.append(PatientAndRoom(patient_id, room_id))
        global unassigned_patients_count
        global assigned_patients_count

        assigned_patients_tree.insert(parent='', index = 'end', iid=patient_id, text='', values=(unassigned_patients_tree.item(selected_unassigned_patient, 'values')))
        unassigned_patients_tree.delete(selected_unassigned_patient)
        
        for patient in patients_list:
            if patient.get_id()==patient_id:
                assigned_patients_list.append(patient)
                break

        for patient in unassigned_patients_list:
            if patient.get_id()==patient_id:
                unassigned_patients_list.remove(patient)
                break
        unassigned_patients_count -= 1
        assigned_patients_count += 1
        Label(roompa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='#ceede8', fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(roompa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def unassign_patient(roompa_subwin, fulwidth, fulheight, assigned_patients_tree, unassigned_patients_tree, assigned_patients_list, unassigned_patients_list, patients_list, room_id, pa_room_list):
    if len(assigned_patients_tree.selection())>0:
        selected_assigned_patient = assigned_patients_tree.selection()[0]
        patient_id = assigned_patients_tree.item(selected_assigned_patient, 'values')[0]

        for relation in pa_room_list:
            if relation.get_PatientID() == patient_id and relation.get_roomID() == room_id:
                pa_room_list.remove(relation)
    
        global unassigned_patients_count
        global assigned_patients_count

        unassigned_patients_tree.insert(parent='', index = 'end', iid=patient_id, text='', values=(assigned_patients_tree.item(selected_assigned_patient, 'values')))
        assigned_patients_tree.delete(selected_assigned_patient)

        for patient in patients_list:
            if patient.get_id()==patient_id:
                unassigned_patients_list.append(patient)
                break

        for patient in assigned_patients_list:
            if patient.get_id()==patient_id:
                assigned_patients_list.remove(patient)
                break
        unassigned_patients_count += 1
        assigned_patients_count -= 1
            
        Label(roompa_subwin, text=f"COUNT: {assigned_patients_count}", anchor='e', bg='#ceede8', fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4+50,y=fulheight-150,width=200,height=50)
        Label(roompa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor='e',fg='black', font=("Work Sans", 16, 'bold')).place(x=fulwidth/4*3+50,y=fulheight-150,width=200,height=50)

def room_press(window, fulwidth, fulheight, room_list, patients_list, pa_room_list):
    global selected_room
    selected_room = -1

    room_subwin = Toplevel(window)
    room_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/HIMS Icon.png")
    room_subwin.iconphoto(False, icon)
    room_subwin.title("room Information Management")
    Frame(room_subwin, bg='#ceede8').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
    
    assigned_patients_list = []
    unassigned_patients_list = []

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview",
        background = "white",
        foreground = "black",
        rowheight = 25,
        font=("Work Sans", 12),
        fieldbackground = "white"
        )
    style.configure("Treeview.Heading", font=("Work Sans", 16,'bold'))
    
    style.map('Treeview', background=[('selected', 'dark blue')])

    # Create TreeView List
    room_tree = ttk.Treeview(room_subwin, selectmode='browse', show='headings')

    # Define columns
    room_tree['columns'] = ("ID", "Name")

    # Format columns
    room_tree.column("#0", width=0, stretch=NO)
    room_tree.column("ID", anchor='center', width=75)
    room_tree.column("Name",anchor='w', width=150)

    # Create Headings
    room_tree.heading("#0", text="")
    room_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "ID", False))
    room_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "Name", False))

    room_tree.bind('<Motion>', 'break')

    # Insert Data
    for room in room_list:
        room_tree.insert(parent='', index = 'end', iid=room.get_id(), text='', values=(room.get_id(), room.get_name()))
        
    room_tree.place(x=fulwidth/2+50, y=50, height=fulheight-250, width=fulwidth/2-100)

    #=====================================================================================
    Label(room_subwin, bg='#ceede8', fg='white', text='room MANAGEMENT', font=("Work Sans", 20, 'bold')).place(x=50, y=25, width=fulwidth/2-100, height=50)
    Frame(room_subwin, bg='white').place(x=50, y=85, width=fulwidth/2-100, height=2)
    entry_frame = Frame(room_subwin, bg='#ceede8')
    entry_frame.place(x=50, y=100, width=fulwidth/2-100, height=fulheight/2)
    Frame(room_subwin, bg='white').place(x=50, y=350, width=fulwidth/2-100, height=2)
    text_frame = Frame(room_subwin, bg='#ceede8')
    text_frame.place(x=50, y=fulheight/2-140, width=fulwidth/2-100, height=115)

    # Column 0: ( * )
    Label(entry_frame, bg='#ceede8', fg='red', text='( * )', font=("Work Sans", 14, 'bold')).grid(column=0, row=0)
    Label(entry_frame, bg='#ceede8', fg='red', text='( * )', font=("Work Sans", 14, 'bold')).grid(column=0, row=1)
    Label(entry_frame, bg='#ceede8', fg='red', text='( * )', font=("Work Sans", 14, 'bold')).grid(column=0, row=2)

    # Column 1: |
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=0)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=1)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=2)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=1, row=3)

    # Column 2: Atribute
    Label(entry_frame, bg='#ceede8', fg='white', text=' - ID - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#ceede8', fg='white', text=' - Name - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=1)
    
    # Column 3: |
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=0)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=1)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=2)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=3, row=3)

    # Column 4: Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    name_entry = Entry(entry_frame)
    name_entry.grid(column=4,row=1)



    # Column 5: |
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='#ceede8', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=3)

    # Description
    Label(text_frame, bg='#ceede8', fg='white', text=' - Description - ', font=("Work Sans", 14, 'bold')).grid(column=0, row=0)
    description_entry = Text(text_frame, width=65, height=5)
    description_entry.grid(row=1, column=0, columnspan=5)

    #==================================================================================

    Label(room_subwin, text='  - Entries marked with " * " must not be empty ', anchor='w', bg='#ceede8', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=360, height=30)
    Label(room_subwin, text='  - ID must be " M-xxx " ', anchor='w', bg='#ceede8', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=385, height=30)
  
    add_room_button = Button(room_subwin, text='ADD room',anchor='center',font=("Work Sans", 12,'bold'), fg='#ceede8', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_add(room_list, room_tree, entry_frame, id_entry, name_entry, description_entry))
    add_room_button.place(x=50, y=fulheight-75-85-10-50, width=150, height=50)

    update_room_button = Button(room_subwin, text='UPDATE',anchor='center',font=("Work Sans", 12,'bold'), fg='#ceede8', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_update(room_list, pa_room_list, room_tree, entry_frame, id_entry, name_entry, description_entry))
    update_room_button.place(x=fulwidth/2-50-150, y=fulheight-75-85-10-50, width=150, height=50)

    clear_button = Button(room_subwin, text='CLEAR',anchor='center',font=("Work Sans", 12,'bold'), fg='red', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, description_entry))
    clear_button.place(x=fulwidth/4*1-100, y=fulheight-75-85-10-50, width=200, height=50)

    remove_room_button = Button(room_subwin, text='REMOVE SELECTED',anchor='center',font=("Work Sans", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='white', activeforeground='white', command=lambda: room_remove(room_list, room_tree, pa_room_list))
    remove_room_button.place(x=fulwidth/4*3-100, y=fulheight-75-85, width=200, height=50)

    remove_all_room_button = Button(room_subwin, text='REMOVE ALL',anchor='center',font=("Work Sans", 12,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='white', activeforeground='white', command=lambda: all_room_remove(room_tree, room_list, pa_room_list))
    remove_all_room_button.place(x=fulwidth-50-150, y=fulheight-75-85, width=150, height=50)

    select_room_button = Button(room_subwin, text='SELECT',anchor='center',font=("Work Sans", 12,'bold'), bg='#ceede8',fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_select(room_list, room_tree, entry_frame, id_entry, name_entry, description_entry))
    select_room_button.place(x=fulwidth/2+50, y=fulheight-75-85, width=150, height=50)

    patients_assignment_button = Button(room_subwin, text='PATIENTS ASSIGNMENT',anchor='center',font=("Work Sans", 12,'bold'), fg='#ceede8', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: patients_assignment(room_subwin, room_tree, fulwidth, fulheight, pa_room_list, patients_list, assigned_patients_list, unassigned_patients_list))
    patients_assignment_button.place(x=50,y=fulheight-75-85, width=fulwidth/2-100, height=50)