from vpython import *
from numpy import matlib
import math

import numpy as np



scene.caption = ""
scene.camera.pos = vector(30, 0, -30)
scene.camera.axis = vector(-10, -10, -10)
scene.center = vector(5, 15, 5)
scene.autoscale = False


H0_3 = [[1, 0, 0, 10], [0, 0, -1, 2.5], [0, -1, 0, -10], [0, -1, 0, 0]]


#-----------3rd cylinder and its line----------

cylinder3 = cylinder(pos = vector(10, 0, -10),
          axis=vector(0, 1, 0),
          length = 5, 
          radius = 1, 
          color = vector(1, 1, 0)) 

cylinder3_line1 = box(pos = vector(15, 2.5, -10),  
    size = vector(0.5, 5, 0.5), 
    color = vector(1, 1, 0)) 

cylinder3_line2 = box(pos = vector(12.5, 5, -10),  
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 

cylinder3_line3 = box(pos = vector(12.5, 0, -10),  
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 

cylinder3_line4 = box(pos = vector(17.5, 2.5, -10),
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 

group_3=compound([cylinder3, cylinder3_line1, cylinder3_line2, cylinder3_line3, cylinder3_line4], origin=vector(10, 2.5, -10))

#-----------------------------------------



#-----------2nd cylinder and its line-------------

cylinder2 = cylinder(pos = vector(0, 0, -10),
          axis=vector(0, 1, 0),
          length = 5, 
          radius = 1, 
          color = vector(1, 1, 0)) 

cylinder2_line1 = box(pos = vector(5, 2.5, -10),              
    size = vector(0.5, 5, 0.5), 
    color = vector(1, 1, 0)) 

cylinder2_line2 = box(pos = vector(2.5, 5, -10),
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 

cylinder2_line3 = box(pos = vector(2.5, 0, -10),
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 

cylinder2_line4 = box(pos = vector(7.5, 2.5, -10),
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 

group_2=compound([cylinder2, cylinder2_line1, cylinder2_line2, cylinder2_line3, cylinder2_line4], origin=vector(0, 2.5, -10))

#----------------------------------------------




#---------1st cylinder and line----------


cylinder1 = cylinder(pos = vector(0, 0, 0),
          axis=vector(0, 0, 1),
          length = 5, 
          radius = 1, 
          color = vector(1, 1, 0))

cylinder1_line1 = box(pos = vector(0, 0, -5),  
    size = vector(0.5, 0.5, 10), 
    color = vector(1, 1, 0))

#group_1=compound([cylinder1, cylinder1_line1])

#----------------------------------------



a1 = -10
a2 = 10
a3 = 10

T1 = 0
T2 = 0
T3 = 0


#print(H0_1)
#print(H0_2)

#print(H0_3[:,3][0])



def rotate_x(event):
    global T1
    global T2
    global T3

    if event.key == 'a':
        T1 = T1 + 5

    if event.key == 'b':
        T1 = T1 - 5
        
    if event.key == 'c':
        T2 = T2 + 5
       
    if event.key == 'd':
        T2 = T2 - 5
        
    if event.key == 'e':
        T3 = T3 + 5
        
    if event.key == 'f':
        T3 = T3 - 5

    T1_radians = (T1/180.0)*np.pi
    T2_radians = (T2/180.0)*np.pi
    T3_radians = (T3/180.0)*np.pi

    R00_1=[[1, 0, 0], [0, 0, -1], [0, -1, 0]]
    R11_2=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    R22_3=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    R0_1=[[np.cos(T1_radians), -np.sin(T1_radians), 0], [np.sin(T1_radians), np.cos(T1_radians), 0], [0, 0, 1]]
    R1_2=[[np.cos(T2_radians), -np.sin(T2_radians), 0], [np.sin(T2_radians), np.cos(T2_radians), 0], [0, 0, 1]]
    R2_3=[[np.cos(T3_radians), -np.sin(T3_radians), 0], [np.sin(T3_radians), np.cos(T3_radians), 0], [0, 0, 1]]

    R0_1=np.dot(R0_1, R00_1)
    R1_2=np.dot(R1_2, R11_2)
    R2_3=np.dot(R2_3, R22_3)

    #R0_2=np.dot(R0_1, R1_2)
    #R0_3=np.dot(R0_2, R2_3)

    d0_1=[[0], [0], [a1]]
    d1_2=[[a2*np.cos(T2_radians)], [a2*np.sin(T2_radians)], [0]]
    d2_3=[[a3*np.cos(T3_radians)], [a3*np.sin(T3_radians)], [0]]

    H0_1=np.concatenate((R0_1, d0_1), 1)
    H0_1=np.concatenate((H0_1, [[0, 0, 0, 1]]), 0)

    H1_2=np.concatenate((R1_2, d1_2), 1)
    H1_2=np.concatenate((H1_2, [[0, 0, 0, 1]]), 0)

    H2_3=np.concatenate((R2_3, d2_3), 1)
    H2_3=np.concatenate((H2_3, [[0, 0, 0, 1]]), 0)

    H0_2=np.dot(H0_1, H1_2)
    H0_3=np.dot(H0_2, H2_3)


    if event.key == 'a' or event.key == 'b':
        group_2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
        group_2.axis = vector(H0_2[:,0][0], H0_2[:,0][1], H0_2[:,0][2])


        group_3.pos = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])
        group_3.axis = vector(H0_3[:,0][0], H0_3[:,0][1], H0_3[:,0][2])
        #group_3.origin = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])

        
    if event.key == 'c' or event.key == 'd':
        group_2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
        group_2.axis = vector(H0_2[:,0][0], H0_2[:,0][1], H0_2[:,0][2])


        group_3.pos = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])
        group_3.axis = vector(H0_3[:,0][0], H0_3[:,0][1], H0_3[:,0][2])
        #group_3.origin = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])

       
        
    if event.key == 'e' or event.key == 'f':
        #group_2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
        #group_2.axis = vector(-H0_2[:,2][1], H0_2[:,2][0], H0_2[:,2][2])


        #group_3.pos = vector(H0_3[:,3][0], H0_3[:,3][1], H0_3[:,3][2])
        group_3.axis = vector(H0_3[:,0][0], H0_3[:,0][1], H0_3[:,0][2])
        #group_3.origin = vector(H0_3[:,3][0], H0_3[:,3][1], H0_3[:,3][2])



    if event.key == 'a' or event.key == 'b' or event.key == 'c' or event.key == 'd' or event.key == 'e' or event.key == 'f':
        print(H0_1[:])
        print(H0_2[:])
        print(H0_3[:])
        print("------------------")
       

scene.bind('keydown', rotate_x)

while True:
    rate(60)

