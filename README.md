# Assignment 1: Welcome to the Command Line   

Your main task this week is to install the software that you will use for the rest of this class.
You will also do some basic navigation of Chicago crime and city salaries, with command line tools.
To "accept" the assignment and create your repository,
  you must first complete the setup instructions below,
  including creating your GitHub account.
This week's assignment is graded only for completeness.
That means: the installation is shown to be working,
  and there are reasonable answers for all of the qustions.

This assignment is due Wednesday October 4 at 1:30am.
A computer will collect it -- not me.  So don't be late!!

## Preliminaries/Setup

Please see separate instructions for [Windows](windows_install_instructions.md) and [Macs](mac_install_instructions.md),
  to install your terminal, python, and text editor.

You can then join this assignment [here](https://classroom.github.com/assignment-invitations/8cfa1521ab98e0dfb7341771721f793b).  You'll get an email telling you that the import is complete.
* Open the Terminal and navigate (`cd`) to whatever directory (folder) you want to work from.
  The choice of directory is up to you -- just as you'd save the documents for any other class.
  Remember that a terminal is analogous to Windows Explorer or Mac Finder.  It allows you to navigate and access your files.
  * On Cygwin, your "normal" directory structure (your C:\ drive) lives at `/cygdrive/c/`.
* Issue ```git clone git@github.com:harris-ippp/hw-1-UserName.git``` (replacing `Username` by your GitHub user name), to download the directory.
* Now `cd` into that directory (`hw-1-UserName`) to get started.
* Issue the command `./test-suite.py`.  It should end by `Congrats!  Check-out looks great!` 
  It will also create a `test-suite.txt` file, that you will submit as part of your homework, 
    along with `density.pdf` and `ba_frac.pdf`.
  If you don't get the `Congrats!` or if the pictures are blank...
    if it fails in any way, it will not work for you in the long run.
  Try to figure out, but if you can't you **must get help!!** 
  The TAs and I will be very generous with help this week, with several sessions.
  But we cannot do this for the entire quarter,
    and any technical problems will make your subsequent assignments and lecture participation much more frustrating!!

<details><summary>FAQs and Common Problems</summary>
* We'll see what questions we get...
</details>


## Command Line Tools

### Downloading some data.

In class, we played with the city salaries file. 
You can check out these data on the excellent [Chicago Data Portal](https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/xzkq-xp2w).
They have some nice interactive tools for grabbing and analyzing these data.
We'll get into some of their APIs, later on.
For now, we can just curl it:

```
curl data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv -s -o salaries.csv
```

### Exercises!

You now have salaries.csv in your homework directory.
The script `salaries.sh` suggests formatting for stepping through these questions.
Fill you answers in, there
Put each of your responses into `SOLUTIONS`.
These have structures for each of the questions below, which you'll fill out.  Open these files with Atom; then one step at a time replace the `cat` commands on each line, to complete the scripts.  (See [salaries.sh](https://github.com/harris-ippp/01-welcome/blob/master/salaries.sh) for an example.)  When you're done, fill in SOLUTIONS, as directed. 

So: you will modify the files in the directory, and then send it back to GitHub.  Since you've made a copy of the repository by accepting the assignment, all of your work will be separate and will not interfere with your classmates.  We will see your edited files (provided that you uploaded them on git), and you can check this too, by navigating to your own repository on your GitHub page. 

#### Salaries

1. Which salaried worker makes the most?
2. How full-time workers are there in the file?
3. How part-time workers are there in the file?  (Check you work for 1, with 2 and 3.)
4. What is the highest hourly wage in the city?
5. Excluding the top four workers (who are doctors), what is the highest hourly wage?
6. How many police officers are there in Chicago?
7. How many of them are detectives?
8. How much does the modal fireman (employee of the fire department) make?
9. What is the most common women's name for police officers?

## Push to GitHub

When you're all done, commit and push the code:
```
git add *pdf *sh SOLUTIONS test-suite.txt # add the relevant files
git status # check that all your modified files are listed
git commit -m "phewff, all done!"
git push
```

Now go online to your GitHub page (with substitutions!), to check that everything is there:

* https://github.com/MyGitHubName/hw-1-welcome

You should have committed five files: `salaries.sh`, `SOLUTIONS`, `ba_frac.pdf`, `density.pdf`, and `test-suite.txt`.

Make sure it's in before Wednesday October 4th at 1:30am!


### Helpful Readings
* Git: [Hello World](https://guides.github.com/activities/hello-world/), GitHub Guides.

### Suggested Readings
* Data and Technology in Government: [Innovative State](https://smile.amazon.com/Innovative-State-Aneesh-Chopra/dp/0802121349/) (Aneesh Chopra), and [The Responsive City](https://smile.amazon.com/Responsive-City-Communities-Data-Smart-Governance-ebook/dp/B00MQTIA3M/) (Stephen Goldsmith and Susan Crawford).



