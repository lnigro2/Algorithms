#Luke Nigro
#Programming Assignment 1: Insertion Sort
import time
#Function that runs the Insertion Sorting Algorithm
def Isort():
    
    #Prompts the user to enter the name of the file to be sorted
    filename = input("What file would you like to sort? ")  #Prompt user to enter file
    f = open(filename, 'r').read()                          #Open and read file
    
    #Stores the stream of numbers from input as a list of integers
    nums =  [int(i) for i in f.split(';')]
    
    #Stores the length of the list as n
    n = len(nums)
    
    #Initialize the Insertion Sort
    for j in range(1, n):
        key = nums[j]                       #Sets the key to jth value
        i = j - 1                           #initializes i at j - 1
        while i > -1 and nums[i] > key:     #i > -1 because of python indexing at 0
            nums[i + 1] = nums[i]           
            i = i - 1
        nums[i + 1] = key                   #Sets the terminal value to key value
    
    #Creates the answer.txt file
    answer_file = open('answer.txt', 'w')   #Name the file to write sorted numbers to
    
    #Writes the all but the last of the sorted numbers to the answer.txt file
    for n in nums[0:len(nums)-1]:
        answer_file.write('{0}; '.format(n))

    #Writes the last of the sorted numbers to answer.txt
    answer_file.write(str(nums[len(nums)-1]))
    answer_file.close()
            
def RunIsort():
    try:
        Isort()

    #Handles invalid file inputs and prompts the user to enter a valid file
    except IOError:
        print("File not found or path is incorrect")
        time.sleep(2.0)

    #Handles errors caused by elements of the input file that cannot be
    #converted to integer format
    except ValueError:
        print("ValueError: Not all data was convertable to integers.")
        time.sleep(2.0)

    else:
        print("File was successfully sorted!")
        time.sleep(2.0)

RunIsort()