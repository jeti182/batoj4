from .toj_model import TOJModel
import tensorflow as tf
import numpy

class TVAModel(TOJModel):
	""" TODO """
	
	def psychometric_function(self, soas, parameters):
		v_p = parameters['v_p']
		v_r = parameters['v_r']
		# At negative SOAs: p encoded before r starts ...
		p_neg = (1.0 - tf.exp(-v_p * (-soas))) \
			+  tf.exp(-v_p * (-soas)) * (v_p / (v_p + v_r)) 	# if not, 
														# both race and p wins according to Luce's choice axiom.
		# At positive SOAs: If not r finishes before p is shown ...
		p_pos = tf.exp(-v_r * soas) \
			* (v_p / (v_p + v_r)) # p wins racing r according to L's choice axiom
			
		p = (soas < 0) * p_neg + (soas >= 0) * p_pos	
		return p
