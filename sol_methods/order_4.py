# this is the fourth order section
# refer to: 
# http://mathworld.wolfram.com/Runge-KuttaMethod.html
# https://www.uni-muenster.de/imperia/md/content/physik_tp/lectures/ss2016/num_methods_ii/rkm.pdf

# numpy for mathematical operations and working with states
import numpy as np

def rk4_stp(func, y_n, t_step, t_n):
	# this is the single step rk4 method 
	
	# rename some stuff
	h = t_step
	a21 = .5
	a32 = .5
	a43 = 1.0
	b1 = float(1/6)
	b2 = float(1/3)
	b3 = float(1/3)
	b4 = float(1/6)
	c2 = .5
	c3 = .5
	c4 = 1
	
	# determine the stage components
	k1 = func(t_n, y_n)
	k2 = func(t_n + c2*h, y_n + h*(a21*k1))
	k3 = func(t_n + c3*h, y_n + h*(a32*k2))
	k4 = func(t_n + c4*h, y_n + h*(a43*k3))
	
	# perform the step 
	y_np1 = y_n + h*(b1*k1 + b2*k2 + b3*k3 + b4*k4)
	
	# return the next step 
	return y_np1
	
def rk4_mul(func, y_n, t_step, t_span, record = True):
	# this is a multi step rk4 method
	
	# rename things
	h = t_step
	y_i = y_n
	
	# create a set of the times
	t_set = np.linspace(t_span[0], t_span[1], (t_span[1]-t_span[0])/t_step)
	y_out = np.reshape(y_n, (6,1)) # maybe make this zeroes? then cut it off later
    # just need to make sure everything lines up, and right now I think it 
    # is one time step off hmmm
	
	# iterate through the time set
	for t in t_set:
		y_i = rk4_stp(func, y_i, t_step, t)
		y_j = np.reshape(y_i, (6,1))
		y_out = np.append(y_out, y_j, axis=1)

	# return the new state
	# if (~record):
		# y_out = y_i
	return y_out