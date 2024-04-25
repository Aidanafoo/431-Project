# 431-Project
Final Project Repository for CMPSC-431
Setting up database:
-There is a file titled “database-setup.sql”, run this script in the appropriate environment to create the project database and associated tables 
    --(NOTE: these will need to be populated once created, attempting to query data will result in nothing being returned or an error fetching keys)
-You may be prompted to enter a username and password, in which case enter your postgres username and password
-	NOTE: you must edit the “project_431.py” file (can be done with a text editor), at the top of the code, in the first try catch block, update username and password accordingly
- If there is an error creating the database I am very sorry, I myself am still unsure how the DDL functions in postgres and it has been a struggle to work with

Using CLI:
- Navigate to the location of the “project_431.py” file (same as this readme), enter “python python_431.py” into the console (without quotations)
 - It will Bring you to the home page which will look like this:


Enter 0 to exit the program, or 1-4 to enter the subsequent submenus
 - 1 for “update game” (page 3 of manual)
 -	2 for “add game” (page 4 of manual)
 -	3 for “delete game” (page 4 of manual)
 -  4 for “select games” (page 5 of manual)


