# this is the basic forward euler solver

# numpy for mathematical operations and working with states
import numpy as np

# https://en.wikipedia.org/wiki/List_of_Runge%E2%80%93Kutta_methods


def fw_eul(func, y_n, t_step, t_n):
    # this is a single step forward euler for a single function
	# func is the function that is passed that acts on the state to produce
    # the state derivatives
    # y_n are the relevant variables that change in time at the initial point
	# h is the time step (recommended lower than 10e-2)
	
    # perform the step 
    y_np1 = y_n + t_step*func(t_n, y_n)
	
    # return the next step
    return y_np1
    

def fw_eul_mul(func, y_n, t_step, t_span):
    # this is a multi step forward euler for a single function
    # the only difference is that t_span is a list in the form [t0, tf]
    
    # generate some set of time the function acts over
    t_set = np.linspace(t_span[0], t_span[1], (t_span[1]-t_span[0])/t_step)
    
    # run through the time set until finished
    for t in t_set:
        y_n = fw_eul(func, y_n, t_step, t)
    
    # return the new output
    return y_n 
    