#  CSI Resume Project 2017
#  Resumes.py
#
#  Created by Ali Tanriverdi on November 6, 2017
#  Copyright 2017 Ali Tanriverdi. All rights reserved.
#

#Resumes Class
#Has Attributes as grade,name,acceptance,reason

class Resumes:

    def __init__(self,name,text,acceptance):
        self.acceptance = False
        self._name = name
        self._grade = 0
        self.acceptance = acceptance
        self.reason = []
        self._text = self.makeResumeText(text)

    def decreaseGrade(self):
        self._grade -=1
    def increaseGrade(self):
        self._grade +=1
    def internationalDecrease(self):
        self._grade = -100

    def getName(self):
        return self._name

    def grade(self):
        return  self._grade
    def name(self):
        return self._name
    def makeResumeText(self,text):
        array = text.split('\n')
        return array
    def getResumeText(self):
        return self._text