# Programming 1 - Insertion Sort
##### Luke Nigro

---
## Program Description
This is a fairly straightforward program that I have created, which takes an ambiguous .txt file which contains a semicolon delimited list of integers and transforms it into a python list. The program then takes that list and runs it through an insertion sort algorithm, which will reproduce the original list of integers such that n\`1 < n\`2 < ... < n\`n. It then takes this new sorted list and writes it to a new file named answer.txt and writes the file to the same directory that the Isort.py program is in.

The program activates the insertion sort with another function named RunIsort, which also error checks for the end user. If an invalid filepath or a file that does not exist is entered into the command line, this raises an `IOError` and informs the user that they have entered an invalid file. If the file entered contains elements that are non-convertible to an integer, this raises a `ValueError` and prompts the user to edit the file, or choose a new one. Finally, if the program runs correctly, it informs the user that this has happened.

---

## Algorithm Breakdown

---
## Compiler/Platform Used

I used the spyder platform to write the Isort.py program, and tested the program on the spyder IDE and the command line to make sure it worked in both environments. To write the README file, I used Sublime Text 3.

---
## What Does and What Does Not Work

---
## Data Structure Design
The data from the .txt file is stored in a python list format 

---