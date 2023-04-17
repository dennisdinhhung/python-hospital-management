from domains.Person import *
from domains.classConnection import *
from domains.Employee import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
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
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    dept_entry.delete(0, END)
    salary_entry.delete(0, END)

    # Set selected_employee to -1
    global selected_employee
    selected_employee = -1
    
def emp_add(employee_list, emp_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
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
    gend = gend_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    dept = dept_entry.get()
    salary = salary_entry.get()

    # Validation
    valid_check = 0
    
    #Validate ID
    if len(id) == 0:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "W-") == 1:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for employee in employee_list:
            if employee.get_id() == id:
                Label(entry_frame, bg='#88C1C2', fg='crimson', text='ID already exist', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break
    
    # Validate Name
    if len(name) == 0:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1

    # Validate Gender
    if len(gend) == 0:
        Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_gend(gend) == 1:
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
    if len(phone) != 0:
        if utils.invalid_phone(phone) == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1

    if len(salary) != 0:
        if utils.invalid_salary(salary) == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1

    # If All Valid
    if valid_check == 0:
        # Add to employee_list
        new_emp = Employee(id, name, gend, dob)
        if len(phone) > 0:
            new_emp.set_phone(phone)
        if len(email) > 0:
            new_emp.set_email(email)
        if len(dept) > 0:
            new_emp.set_dept(dept)
        if len(salary) > 0:
            new_emp.set_salary(salary)
        employee_list.append(new_emp)

        # Display on Treeview
        emp_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name, gend, dob))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gend_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        dept_entry.delete(0, END)
        salary_entry.delete(0, END)

def emp_remove(employee_list, emp_tree):
    if len(emp_tree.selection())>0:
        selected_emp = emp_tree.selection()[0]
        employee_id = emp_tree.item(selected_emp, 'values')[0]
        for employee in employee_list:
            if employee.get_id()== employee_id:
                employee_list.remove(employee)
                break
        emp_tree.delete(selected_emp)

def all_emp_remove(emp_tree, employee_list):
    for emp in emp_tree.get_children():
        emp_tree.delete(emp)
    employee_list.clear()

def emp_select(employee_list, emp_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
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
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    dept_entry.delete(0, END)
    salary_entry.delete(0, END)

    # Show Selected employee Info
    if len(emp_tree.selection())>0:
        global selected_employee
        selected_employee = emp_tree.selection()[0]
        emp_id = emp_tree.item(selected_employee, 'values')[0]
        for employee in employee_list:
            if employee.get_id()== emp_id:
                id_entry.insert(0, employee.get_id())
                name_entry.insert(0, employee.get_name())
                gend_entry.insert(0, employee.get_gender())
                dob_entry.insert(0, employee.get_dob())
                phone_entry.insert(0, employee.get_phone())
                email_entry.insert(0, employee.get_email())
                dept_entry.insert(0, employee.get_dept())
                salary_entry.insert(0, employee.get_salary())
                break

def emp_update(employee_list, emp_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry):
    global selected_employee
    if selected_employee != -1:
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
        gend = gend_entry.get()
        dob = dob_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        dept = dept_entry.get()
        salary = salary_entry.get()
            
        # Validation
        valid_check = 0
        
        #Validate ID
        if len(id) == 0:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "E-") == 1:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if id != emp_tree.item(selected_employee, 'values')[0]:
                for employee in employee_list:
                    if employee.get_id() == id:
                        Label(entry_frame, bg='#88C1C2', fg='crimson', text='ID already exist', font=("Work Sans", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
        
        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Gender
        if len(gend) == 0:
            Label(entry_frame, bg='#88C1C2', fg='crimson', text='EMPTY', font=("Work Sans", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_gend(gend) == 1:
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

        if len(salary) != 0:
            if utils.invalid_salary(salary) == 1:
                Label(entry_frame, bg='#88C1C2', fg='crimson', text='INVALID', font=("Work Sans", 14, 'bold')).grid(column=6,row=7,sticky='w')
                valid_check += 1

        # If All Valid
        if valid_check == 0:
            for employee in employee_list:
                if employee.get_id() == emp_tree.item(selected_employee, 'values')[0]:
                    employee.set_id(id)
                    employee.set_name(name)
                    employee.set_gend(gend)
                    employee.set_dob(dob)
                    if len(phone) > 0:
                        employee.set_phone(phone)
                    elif len(phone) == 0:
                        employee.set_phone('_')
                    if len(email) > 0:
                        employee.set_email(email)
                    elif len(email) == 0:
                        employee.set_email('_')
                    if len(dept) > 0:
                        employee.set_dept(dept)
                    elif len(dept) == 0:
                        employee.set_dept('_')
                    if len(salary) > 0:
                        employee.set_salary(salary)
                    elif len(salary) == 0:
                        employee.set_salary(0)
                    break
            emp_tree.item(selected_employee, text="", values = (id, name, gend, dob))
            selected_employee = -1
        
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            gend_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            dept_entry.delete(0, END)
            salary_entry.delete(0, END)

def changeColor(button, colorEntry, colorLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorEntry))
        button.bind("<Leave>", func=lambda e: button.config(background=colorLeave))

def emp_press(window, fulwidth, fulheight, employee_list):
    global selected_employee
    selected_employee = -1

    emp_subwin = Toplevel()
    emp_subwin.geometry("%dx%d" % (fulwidth, fulheight))
    icon = PhotoImage(file = "images/Hospital_icon.png")
    emp_subwin.iconphoto(False, icon)
    emp_subwin.title("Emplyees Information Management")
    Frame(emp_subwin, bg='#88C1C2').place(x=0, y=0 ,width=fulwidth/2, height=fulheight)
    

    #=====================================================================================
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
    emp_tree = ttk.Treeview(emp_subwin, selectmode='browse', show='headings')

    # Define columns
    emp_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth")

    # Format columns
    emp_tree.column("#0", width=0, stretch=NO)
    emp_tree.column("ID", anchor='center', width=75)
    emp_tree.column("Name",anchor='w', width=150)
    emp_tree.column("Gender",anchor='center', width=75)
    emp_tree.column("Date of Birth",anchor='center', width=125)

    # Create Headings
    emp_tree.heading("#0", text="")
    emp_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(emp_tree, employee_list, "ID", False))
    emp_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(emp_tree, employee_list, "Name", False))
    emp_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(emp_tree, employee_list, "Gender", False))
    emp_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(emp_tree, employee_list, "Date of Birth", False))

    emp_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for employee in employee_list:
        emp_tree.insert(parent='', index = 'end', iid=employee.get_id(), text='', values=(employee.get_id(), employee.get_name(), employee.get_gender(), employee.get_dob()))
        
    emp_tree.place(x=fulwidth/2+50, y=50, height=fulheight-250, width=fulwidth/2-100)
    #=========================================================================================
    
    # Emplyee Control
    Label(emp_subwin, bg='#88C1C2', fg='white', text='EMPLOYEE MANAGEMENT', font=("Work Sans", 20, 'bold')).place(x=50, y=25, width=fulwidth/2-100, height=50)
    Frame(emp_subwin, bg='crimson').place(x=50, y=85, width=fulwidth/2-100, height=2)
    entry_frame = Frame(emp_subwin, bg='#88C1C2')
    entry_frame.place(x=50, y=100, width=fulwidth/2-100, height=fulheight/2)
    Frame(emp_subwin, bg='crimson').place(x=50, y=350, width=fulwidth/2-100, height=2)
    Label(emp_subwin, text=' Entries marked with " * " must not be empty ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=360, height=30)
    Label(emp_subwin, text=' ID must be " E-xxx " ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=385, height=30)
    Label(emp_subwin, text=' Gender must be " M " or " F " ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=410, height=30)
    Label(emp_subwin, text=' Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=435, height=30)
    Label(emp_subwin, text=' Phone & Salary must be numbers ', anchor='w', bg='#88C1C2', fg='white', font=("Work Sans", 12, 'bold')).place(x=50, y=460, height=30)


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
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Dept - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=6)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' - Salary - ', font=("Work Sans", 14, 'bold')).grid(column=2, row=7)

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

    gend_entry = Entry(entry_frame)
    gend_entry.grid(column=4,row=2)

    dob_entry = Entry(entry_frame)
    dob_entry.grid(column=4,row=3)

    phone_entry = Entry(entry_frame)
    phone_entry.grid(column=4,row=4)

    email_entry = Entry(entry_frame)
    email_entry.grid(column=4,row=5)

    dept_entry = Entry(entry_frame)
    dept_entry.grid(column=4,row=6)

    salary_entry = Entry(entry_frame)
    salary_entry.grid(column=4,row=7)

    # Column 5: |
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=0)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=1)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=2)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=3)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=4)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=5)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=6)
    Label(entry_frame, bg='#88C1C2', fg='white', text=' | ', font=("Work Sans", 14, 'bold')).grid(column=5, row=7)

    # Buttons
    add_employee_button = Button(emp_subwin, text='ADD EMPLOYEE',anchor='center',font=("Work Sans", 12,'bold'), fg='#88C1C2', relief='ridge',
        activebackground='#88C1C2', activeforeground='white', command=lambda: emp_add(employee_list, emp_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    add_employee_button.place(x=50, y=fulheight-75-85-10-50, width=250, height=50)
    changeColor(add_employee_button, "#c5ede2", "white")
    
    update_employee_button = Button(emp_subwin, text='UPDATE',anchor='center',font=("Work Sans", 12,'bold'), fg='#88C1C2', relief='ridge',
        activebackground='#88C1C2', activeforeground='white', command=lambda: emp_update(employee_list, emp_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    update_employee_button.place(x=300, y=fulheight-75-85-10-50, width=250, height=50)
    changeColor(update_employee_button, "#c5ede2", "white")
    
    clear_button = Button(emp_subwin, text='CLEAR',anchor='center',font=("Work Sans", 12,'bold'), fg='red', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    clear_button.place(x=50, y=fulheight-75-85-10, width=500, height=50)
    changeColor(clear_button, "#f2dada", "white")

    remove_employee_button = Button(emp_subwin, text='REMOVE SELECTED',anchor='center',font=("Work Sans", 12,'bold'),bg='white', fg='red', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: emp_remove(employee_list, emp_tree))
    remove_employee_button.place(x=fulwidth/4*3-100, y=fulheight-75-85, width=200, height=50)
    changeColor(remove_employee_button, "#f2dada", "white")

    remove_all_employee_button = Button(emp_subwin, text='REMOVE ALL',anchor='center',font=("Work Sans", 12,'bold'),bg='white', fg='red', relief='ridge',
        activebackground='crimson', activeforeground='white', command=lambda: all_emp_remove(emp_tree, employee_list))
    remove_all_employee_button.place(x=fulwidth-50-150, y=fulheight-75-85, width=150, height=50)
    changeColor(remove_all_employee_button, "#f2dada", "white")

    select_employee_button = Button(emp_subwin, text='SELECT',anchor='center',font=("Work Sans", 12,'bold'), bg='white',fg='#88C1C2', relief='ridge',
        activebackground='#88C1C2', activeforeground='white', command=lambda: emp_select(employee_list, emp_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, dept_entry, salary_entry))
    select_employee_button.place(x=fulwidth/2+50, y=fulheight-75-85, width=150, height=50)
    changeColor(select_employee_button, "#c5ede2", "white")