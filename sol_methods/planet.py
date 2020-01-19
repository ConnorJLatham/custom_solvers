# this script aims to replicate the motion of objects subject to gravitational
# forces according to the equations presented in this paper:
# https://www.gsjournal.net/Science-Journals/Research%20Papers-Astrophysics/Download/3763

import numpy as np
import order_4 as o4
import matplotlib.pyplot as plt

# assume that object 1 is stationary at point 0,0,0
# this is all in (m, s, kg) btw

# assume a beginning position for the planet
p_0 = np.array([1.52e11, 0, 0])

# assume a beginning velocity
v_0 = np.array([0, 2.93e4, 0])

# assume a mass of stationary object
m_p = 1.989e30

# assume mass of moving object
m = 5.972e24

# define the universal gravitational constant
G = 6.67430e-11

# define the function that describes how the thing moves
def f_dot(t_n, y_n):
    y_dot = np.zeros(len(y_n))
    
    # get the position vector
    r = y_n[0:3]
    
    # find the magnitude of it 
    r_norm = (r[0]**2 + r[1]**2 + r[2]**2)**.5 
    
    # find the force magnitude 
    F = G*m*m_p/r_norm**2
    
    # find the force components
    y_dot[3:6] = -F*r*(1/m)/r_norm
    
    # reassign velocities to positions
    y_dot[0:3] = y_n[3:6]
    
    return y_dot
    
t_step = 10000
t_span = [0, 3.154e7]
y_0 = np.append(p_0, v_0)

states = o4.rk4_mul(f_dot, y_0, t_step, t_span)

plt.plot(states[0,:], states[1,:])
plt.grid()
plt.show()


