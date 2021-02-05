import os
import json
import numpy as np
from tqdm import tqdm
from slf import SLF

from s3netcdf import NetCDF2D 
from datetime import datetime
import re

class S3NetCDFSLF(NetCDF2D):
  """
  
  """
 
  @staticmethod
  def getTranspose(slf,output):
    if not os.path.exists(output):
      slf = SLF(slf)
      nnode = slf.NPOIN2
      ntime = slf.NFRAME
      nvar = slf.NVAR
      fp = np.memmap(output, dtype='float32', mode='w+', shape=(nnode, nvar, ntime))
      
      for frame in range(slf.NFRAME):
        print("{} of{}".format(frame, slf.NFRAME))
        fp[:, :, frame] = slf.getVALUES(frame).T
      
  def __init__(self,obj):
    super().__init__(obj)
    info    = self.info()
    self.variables = obj["nca"]['groups']['s']['variables']

  
  def uploadSpatial(self,slf):
    variables=self.variables
    slf = SLF(slf)
    for frame in range(slf.NFRAME):
      for v in ['fs','u','v']:
        self['s',v,frame]=slf.getVarsIndexes([variables[v]['slf name']])  

  def uploadTemparol(self,slf,npy):
    slf = SLF(npy)
    gnode=1000
    nnode = slf.NPOIN2
    ntime = slf.NFRAME
    nvar = slf.NVAR
    fp = np.memmap(npy, dtype='float32', mode='r', shape=(nnode,nvar,ntime))
    # Save array in memory to S3
    for i in np.arange(0,nnode,gnode):
      _slice=slice(i,np.minimum(nnode,i+gnode))
      for i,v in enumerate(['fs','u','v']):
        self['t',v,_slice]=fp[_slice,i]