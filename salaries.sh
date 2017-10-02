#!/bin/bash

#f=$1
f="salaries.csv"

echo "(1) TOP SALARIES IN THE CITY!!"
# Remove dollar signs, sort the appropriate column, and show the top few.
grep '\$' salaries.csv | sed 's/\$//g'| sort -k8 -t, -n -r |head

echo "(2) CITY EMPLOYEES"
# Count the lines, but careful of headers....
sed -i '1d' salaries.csv
wc -l salaries.csv

echo "(3 and 4) :: FULL AND PART-TIME WORKERS"
# Cut out the apppropriate column, sort it, and count the types.
# full time workers
cut -f5 -d, salaries.csv | sort | grep F | wc -l
# part time workers
cut -f5 -d, salaries.csv | sort | grep P | wc -l

echo "(5 and 6) HIGHEST HOURLY WAGES"
# Same approach as the first question.
grep -i hourly salaries.csv | sort -k9 -t, -n -r | head

echo "(7) POLICE DEPARTMENT"
# Just grep out the department and count the lines.
sort -k4 -t, salaries.csv | grep "POLICE" | wc -l

echo "(8) DETECTIVES"
# One more grep than the last.
sort -k4 -t, salaries.csv | grep "POLICE" | grep "DETECTIVE" |wc -l


echo "(9) THE MODAL FIREMAN"
# grep out the fire department, cut the salary column, sort it and count the number with each salary.
# Then sort these and print the the most common occurrence.
grep "FIRE" salaries.csv | cut -f8 -d, | sort -n -r | uniq -c | sort -necho

echo "(10) NAMES FOR POLICE OFFICERS"
# sed to remove last names (preceding the first comma).
# grep for police officers, and then remove everything else in the line.
# sort the names, and use uniq to get their frequencies.
grep -i "police officer" salaries.csv | cut -f2 -d, | awk '{print$1;}' | sort -rn | uniq -c | sort -n
