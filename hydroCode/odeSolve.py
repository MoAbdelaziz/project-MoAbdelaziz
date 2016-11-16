import numpy as np

def eulerOriginal(f, ics, tMin, tMax, numSteps):
	# Compute forward Euler for arbitrarily-sized system of first order ODEs 
	# f        : function written as f(r,t), for a vector r of variables, and time.
	# ics      : Vector of n initial conditions, nth entry for nth variable (t0 goes in tMin)
	# tMin     : Start time
	# tMax     : Max time (independent variable) to run to
	# numSteps : Number of steps to perform in total
	print("Starting Euler...")
	tMin = float(tMin)
	tMax = float(tMax)
	h = (tMax-tMin)/numSteps
	
	tPoints = np.arange(tMin,tMax,h)
	rPoints = np.zeros([len(ics),1])
	
	r = ics
	r.shape = (len(ics),1) # Force r to be a column vector
	for t in tPoints:
		rPoints = np.append(rPoints, r, axis = 1)
		r = r + h * f(r,t)
	print("...finished Euler")
	rPoints = np.append(rPoints, r, axis = 1)
	return tPoints,rPoints[:,:]
	
