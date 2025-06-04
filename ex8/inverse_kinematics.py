import sympy as sp
from sympy.physics.mechanics import dynamicsymbols

# Define symbols
theta1, theta2, theta3 = dynamicsymbols('theta1 theta2 theta3')
x, y, z = 0.3, 0, 0.4  # Target point

# Define the equations
eq1 = (0.2*sp.cos(theta3) + 0.2)*sp.cos(theta1)*sp.cos(theta2) - x
eq2 = (0.2*sp.cos(theta3) + 0.2)*sp.sin(theta1)*sp.cos(theta2) - y
eq3 = 0.2*sp.sin(theta2)*sp.cos(theta3) + 0.2*sp.sin(theta2) + 0.2 - z

# Since y = 0, theta1 must be 0
theta1_sol = 0

# Define simplified equations
eq2_simplified = (0.2*sp.cos(theta3) + 0.2)*sp.cos(theta2) - x
eq3_simplified = 0.2*sp.sin(theta2)*sp.cos(theta3) + 0.2*sp.sin(theta2) + 0.2 - z

# Try different initial guesses
initial_guesses = [
    [sp.pi/4, sp.pi/4],    # 45 degrees
    [sp.pi/6, sp.pi/6],    # 30 degrees
    [sp.pi/3, sp.pi/3],    # 60 degrees
    [0, 0],                # 0 degrees
    [-sp.pi/4, -sp.pi/4]   # -45 degrees
]

solution_found = False
for guess in initial_guesses:
    try:
        sol = sp.nsolve([eq2_simplified, eq3_simplified], 
                       [theta2, theta3], 
                       guess,
                       method='hybr',
                       verify=False)
        
        # Check if solution is within reasonable bounds
        if abs(sol[0]) <= sp.pi and abs(sol[1]) <= sp.pi:
            solution_found = True
            break
    except:
        continue

if solution_found:
    print("Solution found!")
    print("\nSolution in radians:")
    print("theta1 =", theta1_sol)
    print("theta2 =", sol[0])
    print("theta3 =", sol[1])

    print("\nSolution in degrees:")
    print("theta1 =", float(theta1_sol*180/sp.pi))
    print("theta2 =", float(sol[0]*180/sp.pi))
    print("theta3 =", float(sol[1]*180/sp.pi))
else:
    print("No valid solution found with the given initial guesses.") 