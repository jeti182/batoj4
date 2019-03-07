from toj_model import TOJModel, ParameterDescription


class LogisticPSSDLModel(TOJModel):
	
	parameters_descriptions = [ 
			ParameterDescription("PSS", "Point of Subjective Simultaneity",
			"the point where probe-first function corsses the .5 level"),
			ParameterDescription("DL", "Difference",
			"TODO")]
	
	used_by = ["TODO", "TODO"]

	def psychometric_function(self, soas, parameters):
		""" Function of judging `probe first` over the SOAs """
		(pss, dl) = parameters
		return (1.0-(1.0/(1.0+tf.exp(-(1.0/dl*(soas-pss))))))

	def summary(self): # TODO: This impl. can go into super class.
		""" Provide a summary description of this model, possibly using
		the information properties """
		pd = self.parameters_descriptions
		return(" A traditional psychometric model with parameters " +
			   pd[0].symbol + " (" + pd[0].full_name + ") " + "which is " +
			   pd[0].meaning +
		" and " +
			   pd[1].symbol + " (" + pd[1].full_name + ") " + 'which is ' +
			   pd[1].meaning)

	def simulate(self, parameters):
		print("Not implemented yet!")	


if __name__ == '__main__':
	model = LogisticPSSDLModel()
	print(model.summary())
