import order_4 as o4
import numpy as np
import time

y_0 = np.array([1, 2, 3, 4, 5])
t_step = .1
t_0 = 1

def y_dot(t_n, y_n):
	y_dot = .01*y_n
	return y_dot
    
y_np1_stp = o4.rk4_stp(y_dot, y_0, t_step, t_0)
print(y_np1_stp)

y_np1_mul = o4.rk4_mul(y_dot, y_0, t_step, [0, 10])
print(y_np1_mul)