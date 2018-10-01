# An example as to what to avoid, taken from CPNest
# In here, there are 2 instead of 4 white spaces indentations
# Some empty lines between methods are missing
# Some white spaces between lines are missing

from abc import ABCMeta,abstractmethod,abstractproperty
from numpy import inf
from .parameter import LivePoint
from numpy.random import uniform

class Model(object):
  """
  Base class for user's model. User should subclass this
  and implement log_likelihood, names and bounds
  """
  __metaclass__ = ABCMeta
  names=[] # Names of parameters, e.g. ['p1','p2']
  bounds=[] # Bounds of prior as list of tuples, e.g. [(min1,max1), (min2,max2), ...]
  def in_bounds(self,param):
    """
    Checks whether param lies within the bounds
    """
    return all(self.bounds[i][0] < param.values[i] < self.bounds[i][1] for i in range(param.dimension))
  
  def new_point(self):
    """
    Create a new LivePoint, drawn from within bounds
    """
    logP=-inf
    while(logP==-inf):
      p = LivePoint(self.names,[uniform(self.bounds[i][0],self.bounds[i][1]) for i,_ in enumerate(self.names)] )
      logP=self.log_prior(p)
    return p
  
  @abstractmethod
  def log_likelihood(self,param):
    """
    returns log likelihood of given parameter
    """
    pass
  def log_prior(self,param):
    """
    Returns log of prior.
    Default is flat prior within bounds
    """
    if self.in_bounds(param):
      return 0.0
    else: return -inf
    
  def strsample(self,sample):
    """
    Return a string representation for the sample to be written
    to the output file. User may overload for additional output
    """
    line='\t'.join('{0:.20e}'.format(sample[n]) for n in sample.names)
    line+='{0:20e}'.format(sample.logL)
    return line
  def header(self):
    """
    Return a string with the output file header
    """
    return '\t'.join(self.names) + '\tlogL'


# MIT License
#
# Copyright (c) 2015-2016 Walter Del Pozzo, John Veitch
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#