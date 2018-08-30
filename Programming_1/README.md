# Programming 1 - Insertion Sort
##### Luke Nigro

---
## Program Description
This is a fairly straightforward program that I have created, which takes an ambiguous .txt file which contains a semicolon delimited list of integers and transforms it into a python list. The program then takes that list and runs it through an insertion sort algorithm, which will reproduce the original list of integers such that n\`<sub>1</sub> < n\`<sub>2</sub> < ... < n\`<sub>n</sub>. It then takes this new sorted list and writes it to a new file named answer.txt and writes the file to the same directory that the Isort.py program is in.

The program activates the insertion sort with another function named RunIsort, which also error checks for the end user. If an invalid filepath or a file that does not exist is entered into the command line, this raises an `IOError` and informs the user that they have entered an invalid file. If the file entered contains elements that are non-convertible to an integer, this raises a `ValueError` and prompts the user to edit the file, or choose a new one. Finally, if the program runs correctly, it informs the user that this has happened.

---

## Algorithm Breakdown
This is a standard insertion sort algorithm which more or less follows the insertion sort algorithm's pseudocode exactly. Some slight adjustments needed to be made since Python starts indexing lists at 0 rather than 1, but it is otherwise standard.

Since this is a standard insertion sort algorithm, in the worst case scenario it should run in &theta;(n^2)
time.

---
## Compiler/Platform Used

I used the spyder platform to write the Isort.py program, and tested the program on the spyder IDE and the command line to make sure it worked in both environments. To write the README file, I used Sublime Text 3.

---
## What Does and What Does Not Work
For the most part everything works as expected so long as the program description is followed. The Isort program consistently sorts numbers from least to greatest so long as initial inputs are correct.

One improvement which could be made would be to allow float values as well and have the program sort all real numbers, and not just integers. Due to the scope of the assignment it did not seem like this was necessary, so files that are entered into the program which contain float type elements will raise a `ValueError`.

---
## Data Structure Design
The data from the .txt file is stored in a python list format. All of the sorting is done within the python list, and the elements of the sorted list are printed to the answer.txt file.

---