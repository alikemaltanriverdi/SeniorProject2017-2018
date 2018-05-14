#  CSI Resume Project 2017
#  GUIImplementation.py
#
#  Created by Ali Tanriverdi on November 6, 2017
#  Copyright 2017 Ali Tanriverdi. All rights reserved.
#


#Listboxes are created and data is inserted to the listboxes
import Tkinter as tk
from Tkinter import *

def insertionToListElement(listElement,resumeID):
    for i in range(0, len(resumeID)):
        newStr = ""
        resumeID[i].reason = sorted(set(resumeID[i].reason))
        if (len(resumeID[i].reason)==1):
            listElement.insert(tk.END, "ID:  " + str(resumeID[i].name()), "Grade:  " + str(resumeID[i].grade()), "Reason:  "  + str(resumeID[i].reason[0]) , " ")
        else:
            for j in range(0, len(resumeID[i].reason)):
                if(j==len(resumeID[i].reason)-1):
                    newStr = newStr+ resumeID[i].reason[j]
                    # print "NewString:" + newStr
                else:
                    newStr = newStr + resumeID[i].reason[j]+","
                    # print "NewString:" + newStr

            listElement.insert(tk.END, "ID:  " + str(resumeID[i].name()), "Grade:  " + str(resumeID[i].grade()), "Reason:  " + str(newStr) , " ")


#Creates listboxes to keep data in it
def GUIMethod(goal,declinedResumes,acceptedResumes,resumesOnTheWaitingList):
    if(len(acceptedResumes)>0):
        acceptanceLabel = tk.Label(goal,text="Accepted")
        acceptanceLabel.grid(row=1,column=0)
        Lb2 = tk.Listbox(goal,height=len(acceptedResumes),width=len(acceptedResumes),bg="green3")
        Lb2.grid(row=1,column=1)
        acceptanceLabel.pack(fill=BOTH)
        Lb2.pack(fill=BOTH, expand=1)
    if(len(resumesOnTheWaitingList)>0):
        waitLabel = tk.Label(goal,text= "Waiting")
        waitLabel.grid(row=1,column=0)
        Lb3 = tk.Listbox(goal,height=len(resumesOnTheWaitingList),width=len(resumesOnTheWaitingList),bg="yellow3")
        Lb3.grid(row=3,column=3)
        waitLabel.pack(fill=BOTH)
        Lb3.pack(fill=BOTH, expand=1)
    if (len(declinedResumes) > 0):
        ali = tk.Label(goal, text="Declined")
        # ali.columnconfigure(0, weight=3)
        Lb1 = tk.Listbox(goal,width=50,height=len(declinedResumes),bg="red3")
        Lb1.grid(row=0, column=0)
        ali.pack(fill=BOTH)
        Lb1.pack(fill=BOTH, expand=1)

    #Data Loading to GUI Related Objects
    if(len(declinedResumes)<=0):
        print ("\nCould not find any declined resume!\n")
    else:
        insertionToListElement(Lb1,declinedResumes)

    if(len(acceptedResumes)<=0):
        print ("\nCould not find any accepted resume!\n")
    else:
        insertionToListElement(Lb2, acceptedResumes)

    if(len(resumesOnTheWaitingList)<=0):
        print("Could not find any resumes on the waiting list")
    else:
        insertionToListElement(Lb3, resumesOnTheWaitingList)