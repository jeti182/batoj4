from .toj_model import TOJModel, ParameterDescription
import tensorflow as tf
import numpy

class LogisticPSSDLModel(TOJModel):
	
	def psychometric_function(self, soas, parameters):
		""" Function of judging `probe first` over the SOAs """
		(pss, dl) = (parameters['PSS'], parameters['DL'])
		return (1.0-(1.0/(1.0+tf.exp(-(1.0/dl*(soas-pss))))))

