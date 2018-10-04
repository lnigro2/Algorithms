# -*- coding: utf-8 -*-
"""
Created on Wed Oct 03 14:59:28 2018

@author: nigrolu
"""
import sys
import re
import random
import time

start = time.time() *1000

def text_to_list(filename):
    f = open(filename, 'r').read()
    A = [float(i.strip()) for i in re.split(';|\n', f)]
    return A

def write_answerfile(A, filename, runtime, answer_file):
    answer_file.write('\nSorting Result\n{} sorted: '.format(filename))
    for n in A:
        answer_file.write('{}; '.format(n))
        
    answer_file.write("\n\nPerformance Analysis\nInput file: {}\nInput size: {}\nSorting Time (in milliseconds): {}ms\n".format(filename, len(A), runtime))

def swap(x, y):
    x, y = y, x
    return x, y

def partition(A, p, r):
    x = A[r]
    i = p - 1
    
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = swap(A[i], A[j])
    A[i + 1], A[r] = swap(A[i + 1], A[r])
    
    return i + 1

def random_part(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = swap(A[r], A[i])
    return partition(A, p, r)

def quicksort(A, p , r):
    if p < r:
        q = random_part(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

filenames = sys.argv[1:]
answer_file = open('answer.txt', 'w')

for file in filenames:
    A = text_to_list(file)
    quicksort(A, 0, len(A) - 1)
    runtime = time.time() * 1000 - start
    write_answerfile(A, file, runtime, answer_file)

answer_file.close()