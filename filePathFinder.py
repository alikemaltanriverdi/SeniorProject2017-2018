#  CSI Resume Project 2017
#  filePathFinder.py
#
#  Created by Ali Tanriverdi on October 20, 2017
#  Copyright 2017 Ali Tanriverdi. All rights reserved.
#

#Finds the files to be process in the given folder
import glob, os
def filePathFinder(resumes):
    pathOfTheDirectory = "C:\\Users\\yalva\\Desktop\\sync\\"
    os.chdir(pathOfTheDirectory)  # Sets file path

    #For jgp extensions
    for file in glob.glob("*.jpg"):
        if ((file == "goodWords.txt") or file == "badWords.txt"):
            continue
        else:
            (resumes).append(pathOfTheDirectory+str(file))  # Adds Files into Resume Array

    # For JPG extensions
    for file in glob.glob("*.JPG"):
        if ((file == "goodWords.txt") or file == "badWords.txt"):
            continue
        else:
            (resumes).append(pathOfTheDirectory+str(file))  # Adds Files into Resume Array

    #For .pdf extensions
    #for file in glob.glob("*.pdf"):
    #    if ((file == "goodWords.txt") or file == "badWords.txt"):
    #        continue
    #    else:
    #        (resumes).append(pathOfTheDirectory+str(file))  # Adds Files into Resume Array