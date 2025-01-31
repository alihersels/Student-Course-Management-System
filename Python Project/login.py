from tkinter import *

# Functions

lst = []

def signup():
    with open("users.txt", 'a') as file:
        file.write(usernameEntry.get() + "-" + passwordEntry.get() + "\n")


def login():
    with open("users.txt", 'r') as file:
        user_lst = file.readlines()
        user = usernameEntry.get() + "-" + passwordEntry.get() + "\n"
        count = 0
        for i in user_lst:
            if i == "\n":
                user_lst.remove(i)
                continue
            if i == user:
                count += 1
        if count == 0:
            statusLabel.config(text="Fail")
        else:
            statusLabel.config(text="Pass")
            lst.append(usernameEntry.get())
            root.destroy()
            import courses
            

# Window Setup
root = Tk()
root.title("Login/Sign-up Window")
root.geometry("600x400")
root.resizable(False, False)

uopLogo = PhotoImage(file="assets/UOP.png")
uopLabel = Label(root, image=uopLogo)
usernameLabel = Label(root, text="Username: ", font=("Consolas", 25), padx=30)
usernameEntry = Entry(root, font=("Consolas", 20))
passwordLabel = Label(root, text="Password: ", font=("Consolas", 25))
statusLabel = Label(root, text="", font=("Consolas", 30))
passwordEntry = Entry(root, show="*", font=("Consolas", 20))
loginButton = Button(root, text="Login", font=("Consolas", 25), command=login)
signupButton = Button(root, text="Sign-up", font=("Consolas", 25), command=signup)


uopLabel.grid(row=0, column=2, columnspan=2, pady=20)
usernameLabel.grid(row=1, column=2, pady=10)
usernameEntry.grid(row=1, column=3, pady=10)
passwordLabel.grid(row=2, column=2)
passwordEntry.grid(row=2, column=3)
loginButton.place(x=200, y=300)
signupButton.place(x=350, y=300)
statusLabel.grid(row=4, column=2, columnspan=2)

root.mainloop()
