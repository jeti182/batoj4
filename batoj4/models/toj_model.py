import abc
from .workarounds import binomial  
import pandas as pd
import os, sys, ntpath
import yaml



class ParameterDescription():
	""" Struct for parameter descriptions """
	def __init__(self, symbol="x", full_name="unnamed",
				meaning="This parameter has no meaning defined "):
		self.symbol = symbol
		self.symbol_math_font = symbol
		self.full_name = full_name
		self.meaning = meaning
		
		

class TOJModel(abc.ABC):
	""" This is the base class for TOJ models """
	
	def __init__(self):
		self.model_name = print(self.__class__.__name__)
		self.models_dir = os.path.dirname(os.path.realpath(__file__))
		self.model_file = ntpath.basename(sys.modules[self.__module__].__file__) 
		self.model_file_name = self.model_file.split(".")[0]
		self.model_description_file = \
			os.path.join(self.models_dir, self.model_file_name) + ".yaml"
	
		print("Loading infos for " + self.model_file_name)
		try:
			with open(self.model_description_file, 'r') as stream:
				try:
					print(yaml.load(stream))
				except yaml.YAMLError as exc:
					print(exc)
		except:
			print("Error reading " + self.model_description_file) 
			print("Please provide this file with info about the model.")
			print("It must be in the same directory as the Python class.")
	
	
	@abc.abstractmethod
	def psychometric_function(self, soas, parameters):
		""" Function of judging `probe first` over the SOAs """
		return
		
	def simulate(self, soas, repetitions, parameters, 
				prameter_distributions = None, number_of_subjects = 1):
		""" A default simulation is implemented, which uses the model's
		psychometric function to simulate binomially distributed data 
		ponits. However, model developers are encouraged to reimplement
		the stimulation (by overriding this function) in a more
		instructive generative, mechanistic form, if their model allows
		this. """
		list_of_tojs = []
		for i in range(number_of_subjects):
			individual_tojs = pd.DataFrame()
			thetas = self.psychometric_function(soas, parameters)
			individual_tojs['Subject'] = [i+1]*len(soas)
			individual_tojs['Codition'] = [1]*len(soas)
			individual_tojs['SOA'] = soas  
			individual_tojs['Repetitions'] = repetitions  
			individual_tojs['Probe_first_count'] = binomial(repetitions, thetas)
			list_of_tojs.append(individual_tojs)
			tojs = pd.concat(list_of_tojs) 
		return tojs
        
	def summary(self):
		""" Provide a summary description of this model, possibly using
		the information properties """
		pd = self.parameters_descriptions
		summary = self.model_description + "\n Parameters: \n" 
		for i in range(len(pd)):
			summary +=  "*" + (pd[i].symbol + " (" + pd[i].full_name + "): " + 
					 pd[i].meaning + "\n") 
		return(summary)
		
##	@property
#	@abc.abstractmethod
#	def model_description(self):
#		""" Profide a brief description """
#		pass

#	@property
#	@abc.abstractmethod
#	def parameters_descriptions(self):
#		""" Provide list of parameter descriptions """
#		pass	
	
#	@property
#	@abc.abstractmethod
#	def used_by(self):
#		""" Provide list of references """
#		pass
		

		

		
