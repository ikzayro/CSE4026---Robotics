from vpython import *
from numpy import matlib
import math

import numpy as np



scene.caption = ""
scene.camera.pos = vector(0, 0, 10)
scene.camera.axis = vector(-10, -10, -10)
scene.center = vector(5, 5, 5)
scene.autoscale = False



#---------6rd cylinder and line----------


cylinder6 = cylinder(pos = vector(27.5, 0, 10),
          axis=vector(1, 0, 0),
          length = 2.5, 
          radius = 1, 
          color = color.blue)

cylinder6_line1 = box(pos = vector(30, 0, 10),  
    size = vector(5, 0.5, 0.5), 
    color = color.blue) 

group_6=compound([cylinder6, cylinder6_line1], origin=vector(27.5, 0, 10))

#----------------------------------------



#---------5rd cylinder and line----------


cylinder5 = cylinder(pos = vector(25, 0, 8.75),
          axis=vector(0, 0, 1),
          length = 2.5, 
          radius = 1, 
          color = color.cyan)

cylinder5_line1 = box(pos = vector(26.25, 0, 10),  
    size = vector(2.5, 0.5, 0.5), 
    color = color.cyan) 

group_5=compound([cylinder5, cylinder5_line1], origin=vector(25, 0, 8.75))

#----------------------------------------


#---------4rd cylinder and line----------


cylinder4 = cylinder(pos = vector(20, 0, 10),
          axis=vector(1, 0, 0),
          length = 2.5, 
          radius = 1, 
          color = color.magenta)

cylinder4_line1 = box(pos = vector(22.5, 0, 10),  
    size = vector(5, 0.5, 0.5), 
    color = color.magenta) 

group_4=compound([cylinder4, cylinder4_line1], origin=vector(20, 0, 10))

# group_all=compound([cylinder6, cylinder6_line1, cylinder5, cylinder5_line1, cylinder4, cylinder4_line1], origin=vector(20, 0, 10))

#----------------------------------------


#-----------3rd cylinder and its line----------

cylinder3 = cylinder(pos = vector(10, 0, 10),
          axis=vector(0, 1, 0),
          length = 2.5, 
          radius = 1, 
          color = vector(1, 1, 0)) 

cylinder3_2 = cylinder(pos = vector(10, 0, 10),
          axis=vector(0, -1, 0),
          length = 2.5, 
          radius = 1, 
          color = vector(1, 1, 0)) 

cylinder3_line4 = box(pos = vector(17.5, 2.5, 10),
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 

#-----------------------------------------



#-----------2nd cylinder and its line-------------

cylinder2 = cylinder(pos = vector(0, 0, 10),
          axis=vector(0, 1, 0),
          length = 2.5, 
          radius = 1, 
          color = vector(1, 1, 0)) 

cylinder2_2 = cylinder(pos = vector(0, 0, 10),
          axis=vector(0, -1, 0),
          length = 2.5, 
          radius = 1, 
          color = vector(1, 1, 0)) 


cylinder2_line4 = box(pos = vector(7.5, 2.5, 10),
    size = vector(5, 0.5, 0.5), 
    color = vector(1, 1, 0)) 


#----------------------------------------------




#---------1st cylinder and line----------


cylinder1 = cylinder(pos = vector(0, 0, 0),
          axis=vector(0, 0, 1),
          length = 5, 
          radius = 1, 
          color = vector(1, 1, 0))

cylinder1_line1 = box(pos = vector(0, 0, 5),  
    size = vector(0.5, 0.5, 10), 
    color = vector(1, 1, 0))


#----------------------------------------



a1 = 10
a2 = 10
a3 = 10
a4 = 10
a5 = 10
a6 = 10

# T1 = 0
# T2 = 0
# T3 = 0


#print(H0_1)
#print(H0_2)

#print(H0_3[:,3][0])

x0_3=10
y0_3=10
z0_3=10


def inverse_kinematics(x0, y0, z0, a1, a2, a3):

    # Compute theta1
    theta1 = math.atan(y0 / x0)

    r1 = math.sqrt(x0 ** 2 + y0 ** 2)
    r2 = z0 - a1
    r3 = math.sqrt(r1 ** 2 + r2 ** 2)

    temp1 = ((a3 ** 2) - (a2 ** 2) - (r3 ** 2))
    temp2 = ((-2) * a2 * r3)
    temp3 = temp1 / temp2

    alpha1 = math.acos(((a3 ** 2) - (a2 ** 2) - (r3 ** 2)) / ((-2) * a2 * r3))
    alpha2 = math.atan2(r2, r1)

    # Compute theta2
    theta2 = alpha2 - alpha1

    alpha3 = math.acos(((r3 ** 2) - (a2 ** 2) - (a3 ** 2)) / ((-2) * a2 * a3))

    # Compute theta3
    theta3 = alpha3

    # Convert angles to degrees 
    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)
    theta3_deg = 180 - math.degrees(theta3)

    return theta1_deg, theta2_deg, theta3_deg


T1, T2, T3 = inverse_kinematics(x0_3, y0_3, z0_3, a1, a2, a3)


T1_radians = (T1/180.0)*np.pi
T2_radians = (T2/180.0)*np.pi
T3_radians = (T3/180.0)*np.pi


# T4_radians = (T4/180.0)*np.pi
# T5_radians = (T5/180.0)*np.pi
# T6_radians = (T6/180.0)*np.pi

# R00_1=[[1, 0, 0], 
#        [0, 0, 1], 
#        [0, -1, 0]]

# R11_2=[[1, 0, 0], 
#        [0, 1, 0], 
#        [0, 0, 1]]

# R22_3=[[0, 0, 1], 
#        [0, -1, 0], 
#        [1, 0, 0]]

# R33_4=[[1, 0, 0], 
#        [0, 0, 1], 
#        [0, -1, 0]]

# R44_5=[[1, 0, 0],
#         [0, 0, -1], 
#         [0, 1, 0]]

# R55_6=[[1, 0, 0], 
#        [0, 1, 0], 
#        [0, 0, 1]]


R00_1=[[1, 0, 0], [0, 0, -1], [0, 1, 0]]
R11_2=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
R22_3=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

R0_1=[[np.cos(T1_radians), -np.sin(T1_radians), 0], [np.sin(T1_radians), np.cos(T1_radians), 0], [0, 0, 1]]
R1_2=[[np.cos(T2_radians), -np.sin(T2_radians), 0], [np.sin(T2_radians), np.cos(T2_radians), 0], [0, 0, 1]]
R2_3=[[np.cos(T3_radians), -np.sin(T3_radians), 0], [np.sin(T3_radians), np.cos(T3_radians), 0], [0, 0, 1]]

R0_1=np.dot(R0_1, R00_1)
R1_2=np.dot(R1_2, R11_2)
R2_3=np.dot(R2_3, R22_3)

R0_2=np.dot(R0_1, R1_2)
R0_3=np.dot(R0_2, R2_3)

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





R0_6 = [[1, 0, 0], 
       [0, 1, 0], 
       [0, 0, 1]]

invR0_3 = np.linalg.inv(R0_3)

R3_6 = np.dot(invR0_3, R0_6)

#print(R3_6)

T5_radians = np.arccos(R3_6[2][2])
T6_radians = np.arccos(-R3_6[2][0]/np.sin(T5_radians))
T4_radians = np.arccos(R3_6[1][2]/np.sin(T5_radians))

print(T1_radians);print(T2_radians);print(T3_radians);
print(T4_radians);print(T5_radians);print(T6_radians);

d3_6 = [[0], [0], [0]]

H3_6=np.concatenate((R3_6, d3_6), 1)
H3_6=np.concatenate((H3_6, [[0, 0, 0, 1]]), 0)

H0_6=np.dot(H0_3, H3_6)
print(H0_6)

# R3_4=[[np.cos(T4_radians), -np.sin(T4_radians), 0], [np.sin(T4_radians), np.cos(T4_radians), 0], [0, 0, 1]]
# R4_5=[[np.cos(T5_radians), -np.sin(T5_radians), 0], [np.sin(T5_radians), np.cos(T5_radians), 0], [0, 0, 1]]
# R5_6=[[np.cos(T6_radians), -np.sin(T6_radians), 0], [np.sin(T6_radians), np.cos(T6_radians), 0], [0, 0, 1]]

# R3_4=np.dot(R3_4, R33_4)
# R4_5=np.dot(R4_5, R44_5)
# R5_6=np.dot(R5_6, R55_6)

# R3_5=np.dot(R3_4, R4_5)
# R3_6=np.dot(R3_5, R5_6)


# d3_4=[[0], [0], [a4]]
# d4_5=[[a5*np.cos(T5_radians)], [a5*np.sin(T5_radians)], [0]]
# d5_6=[[0], [0], [a6]]


# H3_4=np.concatenate((R3_4, d3_4), 1)
# H3_4=np.concatenate((H3_4, [[0, 0, 0, 1]]), 0)

# H4_5=np.concatenate((R4_5, d4_5), 1)
# H4_5=np.concatenate((H4_5, [[0, 0, 0, 1]]), 0)

# H5_6=np.concatenate((R5_6, d5_6), 1)
# H5_6=np.concatenate((H5_6, [[0, 0, 0, 1]]), 0)

# H3_5=np.dot(H3_4, H4_5)
# H3_6=np.dot(H3_5, H5_6)


# H0_6=np.dot(H0_3, H3_6)

# print(H0_6)

end_effector = vector(H0_3[:,3][0], H0_3[:,3][1], H0_3[:,3][2])

cylinder2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
cylinder2.axis = vector(H0_2[:,2][0], H0_2[:,2][1], H0_2[:,2][2])
cylinder2.length = 2.5

cylinder2_2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
cylinder2_2.axis = vector(-H0_2[:,2][0], -H0_2[:,2][1], -H0_2[:,2][2])
cylinder2_2.length = 2.5


cylinder3.pos = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])
cylinder3.axis = vector(H0_3[:,2][0], H0_3[:,2][1], H0_3[:,2][2])
cylinder3.length = 2.5
#group_3.origin = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])

cylinder3_2.pos = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])
cylinder3_2.axis = vector(-H0_3[:,2][0], -H0_3[:,2][1], -H0_3[:,2][2])
cylinder3_2.length = 2.5
#group_3.origin = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])
        

cylinder2_line4.pos = cylinder2.pos + ((cylinder3.pos - cylinder2.pos) / 2)
cylinder2_line4.axis = cylinder3.pos - cylinder2.pos
        
cylinder3_line4.pos = cylinder3.pos + ((end_effector - cylinder3.pos) / 2)
cylinder3_line4.axis = end_effector - cylinder3.pos
#group_3.origin = vector(H0_3[:,3][0], H0_3[:,3][1], H0_3[:,3][2])

# group_all.pos = vector(H0_6[:,3][0], H0_6[:,3][1], H0_6[:,3][2])

group_4.pos = vector(H0_6[:,3][0], H0_6[:,3][1], H0_6[:,3][2])
group_4.axis = vector(H0_6[:,0][0], H0_6[:,0][1], H0_6[:,0][2])

# group_5.pos = vector(H0_6[:,3][0]+5, H0_6[:,3][1], H0_6[:,3][2]-1.25)
group_5.pos = vector(H0_6[:,3][0], H0_6[:,3][1], H0_6[:,3][2])
group_5.axis = vector(H0_6[:,1][0], H0_6[:,1][1], H0_6[:,1][2])

# group_6.pos = vector(H0_6[:,3][0]+7.5, H0_6[:,3][1], H0_6[:,3][2])
group_6.pos = vector(H0_6[:,3][0], H0_6[:,3][1], H0_6[:,3][2])
group_6.axis = vector(H0_6[:,2][0], H0_6[:,2][1], H0_6[:,2][2])










# def rotate_x(event):
#     global T1
#     global T2
#     global T3

#     if event.key == 'a':
#         T1 = T1 + 5

#     if event.key == 'b':
#         T1 = T1 - 5
        
#     if event.key == 'c':
#         T2 = T2 + 5
       
#     if event.key == 'd':
#         T2 = T2 - 5
        
#     if event.key == 'e':
#         T3 = T3 + 5
        
#     if event.key == 'f':
#         T3 = T3 - 5

#     T1_radians = (T1/180.0)*np.pi
#     T2_radians = (T2/180.0)*np.pi
#     T3_radians = (T3/180.0)*np.pi

#     R00_1=[[1, 0, 0], [0, 0, 1], [0, -1, 0]]
#     R11_2=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#     R22_3=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#     R0_1=[[np.cos(T1_radians), -np.sin(T1_radians), 0], [np.sin(T1_radians), np.cos(T1_radians), 0], [0, 0, 1]]
#     R1_2=[[np.cos(T2_radians), -np.sin(T2_radians), 0], [np.sin(T2_radians), np.cos(T2_radians), 0], [0, 0, 1]]
#     R2_3=[[np.cos(T3_radians), -np.sin(T3_radians), 0], [np.sin(T3_radians), np.cos(T3_radians), 0], [0, 0, 1]]

#     R0_1=np.dot(R0_1, R00_1)
#     R1_2=np.dot(R1_2, R11_2)
#     R2_3=np.dot(R2_3, R22_3)

#     #R0_2=np.dot(R0_1, R1_2)
#     #R0_3=np.dot(R0_2, R2_3)

#     d0_1=[[0], [0], [a1]]
#     d1_2=[[a2*np.cos(T2_radians)], [a2*np.sin(T2_radians)], [0]]
#     d2_3=[[a3*np.cos(T3_radians)], [a3*np.sin(T3_radians)], [0]]

#     H0_1=np.concatenate((R0_1, d0_1), 1)
#     H0_1=np.concatenate((H0_1, [[0, 0, 0, 1]]), 0)

#     H1_2=np.concatenate((R1_2, d1_2), 1)
#     H1_2=np.concatenate((H1_2, [[0, 0, 0, 1]]), 0)

#     H2_3=np.concatenate((R2_3, d2_3), 1)
#     H2_3=np.concatenate((H2_3, [[0, 0, 0, 1]]), 0)

#     H0_2=np.dot(H0_1, H1_2)
#     H0_3=np.dot(H0_2, H2_3)


#     if event.key == 'a' or event.key == 'b':
#         group_2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
#         group_2.axis = vector(H0_1[:,0][0], H0_1[:,0][1], H0_1[:,0][2])


#         group_3.pos = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])
#         group_3.axis = vector(H0_3[:,0][0], H0_3[:,0][1], H0_3[:,0][2])
#         #group_3.origin = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])

        
#     if event.key == 'c' or event.key == 'd':
#         group_2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
#         group_2.axis = vector(H0_1[:,0][0], H0_1[:,0][1], H0_1[:,0][2])


#         group_3.pos = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])
#         group_3.axis = vector(H0_3[:,0][0], H0_3[:,0][1], H0_3[:,0][2])
#         #group_3.origin = vector(H0_2[:,3][0], H0_2[:,3][1], H0_2[:,3][2])

       
        
#     if event.key == 'e' or event.key == 'f':
#         #group_2.pos = vector(H0_1[:,3][0], H0_1[:,3][1], H0_1[:,3][2])
#         #group_2.axis = vector(-H0_2[:,2][1], H0_2[:,2][0], H0_2[:,2][2])


#         #group_3.pos = vector(H0_3[:,3][0], H0_3[:,3][1], H0_3[:,3][2])
#         group_3.axis = vector(H0_3[:,0][0], H0_3[:,0][1], H0_3[:,0][2])
#         group_3.origin = vector(H0_3[:,3][0], H0_3[:,3][1], H0_3[:,3][2])



#     if event.key == 'a' or event.key == 'b' or event.key == 'c' or event.key == 'd' or event.key == 'e' or event.key == 'f':
#         print(H0_1[:])
#         print(H0_2[:])
#         print(H0_3[:])
#         print("------------------")
       

# scene.bind('keydown', rotate_x)

while True:
    rate(60)







   