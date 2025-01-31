from tkinter import *
from classes import *

with open('course.txt') as file:
    courseName = file.readline()
course = Course(courseName)

# Root Functions

# Function for the Reports label
def report_click():
    # Functions for the function

    def gen_click():
        stdLst = []
        courseLst = []
        gradeLst = []
        repLst = []

        with open("names.txt") as file:
            stdNames = file.readlines()
        with open("grades.txt") as file:
            stdGrades = file.readlines()
        with open("attendance.txt") as file:
            stdAttendance = file.readlines()
        with open("IDs.txt") as file:
            stdIDS = file.readlines()

        stdNames = [name.strip() for name in stdNames]
        stdGrades = [grade.strip() for grade in stdGrades]
        stdAttendance = [attendance.strip() for attendance in stdAttendance]
        stdIDS = [id.strip() for id in stdIDS]

        for i in range(len(stdNames)):
            stdLst.append(Student(stdNames[i], stdIDS[i], stdAttendance[i]))
        for i in range(len(stdNames)):
            courseLst.append(Course(courseName))
        for i in range(len(stdGrades)):
            gradeLst.append(Grade(stdGrades[i]))
        for i in range(len(stdNames)):
            repLst.append(Report(courseLst[i], stdLst[i], gradeLst[i]))

        start_x = 125
        start_y = 115
        padding_y = 25

        for i in range(len(repLst)):
            stdLabel = Label(rep, text=f"{repLst[i].report_generator()}", font=("Consolas", 11), borderwidth=2, relief="groove")
            stdLabel.place(x=start_x, y=start_y + i * padding_y)
    # Window Setup

    rep = Toplevel(root)
    rep.title("Reports")
    rep.geometry("1000x600")
    rep.resizable(False, False)

    # Rep Widgets

    rep_uopLogo = PhotoImage(file="assets/UOP.png")
    uopLabel3 = Label(rep, image=rep_uopLogo)
    uopLabel3.image = rep_uopLogo

    genButton = Button(rep, text="Generate Report", font=("Consolas", 17), bd=5, command=lambda: gen_click())

    # Widget Placement

    uopLabel3.place(x=400, y=15)
    genButton.place(x=400, y=525)

# Function for the Students label

def students_click():

    global counter # Counter for adding / deleting student entries
    counter = 0

    global stdList # List for saving the student information later on
    stdList = []

    global names # List of all the names of the students
    names = []

    global grades # A tuple of all the grades of the students
    grades = ()

    global attendance # A tuple of all the attendance records of the students
    attendance = ()

    global studentIDs # List of all student IDs
    studentIDs = []

    # Function for the property gear

    def properties(num):

        # Function for the apply button

        def apply_click():
            updated_text = f"Name: {nameEntry.get()} | Student ID: {IDEntry.get()} | Grade: {gradeEntry.get()}/100 | Attendance: {attendanceEntry.get()}/48"
            stdList[num-1] = updated_text # Update the list entry for saving it later
            if num == 1:
                stdLabel1.config(text=updated_text)
            elif num == 2:
                stdLabel2.config(text=updated_text)
            elif num == 3:
                stdLabel3.config(text=updated_text)
            elif num == 4:
                stdLabel4.config(text=updated_text)
            elif num == 5:
                stdLabel5.config(text=updated_text)
            elif num == 6:
                stdLabel6.config(text=updated_text)
            elif num == 7:
                stdLabel7.config(text=updated_text)
            elif num == 8:
                stdLabel8.config(text=updated_text)
            elif num == 9:
                stdLabel9.config(text=updated_text)
            elif num == 10:
                stdLabel10.config(text=updated_text)
            elif num == 11:
                stdLabel11.config(text=updated_text)
            elif num == 12:
                stdLabel12.config(text=updated_text)
            elif num == 13:
                stdLabel13.config(text=updated_text)
            elif num == 14:
                stdLabel14.config(text=updated_text)
            elif num == 15:
                stdLabel15.config(text=updated_text)

        # Window Setup

        prop = Toplevel(std)
        prop.title(f"Properties ({num})")
        prop.geometry("325x200")
        prop.resizable(False, False)

        # Properties Widgets

        nameLabel = Label(prop, text="Name:", font=("Consolas", 12))
        nameEntry = Entry(prop, font=("Consolas", 12))
        IDLabel = Label(prop, text="ID: ", font=("Consolas", 12))
        IDEntry = Entry(prop, font=("Consolas", 12))
        gradeLabel = Label(prop, text="Grade: ", font=("Consolas", 12))
        gradeEntry = Entry(prop, font=("Consolas", 12))
        attendanceLabel = Label(prop, text="Attendance: ", font=("Consolas", 12))
        attendanceEntry = Entry(prop, font=("Consolas", 12))
        applyButton = Button(prop, text="Apply", font=("Consolas", 18), command=lambda: apply_click())

        # Widgets Placement

        nameLabel.grid(row=0, column=0)
        nameEntry.grid(row=0, column=1)
        IDLabel.grid(row=1, column=0)
        IDEntry.grid(row=1, column=1)
        gradeLabel.grid(row=2, column=0)
        gradeEntry.grid(row=2, column=1)
        attendanceLabel.grid(row=3, column=0)
        attendanceEntry.grid(row=3, column=1)
        applyButton.place(x=115, y=125)

    # Function for the avg button

    def avg_click():
        with open("grades.txt") as file:
            grades = file.readlines()
            total = 0.0
            count = 0
            for i in grades:
                total += float(i)
                count += 1
            avg = total/count

        avgLabel = Label(std, text="Avg= " + str(avg), font=("Consolas", 22))
        avgLabel.place(x=850, y=525)

    # Function for the save button

    def save_click():
        gradesLst = []
        attendanceList = []
        with open("full-student-info.txt", 'w') as file:
            for i in stdList:
                file.write(i + "\n")

        for i in stdList:
            a = i.split(": ")
            b = a[3].split("/100 |")
            c = b[0]
            gradesLst.append(int(c))
        grades = tuple(gradesLst)

        with open("grades.txt", 'w') as file:
            for i in grades:
                file.write(str(i) + "\n")

        for i in stdList:
            a = i.split(": ")
            b = a[1].split(" | ")
            c = b[0]
            names.append(c)
        with open("names.txt", 'w') as file:
            for i in names:
                file.write(i + "\n")

        for i in stdList:
            a = i.split(": ")
            b = a[4].split("/48")
            c = b[0]
            attendanceList.append(c)
        attendance = tuple(attendanceList)
        with open("attendance.txt", 'w') as file:
            for i in attendance:
                file.write(str(i) + "\n")

        for i in stdList:
            a = i.split(": ")
            b = a[2].split(" | ")
            c = b[0]
            studentIDs.append(c)
        with open("IDs.txt", 'w') as file:
            for i in studentIDs:
                file.write(str(i) + "\n")



    # Function for the add button

    def add_click():
        global stdList
        global counter
        if counter < 16:
            counter += 1
        # Placeholder Labels
        if counter == 1:
            global stdLabel1
            global gearLabel1
            stdLabel1 = Label(std, text="Name: Student 1 | Student ID: 202310001 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel1 = Label(std, image=newGear)
            gearLabel1.bind("<Button-1>", lambda event: properties(1))
            stdLabel1.place(x=185, y=115)
            gearLabel1.place(x=145, y=113)
            counterLabel.config(text="Students: 1/15")
            stdList.append(stdLabel1.cget("text"))
        elif counter == 2:
            global stdLabel2
            global gearLabel2
            stdLabel2 = Label(std, text="Name: Student 2 | Student ID: 202310002 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel2 = Label(std, image=newGear)
            gearLabel2.bind("<Button-1>", lambda event: properties(2))
            stdLabel2.place(x=185, y=140)
            gearLabel2.place(x=145, y=138)
            counterLabel.config(text="Students: 2/15")
            stdList.append(stdLabel2.cget("text"))
        elif counter == 3:
            global stdLabel3
            global gearLabel3
            stdLabel3 = Label(std, text="Name: Student 3 | Student ID: 202310003 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel3 = Label(std, image=newGear)
            gearLabel3.bind("<Button-1>", lambda event: properties(3))
            stdLabel3.place(x=185, y=165)
            gearLabel3.place(x=145, y=163)
            counterLabel.config(text="Students: 3/15")
            stdList.append(stdLabel3.cget("text"))
        elif counter == 4:
            global stdLabel4
            global gearLabel4
            stdLabel4 = Label(std, text="Name: Student 4 | Student ID: 202310004 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel4 = Label(std, image=newGear)
            gearLabel4.bind("<Button-1>", lambda event: properties(4))
            stdLabel4.place(x=185, y=190)
            gearLabel4.place(x=145, y=188)
            counterLabel.config(text="Students: 4/15")
            stdList.append(stdLabel4.cget("text"))
        elif counter == 5:
            global stdLabel5
            global gearLabel5
            stdLabel5 = Label(std, text="Name: Student 5 | Student ID: 202310005 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel5 = Label(std, image=newGear)
            gearLabel5.bind("<Button-1>", lambda event: properties(5))
            stdLabel5.place(x=185, y=215)
            gearLabel5.place(x=145, y=213)
            counterLabel.config(text="Students: 5/15")
            stdList.append(stdLabel5.cget("text"))
        elif counter == 6:
            global stdLabel6
            global gearLabel6
            stdLabel6 = Label(std, text="Name: Student 6 | Student ID: 202310006 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel6 = Label(std, image=newGear)
            gearLabel6.bind("<Button-1>", lambda event: properties(6))
            stdLabel6.place(x=185, y=240)
            gearLabel6.place(x=145, y=238)
            counterLabel.config(text="Students: 6/15")
            stdList.append(stdLabel6.cget("text"))
        elif counter == 7:
            global stdLabel7
            global gearLabel7
            stdLabel7 = Label(std, text="Name: Student 7 | Student ID: 202310007 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel7 = Label(std, image=newGear)
            gearLabel7.bind("<Button-1>", lambda event: properties(7))
            stdLabel7.place(x=185, y=265)
            gearLabel7.place(x=145, y=263)
            counterLabel.config(text="Students: 7/15")
            stdList.append(stdLabel7.cget("text"))
        elif counter == 8:
            global stdLabel8
            global gearLabel8
            stdLabel8 = Label(std, text="Name: Student 8 | Student ID: 202310008 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel8 = Label(std, image=newGear)
            gearLabel8.bind("<Button-1>", lambda event: properties(8))
            stdLabel8.place(x=185, y=290)
            gearLabel8.place(x=145, y=288)
            counterLabel.config(text="Students: 8/15")
            stdList.append(stdLabel8.cget("text"))
        elif counter == 9:
            global stdLabel9
            global gearLabel9
            stdLabel9 = Label(std, text="Name: Student 9 | Student ID: 202310009 | Grade: 0/100 | Attendance: 0/48",
                              font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel9 = Label(std, image=newGear)
            gearLabel9.bind("<Button-1>", lambda event: properties(9))
            stdLabel9.place(x=185, y=315)
            gearLabel9.place(x=145, y=312)
            counterLabel.config(text="Students: 9/15")
            stdList.append(stdLabel9.cget("text"))
        elif counter == 10:
            global stdLabel10
            global gearLabel10
            stdLabel10 = Label(std, text="Name: Student 10 | Student ID: 202310010 | Grade: 0/100 | Attendance: 0/48",
                               font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel10 = Label(std, image=newGear)
            gearLabel10.bind("<Button-1>", lambda event: properties(10))
            stdLabel10.place(x=185, y=340)
            gearLabel10.place(x=145, y=338)
            counterLabel.config(text="Students: 10/15")
            stdList.append(stdLabel10.cget("text"))
        elif counter == 11:
            global stdLabel11
            global gearLabel11
            stdLabel11 = Label(std, text="Name: Student 11 | Student ID: 202310011 | Grade: 0/100 | Attendance: 0/48",
                               font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel11 = Label(std, image=newGear)
            gearLabel11.bind("<Button-1>", lambda event: properties(11))
            stdLabel11.place(x=185, y=365)
            gearLabel11.place(x=145, y=363)
            counterLabel.config(text="Students: 11/15")
            stdList.append(stdLabel11.cget("text"))
        elif counter == 12:
            global stdLabel12
            global gearLabel12
            stdLabel12 = Label(std, text="Name: Student 12 | Student ID: 202310012 | Grade: 0/100 | Attendance: 0/48",
                               font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel12 = Label(std, image=newGear)
            gearLabel12.bind("<Button-1>", lambda event: properties(12))
            stdLabel12.place(x=185, y=390)
            gearLabel12.place(x=145, y=388)
            counterLabel.config(text="Students: 12/15")
            stdList.append(stdLabel12.cget("text"))
        elif counter == 13:
            global stdLabel13
            global gearLabel13
            stdLabel13 = Label(std, text="Name: Student 13 | Student ID: 202310013 | Grade: 0/100 | Attendance: 0/48",
                               font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel13 = Label(std, image=newGear)
            gearLabel13.bind("<Button-1>", lambda event: properties(13))
            stdLabel13.place(x=185, y=415)
            gearLabel13.place(x=145, y=413)
            counterLabel.config(text="Students: 13/15")
            stdList.append(stdLabel13.cget("text"))
        elif counter == 14:
            global stdLabel14
            global gearLabel14
            stdLabel14 = Label(std, text="Name: Student 14 | Student ID: 202310014 | Grade: 0/100 | Attendance: 0/48",
                               font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel14 = Label(std, image=newGear)
            gearLabel14.bind("<Button-1>", lambda event: properties(14))
            stdLabel14.place(x=185, y=440)
            gearLabel14.place(x=145, y=438)
            stdList.append(stdLabel14.cget("text"))
            counterLabel.config(text="Students: 14/15")
        elif counter == 15:
            global stdLabel15
            global gearLabel15
            stdLabel15 = Label(std, text="Name: Student 15 | Student ID: 202310015 | Grade: 0/100 | Attendance: 0/48",
                               font=("Consolas", 12), borderwidth=2, relief="groove")
            gearLabel15 = Label(std, image=newGear)
            gearLabel15.bind("<Button-1>", lambda event: properties(15))
            stdLabel15.place(x=185, y=465)
            gearLabel15.place(x=145, y=465)
            counterLabel.config(text="Students: 15/15")
            stdList.append(stdLabel15.cget("text"))

    # Function for the delete button

    def del_click():
        global counter
        if counter == 15:
            stdLabel15.destroy()
            gearLabel15.destroy()
            counterLabel.config(text="Students: 14/15")
            del stdList[14]
        elif counter == 14:
            stdLabel14.destroy()
            gearLabel14.destroy()
            counterLabel.config(text="Students: 13/15")
            del stdList[13]
        elif counter == 13:
            stdLabel13.destroy()
            gearLabel13.destroy()
            counterLabel.config(text="Students: 12/15")
            del stdList[12]
        elif counter == 12:
            stdLabel12.destroy()
            gearLabel12.destroy()
            counterLabel.config(text="Students: 11/15")
            del stdList[11]
        elif counter == 11:
            stdLabel11.destroy()
            gearLabel11.destroy()
            counterLabel.config(text="Students: 10/15")
            del stdList[10]
        elif counter == 10:
            stdLabel10.destroy()
            gearLabel10.destroy()
            counterLabel.config(text="Students: 9/15")
            del stdList[9]
        elif counter == 9:
            stdLabel9.destroy()
            gearLabel9.destroy()
            counterLabel.config(text="Students: 8/15")
            del stdList[8]
        elif counter == 8:
            stdLabel8.destroy()
            gearLabel8.destroy()
            counterLabel.config(text="Students: 7/15")
            del stdList[7]
        elif counter == 7:
            stdLabel7.destroy()
            gearLabel7.destroy()
            counterLabel.config(text="Students: 6/15")
            del stdList[6]
        elif counter == 6:
            stdLabel6.destroy()
            gearLabel6.destroy()
            counterLabel.config(text="Students: 5/15")
            del stdList[5]
        elif counter == 5:
            stdLabel5.destroy()
            gearLabel5.destroy()
            counterLabel.config(text="Students: 4/15")
            del stdList[4]
        elif counter == 4:
            stdLabel4.destroy()
            gearLabel4.destroy()
            counterLabel.config(text="Students: 3/15")
            del stdList[3]
        elif counter == 3:
            stdLabel3.destroy()
            gearLabel3.destroy()
            counterLabel.config(text="Students: 2/15")
            del stdList[2]
        elif counter == 2:
            stdLabel2.destroy()
            gearLabel2.destroy()
            counterLabel.config(text="Students: 1/15")
            del stdList[1]
        elif counter == 1:
            stdLabel1.destroy()
            gearLabel1.destroy()
            counterLabel.config(text="Students: 0/15")
            del stdList[0]
        if counter > 0:
            counter -= 1

    # Window Setup
    std = Toplevel(root)
    std.title("Students")
    std.geometry("1000x600")
    std.resizable(False, False)

    # Student Widgets
    std_uopLogo = PhotoImage(file="assets/UOP.png")
    uopLabel2 = Label(std, image=std_uopLogo)
    uopLabel2.image = std_uopLogo

    std.gear = PhotoImage(file="assets/properties.png")
    newGear = std.gear.subsample(19, 19)

    addButton = Button(std, text="Add", font=("Consolas", 22), bd=5, command=lambda: add_click())
    deleteButton = Button(std, text="Delete", font=("Consolas", 22), bd=5, command=lambda: del_click())
    saveButton = Button(std, text="Save", font=("Consolas", 22), bd=5, command=lambda: save_click())
    avgButton = Button(std, text="Avg", font=("Consolas", 22), bd=5, command=lambda: avg_click())
    counterLabel = Label(std, text="Students: 0/15", font=("Consolas", 15))

    # Widget Placement
    uopLabel2.place(x=375, y=10)
    addButton.place(x=350, y=525)
    deleteButton.place(x=450, y=525)
    saveButton.place(x=600, y=525)
    avgButton.place(x=725, y=525)
    counterLabel.place(x=15, y=560)

# Window Setup
root = Tk()
root.title("Dashboard")
root.geometry("800x500")
root.resizable(False, False)

# Root Widgets
uopLogo = PhotoImage(file="assets/UOP.png")
uopLabel = Label(root, image=uopLogo)
courseLabel = Label(root, text="Course: " + courseName, font=("Consolas", 16))
studentsButton = Button(root, text="Students", font=("Consolas", 25), relief="raised", bd=5, command=lambda: students_click())
reportButton = Button(root, text="Reports", font=("Consolas", 25), relief="raised", bd=5, command=lambda: report_click())

# Widget Placement
uopLabel.place(x=275, y=25)
courseLabel.place(x=10, y=460)
studentsButton.place(x=175, y=250)
reportButton.place(x=475, y=250)

root.mainloop()
