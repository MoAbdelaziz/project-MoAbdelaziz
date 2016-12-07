import numpy as np
import scipy.special as ss
import pylab as plt
## Contains several functions for setting the initial conditions of U,F in 2D hydrocode
def energyFunc(p,gamma,rho,v):
	# Calculate energy in terms of p, gamma, rho, v
	return p/(gamma-1) + 0.5* rho*v**2
	
	
def sod1D(U,F,gamma, rhoL,pL,vL, rhoR,pR,vR):
	Nx = len(U[0,:,0,0])
	## Left state
	U[:,0:Nx/2,0,0] = rhoL
	U[:,0:Nx/2,0,1] = rhoL*vL
	U[:,0:Nx/2,0,2] = energyFunc(pL,gamma,rhoL,vL)

	F[:,0:Nx/2,0,0] = rhoL*vL
	F[:,0:Nx/2,0,1] = rhoL*vL**2 + pL
	F[:,0:Nx/2,0,2] = (energyFunc(pL,gamma,rhoL,vL) + pL)*vL

	## Right State
	U[:,Nx/2:,0,0] = rhoR
	U[:,Nx/2:,0,1] = rhoR*vR
	U[:,Nx/2:,0,2] = energyFunc(pR,gamma,rhoR,vR)

	F[:,Nx/2:,0,0] = rhoR*vR
	F[:,Nx/2:,0,1] = rhoR*vR**2 + pR
	F[:,Nx/2:,0,2] = (energyFunc(pR,gamma,rhoR,vR) + pR)*vR
	return U , F
	
def bessel(U,F,xPoints,gamma,rho,p,v):
	pBound = np.abs(ss.j0(10*xPoints))# Pressure at a boundary due to Bessel beam
	
	# Uniform fluid throughout
	U[:,:,0,0] = rho
	U[:,:,0,1] = rho*v
	U[:,:,0,2] = energyFunc(p,gamma,rho,v)
	F[:,:,0,0] = rho*v
	F[:,:,0,1] = rho*v**2 + p
	F[:,:,0,2] = (energyFunc(p,gamma,rho,v) + p)*v
	
	# Change one boundary to have pressure pBound
	U[0,:,0,2] = energyFunc(pBound,gamma,rho,v)
	F[0,:,0,1] = rho*v**2 + pBound
	F[0,:,0,2] = (energyFunc(pBound,gamma,rho,v) + pBound)*v
	U[1,:,0,2] = energyFunc(pBound,gamma,rho,v)
	F[1,:,0,1] = rho*v**2 + pBound
	F[1,:,0,2] = (energyFunc(pBound,gamma,rho,v) + pBound)*v
	
	plt.plot(U[0,:,0,2])
	plt.show()
	return U, F
