import os
import glob
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import pysam
import argparse

def concatAllPosibilities(mainString,possibilties,n):
    if len(mainString)==n:
        print(mainString)
    
    for i in  possibilties:
        if len(mainString) < n :
            concatAllPosibilities(mainString+i,possibilties,n)



if __name__ == "__main__":
    alphabet="A B C D E F G H I"
    n=3

    alphabetList=alphabet.split(" ")
    alphabetList.sort()
    print(alphabetList)
    
    res=""
    concatAllPosibilities(res,alphabetList,n)


