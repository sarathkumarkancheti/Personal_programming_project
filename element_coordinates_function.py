# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:03:23 2024

@author: sarat
"""

def element_coordinates(element_number):
    import numpy as np
    #creating an empty array to store integers
    nnodes = np.array([])
    xcoods = np.array([])
    ycoods = np.array([])
    #opening input file from abaqus
    with open(r"C:\Users\sarat\Desktop\files\Job-1.inp") as file:
        data = file.readlines()
        line_number = 193
        if 1<=line_number<= len(data):
           left = data[line_number-1].strip().split(",")
           left_edge = np.array(left, dtype=int)             #nodes on the left edge of sample
           #print(left_edge.shape)
        line_number1 = 197  
        if 1<=line_number1<= len(data):
            bottom = data[line_number1-1].strip().split(",")
            bottom_edge = np.array(bottom, dtype=int)        #bottom edge
            #print(bottom_edge)
        line_number2 = 201  
        if 1<=line_number2<= len(data):
            top = data[line_number2-1].strip().split(",")
            top_edge = np.array(top, dtype=int)              #top edge
            #print(top_edge)
        line_number3 = 205
        if 1<=line_number3<= len(data):
           right = data[line_number3-1].strip().split(",")
           right_edge = np.array(right, dtype=int)           #right edge
           #print(right_edge)
        for i in range(9,130):
            #dividing columns by comma
            nodes = data[i].strip().split(",")
            #allocating each string
            string = nodes[0]
            xstring = nodes[1]
            ystring = nodes[2]
            # Convert string to an integer/float
            number = int(string)
            xnumber = float(xstring)
            ynumber = float(ystring)
            # Add the number to the array
            nnodes = np.append(nnodes, number)
            xcoods = np.append(xcoods, xnumber)
            ycoods = np.append(ycoods, ynumber)        
    #creating an array combining node numbers, and both coordinates of the nodes
    #zeroth column indicates node number, first x coordinate, second is ycoordinate
    matrix = np.array([nnodes, xcoods, ycoods]).T
    with open(r"C:\Users\sarat\Desktop\files\Job-1.inp") as file1:
         ele_data = file1.readlines()
         ele = np.array([])
         elen1 = np.array([])
         elen2 = np.array([])
         elen3 = np.array([])
         elen4 = np.array([])
         elen5 = np.array([])
         elen6 = np.array([])
         for k in range(131,181):
             elestr = ele_data[k].strip().split(",")
             el= int(elestr[0])#converting string into integer for elements
             eln1 =int(elestr[1])
             eln2 =int(elestr[2])  
             eln3 =int(elestr[3])
             eln4 =int(elestr[4])
             eln5 =int(elestr[5])
             eln6 =int(elestr[6])
             ele = np.append(ele,el)
             elen1 = np.append(elen1,eln1)
             elen2 = np.append(elen2,eln2)
             elen3 = np.append(elen3,eln3)
             elen4 = np.append(elen4,eln4)
             elen5 = np.append(elen5,eln5)
             elen6 = np.append(elen6,eln6)
    col_arrays = np.array([ele,elen1,elen2,elen3,elen4,elen5,elen6])
    m =len(ele)
    matrix1 = [[0]*7 for _ in range(m)] #creating an empty matrix to store elements and nodes
    for i in range(7):
        for j in range(m):
            matrix1[j][i] = col_arrays[i][j] 
    #print(matrix1[18][:]) #list of elements[1] and corresponding npodes[2]
    ele_nod_list = []
    noden = np.array([matrix1[element_number-1][1:]]) #nodes of corresponding element
    for k in range(6):   
        for j in range(121):
            if noden[0][k]== matrix[j][0]: #matching nodes from element connectivity to node numbers
                ele_nod = matrix[j][1:]
                ele_nod_list.append(ele_nod)
    ele_coordinates = np.array(ele_nod_list) #coordinates of the element
    #print(noden)
    #print( ele_coordinates.shape)
    return noden, ele_coordinates