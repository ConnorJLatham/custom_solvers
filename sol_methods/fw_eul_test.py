# this is to test the fw euler script
import fw_eul as fe
import time
import numpy as np

input = np.array([1, 2, 3, 4, 5])
t_step = .1

# def derivative(t_n, y_n):
    # y_dot = np.zeros(len(y_n))
    
    # y_dot[0] = t_n
    # y_dot[1] = 2*y_n[2]
    # y_dot[2] = .5*y_n[1]
    # y_dot[3] = y_n[4]**2
    # y_dot[4] = .1
    
    # return y_dot
def func(t_n, y_n):
    y_dot = t_step*y_n
    return y_dot
    
t_0 = 0

output = fe.fw_eul(func, input, t_step, t_0)
print(output)

def func2(t_n, y_n):
    y_dot = np.tan(y_n) + 1
    return y_dot

tic = time.time()
output_2 = fe.fw_eul_mul(func2, 1, .025, [1, 1.1])
toc = time.time()
print('Output of solver: ', output_2)
print('Time to run: ', toc-tic, ' seconds')