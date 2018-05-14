 --CSI Resume Project Documentation for Building the Application--

Building Steps:
Download Google Drive and sign in using the credentials above. 
Copy the Google Drive path to filepathfinder.py

1- MySQL Installer & Reconfig.

2- MySQL Terminal Start

3- Add MySQL Server to Valentina Studio

4- Valentina Studio -> Create Server 

5-  Create a database called "alikemal"

6- Load the dump database (that will be provided by us) from Downloads .SQL.

7- py -2.7 -m pip install virtualenv 

8- py -2.7 -m virtualenv FileMods ->>>> If you have any other folder for this, change all FileMods to your folder name, C:/.../SeniorProject 20172018-master

9- cd /scripts

10- activate 

11- SET GOOGLE_APPLICATION_CREDENTIALS=C:/.../SeniorProject20172018-master/credentials.json

12- Add database user as: seniorProject
	-> Admin ? all privileges apply

13- On Google Drive: change filepath finder.

14- py -2.7 -m pip install mysql-connector

15- py -2.7 -m dashboardimplementation.py


 --Code Files Documentation--
	
Dashboardimplementation.py:
Has 3 classes:
ResumeApp class: Uses Tkinter library and calls the default library functions to create a window structure.
StartPage class: Handles the user authentication for the log in.
PageOne class: Display of the data that is loaded from the database, calls gui implementation method, uses refresh elements function, calls worker function to refresh all the data including all operations.

 Workerfunction.py:
Worker class: Retrieves good and bad words from the database, calls resume selection method and classifies the resumes.


 ResumeSelection.py:
Searches through the file and returns the decision of the decline or acceptance.

 Resumes.py:
Has Attributes as grade, name, acceptance and reason

 ReadFile.py:
Retrieves the resume id and the text from the Resumes table in the database.

 Main.py:
Uploads the resume images to the database.

 Images.py:
Image object class

 GUIImplementation.py:
Listboxes are created and data is inserted to the listboxes.

 Grading.py:
Determines prespecified grading types using increment, decrement or int.

 FileReader.py:
Reads file and stores elements into an array

 FilePathFinder.py:
Finds the files to be processed in the given folder. 

 DatabaseConnection.py:
All the database functions considering storing, retrieving and manipulating the data.

 CountriesTry.py:
Reads the countries.json file.

 Index.py:
Inserts the text file of the resumes to the database and updates the previous version if a newer version is inserted.

 Asd.py:
Uses Google-cloud to transform the image into text and extracts resume ID.
