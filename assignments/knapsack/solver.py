#!/usr/bin/python
# -*- coding: utf-8 -*-


def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = []

    #Implementing Dynamic Programming
    #initionalize a two dimensional array
    table=[]
    for i in range(0,capacity+1):
        new=[]
        for j in range(0,items+1):
            new.append(0)
        table.append(new)

    #Filling the table
    for i in range(1,capacity+1):
        for j in range(1, items+1):
            if i-weights[j-1]<0:
                table[i][j]=table[i][j-1]
            else:
                if table[i-weights[j-1]][j-1] + values[j-1] > table[i][j-1]:
                    table[i][j]=table[i-weights[j-1]][j-1] + values[j-1]
                else:
                    table[i][j]=table[i][j-1]

    value=table[capacity][items]

    #Identifing the selected items
    current_row=capacity
    for j in range(items,0,-1):
        if table[current_row][j]==table[current_row][j-1]:
            taken.insert(0,0)
        else:
            current_row-=weights[j-1]
            taken.insert(0,1)

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

