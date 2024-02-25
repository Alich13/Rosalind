
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

    X="xyzxzxyyzyyzyzzzzxzzxxzxzyzyzzzyzxyxxyxzxyzzzyyyyz"
    PiPath="AABBBBBBBBAABBAABAABBBABABABBABAAABABABAABAABAAABA"

    ProbMatrix={ 
        "Ax":0.034, # prob of x given A
        "Ay":0.348,
        "Az":0.618,
        "Bx":0.204,     
        "By":0.336,
        "Bz":0.46,
        
    }



    assert len(PiPath)>1 and len(X) >1 and   len(X)==len(PiPath)

    prob=(1) # init prob of either getting A or B 
    print("init prob ",prob)
    for i in range(0,len(PiPath)):
        try :
            print (f"{PiPath[i]}{X[i]}")
            emissonProb=ProbMatrix[f"{PiPath[i]}{X[i]}"]
           
        except:
            raise KeyError("error")
            
        #print(PiPath[i:i+2] ,"--",transition )
        prob=prob*(emissonProb)

    print(prob)
  

    

