import tensorflow as tf

def binomial(repetitions,success_probabilities):
	""" Required until TensorFlow devs solve 
	https://github.com/tensorflow/probability/issues/81"""
	from numpy.random import binomial 
	if type(repetitions) == tf.Tensor:
		repetitions = repetitions.eval(session=tf.Session())
	if type(success_probabilities) == tf.Tensor:
		success_probabilities = success_probabilities.eval(session=tf.Session())
	return binomial(repetitions, success_probabilities)
