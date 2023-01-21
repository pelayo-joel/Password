from json import *
from tkinter import *
import hashlib

"""The whole code for the password project, supports password security check, corresponding passsword, 
    new user or adding of new passwords for registered users, and displaying of passwords for every user that are registered"""

#Main window of the program
mainWindow = Tk()
mainWindow.geometry("320x120")
mainWindow.title("Password Storage")
mainWindow.resizable(height=False, width=False)

#Stores what has been putted in both entries
entries = ["", ""]

#Configures the frame and the message
formFrame = Frame(mainWindow)
formFrame.pack(expand=True, fill="both")
messageLabel = Label(formFrame, font=("Arial", 8))
messageLabel.grid(row=4, column=1, pady=5)

#Data from the json file that contains all registered users:passwords and stores it in 'register'
with open("Register.json") as rg:
    register = load(rg)


#Function that checks if username and password are valid, username forbids " to prevent potential bugs with the json 
def CheckEntries():
    global entries
    conditions = [False]*4
    specialChar = "&é'(-è_çà)=~#}{[|`\^@]+^¨$£%*µ!§:/;.,?<>²°"
    messageLabel.config(text="")
    try:
        if '"' in entries[0].get() or entries[0].get() == "" or " " in entries[0].get():
            messageLabel.config(text="Invalid username", fg="red")
            return False

        if len(entries[1].get()) > 8:
            for char in entries[1].get():
                if char.isupper():
                    conditions[0] = True
                if char.islower():
                    conditions[1] = True
                if char.isalnum():
                    conditions[2] = True
                if char in specialChar:
                    conditions[3] = True
                if all(conditions):
                    return True
            if all(conditions) == False:
                messageLabel.config(text="Upper, lower, num, special char needed", fg="red")
                return False
        else:
            messageLabel.config(text="Need nore than 8 char", fg="red")
            return False
    except:
        messageLabel.config(text="Error", fg="red")
        return False

#Checks if inputs are valid then if the user has already been registered it checks the password, if not it adds the user and its password to the json
def Registering():
    global entries
    username = entries[0].get()
    if CheckEntries():
        password = hashlib.sha256(entries[1].get().encode()).hexdigest()
        if username in register:
            if password in register[username]["Hashes"]:
                messageLabel.config(text=f"Hi {username}, welcome back !", fg="green")
            else:
                messageLabel.config(text=f"Password incorrect", fg="red")
        else:
            register.update({username: {"Passwords":[entries[1].get()], "Hashes":[password]}})
            messageLabel.config(text=f"Welcome {username}, you've been registered !", fg="green")
            SaveJSON_Updates()

#Adds a new password to the user if it corresponds to no other passwords
def Add():
    global entries
    username = entries[0].get()
    if CheckEntries() and username in register and entries[1].get() not in register[username]["Passwords"]:
        password = hashlib.sha256(entries[1].get().encode()).hexdigest()
        register[username]["Passwords"].append(entries[1].get())
        register[username]["Hashes"].append(password)
        messageLabel.config(text=f"Successfully added new password for {username} !", fg="green")
        SaveJSON_Updates()
    else:
        messageLabel.config(text=f"Unknown user or password already exist", fg="black")

#Displays in a list of a new window all the user passwords
def DisplayPass():
    global entries
    username = entries[0].get()

    if username in register:
        passWin = Toplevel()
        passWin.geometry("200x150")
        passWin.title(f"{username}'s passwords list")
        userLabel = Label(passWin, text=f"{username}", font=("Arial", 10))
        userLabel.pack(expand=True, fill="both")

        passList = Listbox(passWin)
        i = 1
        for password in register[username]["Passwords"]:
            passList.insert(i, password)
            i += 1 
        passList.pack(expand=True, fill="both")
    else:
        messageLabel.config(text=f"Unknown user", fg="black")

#Utility to update tthe json file
def SaveJSON_Updates():
    with open("Register.json", "w") as rg:
        dump(register, rg, indent=4, separators=(",",": "))

#Sets up the frame of the main window
def SetUpFrame():
    global entries
    labels = ["Username: ", "Password: "]
    paddingY = 5
    paddingX = 10
    for i in range(2):
        formLabel = Label(formFrame, text=labels[i])
        formLabel.grid(row=i, column=0, padx=paddingX, pady=paddingY)
        formEntry = Entry(formFrame, width=36)
        formEntry.grid(row=i, column=1)
        if i == 1:
            formEntry.config(show="*")
        entries[i] = formEntry

    buttonFrame = Frame(formFrame)
    buttonFrame.grid(row=2, column=1, sticky=NSEW)
    signing = Button(buttonFrame, text="Register", command=Registering)
    signing.pack(side=LEFT, padx=10)
    change = Button(buttonFrame, text="Add", command=Add)
    change.pack(side=LEFT, padx=10)
    display = Button(buttonFrame, text="DisplayPass", command=DisplayPass)
    display.pack(side=LEFT, padx=10)

def main():
    try:
        SetUpFrame()
        mainWindow.mainloop()
    except:
        print("Program closed")





if __name__ == "__main__":
    main()