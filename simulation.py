import tensorflow as tf
from psychometric_functions import logistic_pss_dl
from tensorflow_probability import distributions as dist
from inspect import signature

def workaround_binomial_sample(repetitions,success_probabilities):
	""" Required until TensorFlow devs solve 
	https://github.com/tensorflow/probability/issues/81"""
	from numpy.random import binomial 
	with tf.Session() as sess:
		reps = repetitions.eval(session=sess)
		prob = success_probabilities.eval(session=sess)
		samples = []
		for i in range(len(reps)):
			samples.append(binomial(reps[i], prob[i]))
		return samples


def simulate_tojs(soas=tf.linspace(-100.0,100.0,11),
				repetitions=tf.convert_to_tensor([20.0]*11),
				psychometric_function = logistic_pss_dl,
				parameters=(0.0,10.0)): 
					
	assert len(signature(psychometric_function).parameters)-1 == len(parameters), \
		"Number of distributions in parameters must match requried parameters (-1) of the psychometric function."
	assert soas.shape == repetitions.shape, \
		"The list of repetitions must have the same lenght as the list of SOAs"

	return workaround_binomial_sample(repetitions, psychometric_function(soas,*parameters))


def simulate_group_tojs(soas=tf.linspace(-100.0,100.0,11),
				repetitions=tf.convert_to_tensor([20.0]*11),
				psychometric_function = logistic_pss_dl,
				parameters=(dist.Normal(0.0,3.0),
				dist.Normal(10.0,3.0)),
				group_size=40):
					
	parameter_samples = []
	for parameter in parameters:
		parameter_samples.append(parameter.sample())
	tojs = []	
	for i in range(group_size):
		tojs.append(simulate_tojs(soas,repetitions,psychometric_function, parameter_samples))
	
	return tojs
