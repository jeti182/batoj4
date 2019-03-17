from .toj_model import TOJModel, ParameterDescription
import tensorflow as tf
import numpy

class GaussMuSigmaModel(TOJModel):

	def psychometric_function(self, soas, parameters):
		""" Function of judging `probe first` over the SOAs """
		mu = parameters['Mu']
		sigma = parameters['Sigma']
		normcdf = (0.5*(1+tf.erf((soas-mu)/(sigma*tf.sqrt(2.0)))))
		return (1.0 - normcdf)


