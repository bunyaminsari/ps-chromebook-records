# frontend of the app 
from tkinter import *
from app1_backend import Database

db = Database("chromebooks.db")

def selected_row(event):
    try:
        global selected_content
        index = student_list.curselection()[0]
        selected_content = student_list.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_content[1])

        e2.delete(0,END)
        e2.insert(END,selected_content[2])

        e3.delete(0,END)
        e3.insert(END,selected_content[3])

        e4.delete(0,END)
        e4.insert(END,selected_content[4])

        e5.delete(0,END)
        e5.insert(END,selected_content[5])

        e6.delete(0,END)
        e6.insert(END,selected_content[6])

        e7.delete(0,END)
        e7.insert(END,selected_content[7])

        e8.delete(0,END)
        e8.insert(END,selected_content[8])
    except IndexError:
        pass

# connecting the backend functions
def view_all():
    student_list.delete(0,END)
    for row in db.view():
        student_list.insert(END,row)

def search_record():
    student_list.delete(0,END)
    for row in db.search(en_date.get(),en_sname.get(),en_grade.get(),en_class.get(),en_pname.get(),en_psign.get(),en_cin.get(),en_ccn.get()):
        student_list.insert(END,row)
        
def add_record():
    try:
        if en_sname.get():
            db.insert(en_date.get(),en_sname.get(),en_grade.get(),en_class.get(),en_pname.get(),en_psign.get(),en_cin.get(),en_ccn.get())
            student_list.delete(0,END)
            student_list.insert(END,(en_date.get(),en_sname.get(),en_grade.get(),en_class.get(),en_pname.get(),en_psign.get(),en_cin.get(),en_ccn.get()))
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
    except:
        print("tcl Error")

def delete_record():
    db.delete(selected_content[0])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)

    view_all()


def update_record():
    db.update(selected_content[0],en_date.get(),en_sname.get(),en_grade.get(),en_class.get(),en_pname.get(),en_psign.get(),en_cin.get(),en_ccn.get())
    view_all()

def new_record():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)


window = Tk()
window.wm_title("Chromebook Agreement")


# GUI Components
#  Labels 
lb_title = Label(window,text="Public School, Chromebook Agreement".upper())
lb_title.grid(row=0,column=0,columnspan=4,pady=15)


lb_info = Label(window , text="By signing below, the student and his/her parent/guardian agree to follow and agree:")
lb_info.grid(row=1,column=0,columnspan=4)


lb_explanation = Label(window, text="- All policy and procedures as identified in the student handbook and acceptable use policy.\n\n- The 1:1 Handbook policy and procedures,that Public School owns the Chromebook,software, \nand issued perpherals.\n\n- If the student ceases to be enrolled in Public School, the student/parents will return the Chromebook \nin good working order or pay the full $200.00 replacement cost of the device. \n\n- The student will immediately report any problems or damage of the Chromebook \nto a member of the Public School admin team. \n\n- In no event shall Public School be held liable to any claim of damage,negligence, or breach of duty.")
lb_explanation.grid(row=2,column=0,columnspan=4)


lb_ps = Label(window,text="CIN: Chromebook Identification Number/Make, CCN: Chromebook Charger Number")
lb_ps.grid(row=3,column=0,columnspan=4,pady=25)




lb_date = Label(window,text="Date:")
lb_date.grid(row=4,column=0,sticky="e")

lb_sname = Label(window,text="Student's Name:")
lb_sname.grid(row=5,column=0,sticky="e")

lb_grade = Label(window,text="Grade:")
lb_grade.grid(row=6,column=0,sticky="e")

lb_class = Label(window,text="Class:")
lb_class.grid(row=7,column=0,sticky="e")

lb_pname = Label(window,text="Parent/Guardian Name:")
lb_pname.grid(row=4,column=2,sticky="e")

lb_psign = Label(window,text="Parent/Guardian Sign:")
lb_psign.grid(row=5,column=2,sticky="e")

lb_cin = Label(window,text="CIN:")
lb_cin.grid(row=6,column=2,sticky="e")

lb_ccn = Label(window,text="CCN:")
lb_ccn.grid(row=7,column=2,sticky="e")

# Entries

en_date = StringVar()
e1 = Entry(window,textvariable= en_date)
e1.grid(row =4,column=1)

en_sname = StringVar()
e2 = Entry(window,textvariable= en_sname)
e2.grid(row =5,column=1)

en_grade = StringVar()
e3 = Entry(window,textvariable= en_grade)
e3.grid(row =6,column=1)

en_class = StringVar()
e4 = Entry(window,textvariable= en_class)
e4.grid(row =7,column=1)

en_pname = StringVar()
e5 = Entry(window,textvariable= en_pname)
e5.grid(row =4,column=3)

en_psign = StringVar()
e6 = Entry(window,textvariable= en_psign)
e6.grid(row =5,column=3)

en_cin = StringVar()
e7 = Entry(window,textvariable= en_cin)
e7.grid(row =6,column=3)

en_ccn = StringVar()
e8 = Entry(window,textvariable= en_ccn)
e8.grid(row =7,column=3)


# Buttons 

b1 = Button(window,text="View All", width=23,height=2,command=view_all)
b1.grid(row=8,column=0,columnspan=2,sticky="e",padx=10,pady=6)

b2 = Button(window,text="Search", width=23,height=2,command=search_record)
b2.grid(row=8,column=2,columnspan=2,sticky="w",padx=10,pady=6)

b3 = Button(window,text="Add", width=23,height=2,command=add_record)
b3.grid(row=9,column=0,columnspan=2,sticky="e",padx=10,pady=6)

b4 = Button(window,text="Update", width=23,height=2,command=update_record)
b4.grid(row=9,column=2,columnspan=2,sticky="w",padx=10,pady=6)

b5 = Button(window,text="Delete", width=23,height=2,command=delete_record)
b5.grid(row=10,column=0,columnspan=2,sticky="e",padx=10,pady=6)

b6 = Button(window,text="Close", width=23,height=2,command=window.destroy)
b6.grid(row=11,column=0,columnspan=2,sticky=E,padx=10,pady=6)

b7 = Button(window,text="Clear", width=23,height=2,command=new_record)
b7.grid(row=10,column=2,columnspan=2,sticky="w",padx=10,pady=6)


# Listbox and scrollbar 

student_list= Listbox(window,height=6,width=40)
student_list.grid(row=12,column=0,rowspan=6,columnspan=3,sticky=E,padx=10,pady=10)

sb1 = Scrollbar(window)
sb1.grid(row=12,column=3,rowspan=6,sticky=W)

student_list.configure(yscrollcommand=sb1.set)
sb1.configure(command=student_list.yview)

# get the selected row from Listox to use Delete and Update Commands
student_list.bind('<<ListboxSelect>>',selected_row)

window.resizable(0,0)
window.mainloop()
