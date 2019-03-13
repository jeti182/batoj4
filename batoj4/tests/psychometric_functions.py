import tensorflow as tf


def logistic_pss_dl(soas,pss,dl):
 """Logistic psychometric function. Parametrized to directly take
the PSS and DL as arguments. 

:param soas: Stimulus Onset Asynchronies
:type soas: List-like object with float-like numbers of the SOAs in ms.

:return: List with the probability of judging `probe first` at each SOA
:rtype: Tensor
"""
 return (1.0-(1.0/(1.0+tf.exp(-(1.0/dl*(soas-pss))))))
