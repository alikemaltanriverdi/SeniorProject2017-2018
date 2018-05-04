#  CSI Resume Project 2017
#  resumeSelection.py
#
#  Created by Ali Tanriverdi on October 25, 2017
#  Copyright 2017 Ali Tanriverdi. All rights reserved.
#

# import fileReader as readFile
import Grading as grader
import CountriesTry as mainGrader

countryList = mainGrader.newStr

#Searches through the file and returns the decision of the decline or acceptance
def resumeSelection(resObj, personName, badWordsArray, goodWordsArray):
    array = personName
    try:
        #Searches through the lines to find Bad Words and Good Words, and use increaseGrade or decreaseGrade according to the result
        for i in range(0, len(array)):
            for j in range(0, len(badWordsArray)):
                if (badWordsArray[j] == "" or badWordsArray[j] == " " or badWordsArray[j] == "\\" or
                            badWordsArray[j] == "/" or badWordsArray[j] == ","):
                    continue
                else:
                    if ((str(array[i]).lower()).find(str(badWordsArray[j]).lower()) != -1):
                        grader.Grading(resObj, "dec")
                        resObj.reason.append(badWordsArray[j])
                        break

            for j in range(0, len(goodWordsArray)):
                if(goodWordsArray[j]=="" or goodWordsArray[j] == " " or goodWordsArray[j]=="\\" or goodWordsArray[j]=="/" or goodWordsArray[j]=="" or goodWordsArray[j]== ","):
                    continue
                else:
                    if ((str(array[i]).lower()).find(str(goodWordsArray[j]).lower()) != -1):
                        grader.Grading(resObj, "inc")
                        resObj.reason.append(goodWordsArray[j])
                        break

            if(str(array[i]).lower().find("eagle scout")==-1):
                for k in range(0,len(countryList)):
                    if ((str(array[i]).lower()).find(str(countryList[k]).lower()) != -1):
                        grader.Grading(resObj, "int")
                        resObj.reason.append(countryList[k])
                        break
                resObj.reason = sorted(set(resObj.reason))  # removes duplicates from the list

        if(resObj.grade()>0):
            resObj.acceptance = "True"
        elif(resObj.grade() ==0):
            resObj.acceptance = "Waiting"
        else:
            resObj.acceptance = "False"
    except:
        quit(1)