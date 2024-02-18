import os
import glob
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import pysam
import argparse


def printPermut(res:str,possibleNumbers:list,n:int):
    if len(res)==n:
        print(" ".join(res))

    for i in possibleNumbers:
        if (len(res)<n) and (i not in res ):
            new_res=res.copy()
            new_res.append(i)
            printPermut(new_res,possibleNumbers,n)


if __name__ == "__main__":
    
    n=5
    nbPermutation=math.factorial(n)
    print(nbPermutation)
    possibleNumbers=list(range(1,n+1))
    possibleNumbers.sort()
    possibleNumbers=[str(x) for x in possibleNumbers ]
    printPermut([],possibleNumbers,n)
    
    
    

