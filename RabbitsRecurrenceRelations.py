import os
import glob
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
#import pysam
import argparse

#  Fibonacci sequence :Fn=Fn-1 + Fn-2 with F1 and F2 = 1 

def Fn(n,k,f0):
  
  if (n == 1) or (n == 2): 
    return f0

  if n >  2 : 
    return Fn(n-1,k,f0) + k*Fn(n-2,k,f0)

  assert n > 0
  

if __name__ == "__main__":
  
  print("running ...")
  print(Fn(32,5,1))



