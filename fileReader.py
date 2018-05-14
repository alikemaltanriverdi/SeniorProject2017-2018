#  CSI Resume Project 2017
#  filerReader.py
#
#  Created by Ali Tanriverdi on October 20, 2017
#  Copyright 2017 Ali Tanriverdi. All rights reserved.
#

def fileRead(fileName,array):
    try:
        with open(fileName, "r") as f:
            for line in f:
                array.append(line)  # appends the lines of the the file to the array
        f.close()
    except IOError:
        print("Cannot open the file:"+str(fileName))