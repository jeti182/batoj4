from numpy import linspace
import tensorflow as tf
from matplotlib.pylab import plt

from  batoj4 import LogisticPSSDLModel, GaussMuSigmaModel, AQGPModel

sess = tf.Session()

with sess:

	def plot_curve_and_simulation(model, parameters):
		fine_grained_soas =  linspace(-100,100,1000) 
		coarse_soas =  linspace(-100,100,21)
		repetitions = 32 
		y =  model.psychometric_function(fine_grained_soas, parameters).eval() * repetitions
		y_simulated =  model.simulate(coarse_soas, repetitions, parameters) 
		plt.plot(fine_grained_soas,y, "b-")
		plt.plot(coarse_soas,y_simulated.Probe_first_count, "bx")	



	
	# Test the logistic model
	model = LogisticPSSDLModel()
	parameters = {'PSS' : 30, 'DL' : 10}
	plot_curve_and_simulation(model, parameters)
	
	# Test the normalcdf model
	model = GaussMuSigmaModel()
	parameters = {'Mu' : 30, 'Sigma' : 5}
	plot_curve_and_simulation(model, parameters)

	# Test AQ & GP's model
	model = AQGPModel()
	parameters = {	'lam_p' : 0.02, 'lam_r' : 0.02,
					'tau' : 2.0, 'delta' : 5.0,	'xi' : 0.5,
					'e_p' : 0.01, 'e_r' : 0.02}
	plot_curve_and_simulation(model, parameters)
	
	
	plt.show()
