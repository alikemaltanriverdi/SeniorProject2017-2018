#  CSI Resume Project 2017
#  GUIImplementation.py
#
#  Created by Ali Tanriverdi on February 6, 2018
#  Copyright 2018 Ali Tanriverdi. All rights reserved.
#

#Creates Dashboard, and call other functions to run the program


import Tkinter as tk
from Tkinter import *
import datetime as nowTime
import workerFunction as works
import GUIImplemantation as gui
import tkMessageBox
import filePathFinder as files

LARGE_FONT = ("Times New Roman", 14)

worker = works.Worker()

#Temporary user names for login
usersOfApp = {
    "Ali":"Kemal",
    "Merwyn":"Jones",
    "Yalvac":"Top",
    "Elcin":"Can"
}

#Initialize main Dasboard to run other dashboards
class ResumeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#For creation of the user login page
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        user_name_getter = tk.Entry(self,text="")
        user_pass_getter = tk.Entry(self,show="*",text="")

        label = tk.Label(self, text="User Information", font=LARGE_FONT)
        label.grid(row=0, column=0)

        userName = tk.Label(self,text="User Name", font=LARGE_FONT)
        userPassword = tk.Label(self,text="User Password", font = LARGE_FONT)
        userPassword.grid(row=2, column=0)
        user_pass_getter.grid(row=2, column=2)
        userName.grid(row=1, column=0)
        user_name_getter.grid(row=1, column=2)

        label.pack(pady=10, padx=10)
        userName.pack()#pady=10, padx=10)
        user_name_getter.pack()#pady=10, padx=10)

        userPassword.pack()#padx=10)
        user_pass_getter.pack()#pady=10, padx=10)

        button = tk.Button(self, text="Login",command = lambda: self.checkInput(user_name_getter.get(),user_pass_getter.get(),controller), font=LARGE_FONT)
        button.pack()

    def checkInput(self,user_name_get,user_pass_get,controller):
        if (usersOfApp[user_name_get]==user_pass_get):
            controller.show_frame(PageOne)
        elif(user_name_get =="" or user_name_get == " " or user_pass_get=="" or user_pass_get==" "):
            tkMessageBox.showinfo("Error!","You have entered missing information")
        else:
            tkMessageBox.showinfo("Error!", "You have entered missing information")
            print("wrong info")
            print(nowTime.datetime.now())

#For creation of the data loads from the database
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.button2 = tk.Button(self, text="Refresh", command=lambda: self.refreshElements(),bg="blue")
        self.button2.pack(side="top",fill=X,padx=0,pady=0)
        self.button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage),bg="blue")
        self.button1.pack(side="bottom",fill=X)
        gui.GUIMethod(self, worker.declined, worker.accepted, worker.waiting)

    def refreshElements(self):
        imList = []
        files.filePathFinder(imList)
        if (len(imList) > 0):
            worker = works.Worker()
            gui.GUIMethod(self, worker.declined, worker.accepted, worker.waiting)
        else:
            tkMessageBox.showinfo("Warning", "Please update the files in the directory to be able to use this feature or check your file extensions")


app = ResumeApp()
app.title("CSI Resume Analysis")

app.mainloop()