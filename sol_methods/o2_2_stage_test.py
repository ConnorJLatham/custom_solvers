import o2_2_stage as so
import numpy as np
from math import tan

# see wiki for their numerical test: 
# https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods

state = np.array([1, 2, 3, 4, 5])
t_step = .1
t_0 = 1

def func(t_n, y_n):
    y_dot = .1*y_n
    
    return y_dot

y_np1 = so.gen_2(func, state, t_step, t_0, alpha=.5)

print(y_np1)

y_n = 1

def func2(t_n, y_n):
    y_dot = np.tan(y_n)+1
    
    return y_dot
    
y_np1_2 = so.gen_2(func2, y_n, .025, 1, alpha=.5)

print(y_np1_2)

y_np1_3 = so.gen_2_mul(func2, y_n, .025, [1, 1.1], alpha=float(2/3))
print(y_np1_3)