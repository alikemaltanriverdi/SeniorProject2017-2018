#  CSI Resume Project 2017
#  databaseConnection.py
#
#  Created by Ali Tanriverdi on November 10, 2017
#  Copyright 2017 Ali Tanriverdi. All rights reserved.
#

#Connects to the database and gets all data from the database
import mysql.connector
from mysql.connector import errorcode
import Resumes as Resumes
import sys
reload(sys)  # Reload is a hack
sys.setdefaultencoding('UTF8')

#Connects to the database
def dataBaseConnectionEstablish(database):
    try:
        databaseObj = mysql.connector.connect(user='admin', password='admin', host='127.0.0.1', database=database)
        print "Connection Worked"
        return databaseObj
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "Could not connect"
            quit()
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist"
            quit()
        else:
            print e
            quit()

#Makes insert operations to accepted or declined resumes tables in the database
def dataBaseInsertion(database, array, acceptionType):
    connectionObj = dataBaseConnectionEstablish(database)

    if(acceptionType == "Accepted"):
        cursor = connectionObj.cursor()
        emplooyesInsertion(cursor,array)
        connectionObj.commit()
        cursor.close()
        connectionObj.close()
        print "Accepted worked"
    elif(acceptionType == "Declined"):
        cursor = connectionObj.cursor()
        declinedResumesInsertion(cursor,array)
        connectionObj.commit()
        cursor.close()
        connectionObj.close()
        print "Declined worked"
    else:
        print "Could not find the right type! Closing the connection..."
        connectionObj.close()


def declinedResumesInsertion(obj,dArray):
    for i in range(0, len(dArray)):
        try:
            sql = ("INSERT INTO DeclinedResumes (Name,Reason) VALUES (%s, %s)")
            obj.execute(sql, (str(dArray[i].name()), str(dArray[i].reason).replace("[", "").replace("]", "").replace("'", "")))

        except mysql.connector.IntegrityError:
            query = "UPDATE DeclinedResumes SET Reason = %s WHERE Name= %s"
            obj.execute(query,(str(dArray[i].reason).replace("[", "").replace("]", "").replace("'", ""), str(dArray[i].name())))
            print("Daha da giris")
            continue
            # print "Could not execute for declined resumes"

def emplooyesInsertion(obj, eArray):
    for i in range (0, len(eArray)):
        try:
            sql = ("INSERT INTO AcceptedResumes (Name,Grade,Reason) VALUES (%s, %s, %s)")
            obj.execute(sql, (str(eArray[i].name()), str(eArray[i].grade()), str(eArray[i].reason).replace("[", "").replace("]", "").replace("'", "")))
        except mysql.connector.IntegrityError:
            query = "UPDATE AcceptedResumes SET Grade = %s, Reason = %s WHERE Name= %s"
            obj.execute(query, (str(eArray[i].grade()),str(eArray[i].reason).replace("[", "").replace("]", "").replace("'", ""),str(eArray[i].name())))
            print("Daha fazla da giris")
            continue

def badWordsSelection(database, array):
    try:
        connectionObj = dataBaseConnectionEstablish(database)
        cursor = connectionObj.cursor()
        sql = ("SELECT BadWord FROM BadWords")
        cursor.execute(sql)
        rows = cursor.fetchall()
        # print rows
        for row in rows:
            # print row[0]
            array.append(str(row[0]))

        cursor.close()
        connectionObj.close()
    except mysql.connector.Error as a:
        if a.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print "Something went wrong to get bad words!"

def goodWordsSelection(database, array):
    try:
        connectionObj = dataBaseConnectionEstablish(database)
        cursor = connectionObj.cursor()
        sql = ("SELECT GoodWord FROM GoodWords")
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            array.append((str(row[0])))
        cursor.close()
        connectionObj.close()
    except mysql.connector.Error as a:
        if a.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something went wrong to get bad words!")
        print("Something went wrong to get good words!")

def resumeSelectionOfDatabase(database,array):
    try:
        connectionObj = dataBaseConnectionEstablish(database)
        cursor = connectionObj.cursor()
        sql = ("SELECT * FROM Resumes")
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            array.append(Resumes.Resumes(str(row[0]),str(row[1]),"False"))

        cursor.close()
        connectionObj.close()
    except mysql.connector.Error as a:
        if a.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print ("Something went wrong to get bad words!")
        print("Something went wrong to get good words!")
