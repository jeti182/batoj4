from numpy import linspace
import tensorflow as tf
from matplotlib.pylab import plt

from  batoj4 import LogisticPSSDLModel, AQGPModel

sess = tf.Session()

with sess:

	fine_grained_soas =  linspace(-100,100,1000) 
	coarse_soas =  linspace(-100,100,21)
	repetitions = 32 

	pss = 30
	dl = 10

	model = LogisticPSSDLModel()


	y =  model.psychometric_function(fine_grained_soas, (pss, dl)).eval() * repetitions
	y_simulated =  model.simulate(coarse_soas, repetitions, (pss, dl)) 


	plt.plot(fine_grained_soas,y, "b-")
	plt.plot(coarse_soas,y_simulated.Probe_first_count, "bx")
	

	lam_p = 0.02
	lam_r = 0.02
	tau = 2.0
	delta = 5.0
	xi = 0.5
	e_p = 0.01
	e_r = 0.02
	
	
	
	model = AQGPModel()

	parameters = (lam_p, lam_r, tau, delta, xi, e_p, e_r)
	y =  model.psychometric_function(fine_grained_soas, parameters).eval() * repetitions
	y_simulated =  model.simulate(coarse_soas, repetitions, parameters) 


	plt.plot(fine_grained_soas,y, "b-")
	plt.plot(coarse_soas,y_simulated.Probe_first_count, "bx")
	
	plt.show()
