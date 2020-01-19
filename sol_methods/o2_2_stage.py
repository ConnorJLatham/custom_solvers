# this is the second order two stage method
# it is your choice as to what the parameter alpha is
# refer to https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods

# numpy for mathematical operations and working with states
import numpy as np

def gen_2(func, y_n, t_step, t_n, alpha = .5):
    # this is a single step generalized 2 stage, 2nd order solver
    # automatically set to the midpoint method, adjust alpha for more
    
    # rename some stuff
    a = alpha
    h = t_step
    
    # determine the stage components
    k1 = func(t_n, y_n)
    k2 = func(t_n + a*h, y_n + a*h*k1)
    
    # perform the step 
    y_np1 = y_n + h*((1-(1/(2*a)))*k1 + (1/(2*a))*k2)
    
    # return the next step 
    return y_np1
    
def gen_2_mul(func, y_n, t_step, t_span, alpha = .5):
    # this is a multi step generalized 2 stage, 2nd order solver
    # automatically set to midpoint method, adjust alpha for more
    
    # rename things
    a = alpha
    h = t_step
    
    # create a set of the times
    t_set = np.linspace(t_span[0], t_span[1], (t_span[1]-t_span[0])/t_step)
    
    # iterate through the time set
    for t in t_set:
        y_n = gen_2(func, y_n, t_step, t, alpha)
        
    # return the new state
    return y_n