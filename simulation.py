import tensorflow as tf
from psychometric_functions import logistic_pss_dl
from tensorflow_probability import distributions as dist
from inspect import signature

def simulate_toj(soas=tf.linspace(-100.0,100.0,11), psychometric_function = logistic_pss_dl, parameters=(dist.Normal(0.0,3.0), dist.Normal(10.0,3.0))):
	assert len(signature(psychometric_function).parameters)-1 == len(parameters), "Number of distributions in parameters must match requried parameters (-1) of the psychometric function."
	parameter_samples = []
	for parameter in parameters:
		parameter_samples.append(parameter.sample())
	return psychometric_function(soas,*parameter_samples)
