from .toj_model import TOJModel, ParameterDescription
import tensorflow as tf
import numpy

class AQGPModel(TOJModel):
	""" Implementation of Alcalá-Quintana & García-Pérez (2013) model,
		relatively close to the MATLAB & R routines in their 
		supplementary material. """
	
	def psychometric_function(self, soas, parameters):
		(lam_p, lam_r, tau, delta, xi, e_p, e_r) = parameters
		def difcdf(soas, shift, lam1, lam2):
			y = soas - shift
			left = lam1*tf.exp(lam2*y)/(lam1+lam2)    ## min ( ...,1) 
			right =1-(lam1*tf.exp(-lam1*y))/(lam1+lam2) ## max ...,0)
			return (y<=0) * left + (y>0)*right
		pPF = difcdf(-delta, soas+tau, lam_p, lam_r)
		pRF = 1 - difcdf(delta, soas+tau, lam_p, lam_r)
		pS = 1 - pPF - pRF
		p = (1-e_p)*pPF + (1-xi)*pS + e_r*pRF
		return p
		


