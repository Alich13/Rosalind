
from calendar import c
from curses import keyname
import os
import glob
from re import A
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import argparse



if __name__ == "__main__":


    PiPath="BABAABABABBBBBBABBBBBBABBABABBAAAAAABBABABBAABABBA"

    ProbMatrix={ 
        "AA":0.326,
        "AB":0.674,
        "BA":0.441,
        "BB":0.559,
    }

    assert len(PiPath)>1

    prob=0.5 # init prob of either getting A or B 
    print("init prob ",prob)
    for i in range(0,len(PiPath)-1):
        try : 
            transition=ProbMatrix[PiPath[i:i+2]]
        except:
            raise KeyError("")
            
        #print(PiPath[i:i+2] ,"--",transition )
        prob=prob*(transition)

    print(prob)
  

    

