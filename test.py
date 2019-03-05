import tensorflow as tf
from matplotlib.pylab import plt
from psychometric_functions import logistic_pss_dl

soas = tf.linspace(-100.0, 100.0, 21, name="SOAs") 

sess = tf.Session() 

with sess.as_default(): 
	y = logistic_pss_dl(soas,30,10)
   
	plt.plot(soas.eval(),y.eval())
	plt.show()
