# -*- coding: utf-8 -*-

import random

n = 1000000

ints = [random.randint(-n,n) for i in range(n)]

sortable = open('input_3.txt', 'w')
for n in ints[0:len(ints)-1]:
    sortable.write('{};'.format(n))
sortable.write('{}'.format(ints[len(ints)-1]))