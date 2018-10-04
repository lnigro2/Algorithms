# Programming 2 - QuickSort
##### Luke Nigro

---
## Program Description
This is a fairly straightforward program that I have created, which takes n .txt files which contain a semicolon and newline delimited list of real numbers and transforms it into a python list. The program then takes that list and runs it through an quicksort algorithm, which will reproduce the original list of integers such that n\`<sub>1</sub> < n\`<sub>2</sub> < ... < n\`<sub>n</sub>. It then takes this new sorted list and writes it, as well as a performance summary, to a new file named answer.txt and writes the file to the same directory that the Qsort.py program is in. The program activates the quicksort by directly calling the function.

---

## Algorithm Breakdown
This is a randomized-partition quicksort algorithm which more or less follows the algorithm's pseudocode exactly. I chose the randomized partitioning over standard partitioning in order to hopefully end up with a more consistent average-case

The worst case runtime scenario here is &theta;(n^2), however, it is likely that randomized partitioning will avoid the worst case of scenario by having reasonably balanced partitions, and achieve the average case of &theta;(n\*log(n)) time.

---
## Compiler/Platform Used

I used the spyder platform to write the Qsort.py program, and tested the program on the spyder IDE and the command line to make sure it worked in both environments. To write the README file, I used Sublime Text 3.

---
## What Does and What Does Not Work
For the most part everything works as expected so long as the program description is followed. The only problem that I consistenly have not been able to solve is avoiding ValueErrors when converting to float types. I often run into the problem where there is an errant space somewhere and the entire program fails.

Also a note on the performance: One would expect input size of 10^4 to be about 200x times slower that of 10^2, while this algorithm was able to sort the input in only 36x. 10^6 compared to 10^4 was a bit more in line with expectations, as it should be about 150x slower, and performed at 142x slower.

---
## Data Structure Design
The data from the .txt file is stored in a python list format. All of the sorting is done within the python list, and the elements of the sorted list are printed to the answer.txt file.

---