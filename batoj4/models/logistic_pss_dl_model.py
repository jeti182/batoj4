from .toj_model import TOJModel, ParameterDescription
import tensorflow as tf
import numpy

class LogisticPSSDLModel(TOJModel):
	

	parameters_descriptions = [ 
			ParameterDescription("PSS", "Point of Subjective Simultaneity",
			"The point where probe-first function corsses the .5 level"),
			ParameterDescription("DL", "Difference Limen",
			"TODO")]
	
	used_by = ["TODO", "TODO"]

	def psychometric_function(self, soas, parameters):
		""" Function of judging `probe first` over the SOAs """
		(pss, dl) = parameters
		return (1.0-(1.0/(1.0+tf.exp(-(1.0/dl*(soas-pss))))))

if __name__ == '__main__':
	model = LogisticPSSDLModel()
	print(model.summary())
	soas = numpy.linspace(-100.0,100.0,21)
	repetitions = [32] * 21
	pse = 10
	dl = 30
	print("Simulating myself for SOAs = " + str(soas) +
			" and Repetitions = " + str(repetitions) + 
			" with paramters PSE = " + str(pse) +
			" and DL = " + str(dl))
	tojs = model.simulate(soas, repetitions, (pse, dl))	
	print(tojs)
	
