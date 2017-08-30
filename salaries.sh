#!/bin/bash

#f=$1
f="salaries.csv"

echo "(1) TOP SALARIES IN THE CITY!!"
# Remove dollar signs, sort the appropriate column, and show the top few.
cat $f | head -1
echo

echo "(2) CITY EMPLOYEES"
# Count the lines, but careful of headers....
cat $f | head -1
echo 

echo "(3 and 4) :: FULL AND PART-TIME WORKERS"
# Cut out the apppropriate column, sort it, and count the types.
cat $f | head -1
echo

echo "(5 and 6) HIGHEST HOURLY WAGES"
# Same approach as the first question.
cat $f | head -1
echo 

echo "(7) POLICE DEPARTMENT"
# Just grep out the department and count the lines.
cat $f | head -1
echo

echo "(8) DETECTIVES"
# One more grep than the last.
cat $f | head -1
echo

echo "(9) THE MODAL FIREMAN"
# grep out the fire department, cut the salary column, sort it and count the number with each salary.
# Then sort these and print the the most common occurrence.
cat $f | head -1
echo

echo "(10) NAMES FOR POLICE OFFICERS"
# sed to remove last names (preceding the first comma).
# grep for police officers, and then remove everything else in the line.
# sort the names, and use uniq to get their frequencies.
cat $f | head -1
echo

