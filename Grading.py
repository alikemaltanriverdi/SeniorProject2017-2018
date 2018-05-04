
def Grading(resumeObj,kindOfGrade):
    try:
        if(kindOfGrade == "inc"):
            resumeObj.increaseGrade()
        elif(kindOfGrade=="dec"):
            resumeObj.decreaseGrade()
        elif(kindOfGrade == "int"):
            resumeObj.internationalDecrease()

    except:
        print "Grading error"
