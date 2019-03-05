import tensorflow as tf


def logistic_pss_dl(soas,pss,dl):
 return (1.0-(1.0/(1.0+tf.exp(-(1.0/dl*(soas-pss))))))
