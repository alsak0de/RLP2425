import sympy as sp
import numpy as np

# Define symbols
theta1, theta2, theta3 = sp.symbols('theta1 theta2 theta3')

# Forward kinematics matrix (from the notebook, simplified and with l1, l2, l3 = 0.2)
mbee = sp.Matrix([
    [sp.cos(theta1)*sp.cos(theta2)*sp.cos(theta3), 0, 0, (0.2*sp.cos(theta3) + 0.2)*sp.cos(theta1)*sp.cos(theta2)],
    [sp.sin(theta1)*sp.cos(theta2)*sp.cos(theta3), 0, 0, (0.2*sp.cos(theta3) + 0.2)*sp.sin(theta1)*sp.cos(theta2)],
    [sp.sin(theta2)*sp.cos(theta3), 0, 0, 0.2*sp.sin(theta2)*sp.cos(theta3) + 0.2*sp.sin(theta2) + 0.2],
    [0, 0, 0, 1]
])

# Joint angles in degrees (from your solution)
theta1_deg = -0.0
theta2_deg = 33.69
theta3_deg = 36.604

# Convert to radians
theta1_val = np.deg2rad(theta1_deg)
theta2_val = np.deg2rad(theta2_deg)
theta3_val = np.deg2rad(theta3_deg)

# Substitute values into the matrix
subs = {
    theta1: theta1_val,
    theta2: theta2_val,
    theta3: theta3_val
}

# Evaluate the position
fk = mbee.subs(subs)
x = float(fk[0, 3])
y = float(fk[1, 3])
z = float(fk[2, 3])

print(f"FK position: x={x:.5f}, y={y:.5f}, z={z:.5f}")
print("Target position: x=0.3, y=0, z=0.4")
print(f"Error: dx={x-0.3:.5f}, dy={y-0.0:.5f}, dz={z-0.4:.5f}") 