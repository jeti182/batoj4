import abc


class ParameterDescription:
	""" Struct for parameter descriptions """
	def __init__(self, symbol="x", full_name="unnamed",
					meaning="This parameter has no meaning defined "):
		self.symbol = symbol
		self.symbol_math_font = symbol
		self.full_name = full_name
		self.meaning = meaning


class TOJModel(abc.ABC):
	""" This is the base class for TOJ models """
	@abc.abstractmethod
	def psychometric_function(self, soas, parameters):
		""" Function of judging `probe first` over the SOAs """
		return
		
	@abc.abstractmethod
	def simulate(self, parameters):
		""" Implement a (if possible generative) simulation """
		return

	@abc.abstractmethod
	def summary(self):
		""" Provide a summary description of this model, possibly using
		the information properties """
		return	

	@property
	@abc.abstractmethod
	def parameters_descriptions(self):
		""" Provide list of parameter descriptions """
		pass	
	
	@property
	@abc.abstractmethod
	def used_by(self):
		""" Provide list of references """
		pass
