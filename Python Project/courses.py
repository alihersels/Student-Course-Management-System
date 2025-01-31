from tkinter import *
from login import lst

# Functions


def course_click():

    # Functions of function (confusing but it works)
    global counter
    counter = 0

    def course_sel(c_name):
        with open("course.txt", 'w') as file:
            file.write(c_name)
        course.destroy()
        import dashboard

    def properties(num):
        # Functions of a function's function (treading on thin ice, but it still works)
        def apply_click(i):
            if i == 1:
                courseButton1.config(text=propEntry.get())
                course.update_idletasks()
                # Unholy abomination ahead...but it works (Used to change the placement of the gear image when the
                # button's placement is also changed)
                gearLabel1.place(x=courseButton1.winfo_x() + courseButton1.winfo_width() / 2 - newGear.width() / 2,
                                 y=courseButton1.winfo_y() + courseButton1.winfo_height() + 5)
            elif i == 2:
                courseButton2.config(text=propEntry.get())
                course.update_idletasks()
                gearLabel2.place(x=courseButton2.winfo_x() + courseButton2.winfo_width() / 2 - newGear.width() / 2,
                                 y=courseButton2.winfo_y() + courseButton2.winfo_height() + 5)
            elif i == 3:
                courseButton3.config(text=propEntry.get())
                course.update_idletasks()
                gearLabel3.place(x=courseButton3.winfo_x() + courseButton3.winfo_width() / 2 - newGear.width() / 2,
                                 y=courseButton3.winfo_y() + courseButton3.winfo_height() + 5)
            else:
                courseButton4.config(text=propEntry.get())
                course.update_idletasks()
                gearLabel4.place(x=courseButton4.winfo_x() + courseButton4.winfo_width() / 2 - newGear.width() / 2,
                                 y=courseButton4.winfo_y() + courseButton4.winfo_height() + 5)
        # Constructing the properties window
        prop = Tk()
        prop.resizable(False, False)
        # num stands for the course number
        prop.title(f"Properties ({num})")
        prop.geometry("250x75")

        propLabel = Label(prop, text="Rename Course: ", font=("Consolas", 10))
        propEntry = Entry(prop, font=("Consolas", 10))
        applyButton = Button(prop, text="Apply", font=("Consolas", 15))
        propLabel.grid(row=0,column=0)
        propEntry.grid(row=0,column=1)
        applyButton.grid(row=1, column=0, columnspan=2, pady=12)
        applyButton.config(command=lambda: apply_click(num))

        prop.mainloop()

    def add_click():
        global counter
        if counter < 5:
            counter += 1
        if counter == 1:
            # Made global so other functions could interact with them
            global courseButton1
            global gearLabel1
            courseButton1 = Button(course, text="Course 1", font=("Consolas", 15), bd=5, relief="raised",
                                  command=lambda: course_sel(courseButton1.cget('text')))
            courseButton1.place(x=150, y=250)
            gearLabel1 = Label(course, image=newGear)
            gearLabel1.place(x=175, y=300)
            # We're binding the function to the event, and not the event to the function; hence the use of event:
            gearLabel1.bind("<Button-1>", lambda event: properties(1))
            counterLabel.config(text="Courses: 1/4")
        elif counter == 2:
            global courseButton2
            global gearLabel2
            courseButton2 = Button(course, text="Course 2", font=("Consolas", 15), bd=5, relief="raised",
                                   command=lambda: course_sel(courseButton2.cget('text')))
            courseButton2.place(x=300, y=250)
            gearLabel2 = Label(course, image=newGear)
            gearLabel2.place(x=325, y=300)
            gearLabel2.bind("<Button-1>", lambda event: properties(2))
            counterLabel.config(text="Courses: 2/4")
        elif counter == 3:
            global courseButton3
            global gearLabel3
            courseButton3 = Button(course, text="Course 3", font=("Consolas", 15), bd=5, relief="raised",
                                   command=lambda: course_sel(courseButton3.cget('text')))
            courseButton3.place(x=450, y=250)
            gearLabel3 = Label(course, image=newGear)
            gearLabel3.place(x=475, y=300)
            gearLabel3.bind("<Button-1>", lambda event: properties(3))
            counterLabel.config(text="Courses: 3/4")
        elif counter == 4:
            global courseButton4
            global gearLabel4
            courseButton4 = Button(course, text="Course 4", font=("Consolas", 15), bd=5, relief="raised",
                                   command=lambda: course_sel(courseButton4.cget('text')))
            courseButton4.place(x=600, y=250)
            gearLabel4 = Label(course, image=newGear)
            gearLabel4.place(x=625, y=300)
            gearLabel4.bind("<Button-1>", lambda event: properties(4))
            counterLabel.config(text="Courses: 4/4")

    def delete_click():
        # Destroys the labels and buttons while also maintaining responsiveness by editing the counterLabel's text as
        # it goes
        global counter
        if counter == 4:
            courseButton4.destroy()
            gearLabel4.destroy()
            counterLabel.config(text="Courses: 3/4")
        elif counter == 3:
            courseButton3.destroy()
            gearLabel3.destroy()
            counterLabel.config(text="Courses: 2/4")
        elif counter == 2:
            courseButton2.destroy()
            gearLabel2.destroy()
            counterLabel.config(text="Courses: 1/4")
        elif counter == 1:
            courseButton1.destroy()
            gearLabel1.destroy()
            counterLabel.config(text="Courses: 0/4")
        if counter > 0:
            counter -= 1

    root.destroy()

    # Window Setup
    course = Tk()
    course.title("Courses")
    course.geometry("800x500")
    course.resizable(False, False)

    course.uopLogo2 = PhotoImage(file="assets/UOP.png")
    course.gear = PhotoImage(file="assets/properties.png")
    newGear = course.gear.subsample(10,10)


    # Course Widgets
    counter = 0
    uopLabel2 = Label(course, image=course.uopLogo2)
    addButton = Button(course, text="Add", font=("Consolas", 20), command=add_click)
    deleteButton = Button(course, text="Delete", font=("Consolas", 20), command=delete_click)
    counterLabel = Label(course, text="Courses: 0/4", font=("Consolas", 15))

    # Widget Placement
    uopLabel2.place(x=275, y=25)
    addButton.place(x=275, y=425)
    deleteButton.place(x=425, y=425)
    counterLabel.place(x=25, y=450)


# Window Setup
root = Tk()
root.title("Performance Tracker")
root.geometry("600x350")
root.resizable(False, False)


uopLogo = PhotoImage(file="assets/UOP.png")

# Root Widgets
uopLabel = Label(root, image=uopLogo)
usernameLabel = Label(root, text="Logged in as: " + lst[0], font=("Consolas", 15))
courseButton = Button(root, text="Courses", font=("Consolas", 20), command=lambda: course_click())

# Widget Placement
uopLabel.place(x=175, y=20)
courseButton.place(x=240, y=175)
usernameLabel.place(x=5, y=315)


root.mainloop()
