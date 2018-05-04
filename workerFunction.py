#  CSI Resume Project 2017
#  workerFunction.py
#
#  Created by Ali Tanriverdi on October 20, 2017
#  Copyright 2017 Ali Tanriverdi. All rights reserved.
#

import resumeSelection as resSelect
import databaseConnection as database
import index as databaseAdder


class Worker():
    def __init__(self):
        databaseAdder.work()
        self.firstList = []
        self.secondList = []
        self.thirdList = []

        self.workerFunction()


    def workerFunction(self):
        resumes = []#Holds resume names
        declinedResumes = [] #Holds the declined resumes as objects of Resumes Class
        resumesArr =[]#Holds all resumes those are in the directory

        acceptedResumes = []#Holds the accepted resumes as objects of Resumes Class
        resumesOnTheWaitingList = []#Holds The Resume Objects Those on the waiting list
        topResumes = []
        #Will be used to hold the path for the file

        badWords = [] #Holds the array of bad words for grading
        goodWords = [] #Holds the array of good words for grading

         #Calls badWordsSelection method of the databaseConnection Module
        database.badWordsSelection('alikemal', badWords)

        #Calls goodWordsSelection method of the databaseConnection Module
        database.goodWordsSelection('alikemal', goodWords)

        database.resumeSelectionOfDatabase('alikemal',resumesArr)

        for i in range(0, len(resumesArr)):
            resSelect.resumeSelection(resumesArr[i], resumesArr[i].getResumeText()  , badWords, goodWords)
            resumesArr[i].reason = sorted(set(resumesArr[i].reason))#removes duplicates from the list
            if(resumesArr[i].acceptance=="True"):
                acceptedResumes.append(resumesArr[i])#Will be changed to database instead of Array
                resumesArr[i].acceptance = "True"
                topResumes.append(resumesArr[i])

            elif(resumesArr[i].acceptance=="False"):
                resumesArr[i].acceptance = "False"
                declinedResumes.append(resumesArr[i])

            elif(resumesArr[i].acceptance=="Waiting"):
                resumesOnTheWaitingList.append(resumesArr[i])
                topResumes.append(resumesArr[i])
            else:
                print ("Could not find")

        database.dataBaseInsertion("alikemal", topResumes, "Accepted")
        database.dataBaseInsertion("alikemal", declinedResumes, "Declined")

        # print("\nAccepted Resumes:")
        # for i in range(0,len(acceptedResumes)):
        #     print ("Grade:" + str(acceptedResumes[i].grade())+" \tName:" + str(acceptedResumes[i].name())+"\tReason:"+str(acceptedResumes[i].reason).replace("[", "").replace("]", "").replace("'", "") )
        #
        #
        # print ("\nDeclined Resumes:" )
        # for i in range(0,len(declinedResumes)):
        #     print ("Grade:" + str(declinedResumes[i].grade())+" \tName:" + str(declinedResumes[i].name()) +"\tReason:"+str(declinedResumes[i].reason).replace("[", "").replace("]", "").replace("'", ""))
        #
        #
        # print ("\nResumes On The Waiting List:")
        # for i in range(0, len(resumesOnTheWaitingList)):
        #     if(len(resumesOnTheWaitingList[i].reason)!=0):
        #         print ("Grade:" + str(resumesOnTheWaitingList[i].grade())+" \tName:" + resumesOnTheWaitingList[i].name()+"\tReason:"+str(resumesOnTheWaitingList[i].reason).replace("[","").replace("]","").replace("'","") )
        #     else:
        #         print ("Grade:" + str(resumesOnTheWaitingList[i].grade()) + " \tName:" + resumesOnTheWaitingList[i].name() + "\tReason: Does not have any words in it" )


        #Sorting Arrays into a new array comparing to their grades in decending order
        self.accepted = sorted(acceptedResumes, key=lambda x: x.grade(), reverse=True)
        self.waiting = sorted(resumesOnTheWaitingList, key=lambda x: x.grade(), reverse=True)
        self.declined = sorted(declinedResumes, key=lambda x: x.grade(), reverse=True)