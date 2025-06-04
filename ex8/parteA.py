# We import the necessary libraries to work
import numpy as np
import sympy as sp
from sympy import *

from sympy.physics.vector import init_vprinting
init_vprinting(use_latex='mathjax', pretty_print=False)

# we declare the symbols (lengths, variables, etc.) that will be used for a later formulation.
from sympy.physics.mechanics import dynamicsymbols
theta1, theta2, theta3, l1, l2, l3, theta, alpha, a, d = dynamicsymbols('theta1 theta2 theta3 l1 l2 l3 theta alpha a d')

# The standard homogeneous transformation matrix is represented as:
rot = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha)],
                 [sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha)],
                 [0, sp.sin(alpha), sp.cos(alpha)]])

trans = sp.Matrix([a*sp.cos(theta),a*sp.sin(theta),d])
last_row = sp.Matrix([[0, 0, 0, 1]])
m = sp.Matrix.vstack(sp.Matrix.hstack(rot, trans), last_row)

# Transformation: 1st axis from '0' to '1'
m01 = m.subs({ theta:theta1, d:l1, a:0, alpha:90*np.pi/180})
m01[0,1]=0
m01[1,1]=0
m01[2,2]=0
print("m01:")
print(m01)

# Transformation: 2nd axis from '1' to '2'
m12 = m.subs({ theta:theta2, d:0, a:l2, alpha:0})
m12[0,1]=0
m12[1,1]=0
m12[2,2]=0
print("\nm12:")
print(m12)

# Transformation: 3rd axis from '2' to '3'
m23 = m.subs({ theta:theta3, d:0, a:l3, alpha:0})
m23[0,1]=0
m23[1,1]=0
m23[2,2]=0
print("\nm23:")
print(m23)

# Resulting Matrix without simplification
m03 = (m01*m12*m23)
print("\nm03 (without simplification):")
print(m03)

# Resulting Matrix with simplification
mbee = sp.Matrix([[sp.trigsimp(m03[0,0].simplify()), sp.trigsimp(m03[0,1].simplify()), sp.trigsimp(m03[0,2].simplify()), sp.trigsimp(m03[0,3].simplify())],
                 [sp.trigsimp(m03[1,0].simplify()), sp.trigsimp(m03[1,1].simplify()), sp.trigsimp(m03[1,2].simplify()), sp.trigsimp(m03[1,3].simplify())],
                 [m03[2,0].simplify(), m03[2,1].simplify(), m03[2,2].simplify(), sp.trigsimp(m03[2,3].simplify())],
                 [m03[3,0].simplify(), m03[3,1].simplify(), m03[3,2].simplify(), m03[3,3].simplify()]])

print("\nmbee (simplified):")
print(mbee)

# Substitute the values of l1, l2, l3 in the matrix
mbee = mbee.subs({ l1:0.2, l2:0.2, l3:0.2 })
print("\nmbee with numerical values:")
print(mbee) 