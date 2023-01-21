from json import *
from tkinter import *
import random
import hashlib

mainWindow = Tk()
mainWindow.geometry("280x120")
mainWindow.title("Password sim")
mainWindow.resizable(height=False, width=False)

entries = ["", ""]

formFrame = Frame(mainWindow)
formFrame.pack(expand=True, fill="both")
messageLabel = Label(formFrame, font=("Arial", 7))
messageLabel.grid(row=4, column=1, pady=5)

"""with open("Register.json") as rg:
    register = load(rg)"""


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

def Registering():
    global entries
    password = sha256(entries[1].get())

    if CheckEntries():
        
        return None

def SetUpFrame():
    global entries
    labels = ["Username: ", "Password: "]
    paddingY = 5
    paddingX = 10
    for i in range(2):
        formLabel = Label(formFrame, text=labels[i])
        formLabel.grid(row=i, column=0, padx=paddingX, pady=paddingY)
        formEntry = Entry(formFrame)
        formEntry.grid(row=i, column=1)
        if i == 1:
            formEntry.config(show="*")
        entries[i] = formEntry


    converter = Button(formFrame, text="Register", command=Registering)
    converter.grid(row=3, column=1)

def main():
    SetUpFrame()
    mainWindow.mainloop()
    """try:
        SetUpFrame()
        mainWindow.mainloop()
    except:
        print("Program closed")"""





if __name__ == "__main__":
    main()