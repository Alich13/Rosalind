import os
import glob
import pandas as pd
#import pysam
import math
import numpy as np
import datetime
from Bio import SeqIO
import argparse


# based on probabilities tree 
# A/A homozygous dominant
# A/a heterozygous
# a/a homozygous recessive
# D = event : final genotype contains A
# P(D) = 
#   P(A/A) +
#   P(A/a and A/A) + P(A/a and A/a) * 3/4 + P(A/a and a/a) * 1/2 + 
#   P(a/a and A/A) + P(a/a and A/a) * 1/2   


if __name__ == "__main__":
    print ("runing ... ")
    k=28
    m=18
    n=26
    S=k+m+n

    P_D= (k/S) + (m/S * k/(S-1)) + ( m/S * (m-1)/(S-1) * 3/4 ) + (m/S * n/(S-1) * 1/2 )    + (n/S * k/(S-1)) + ( n/S * m/(S-1) * 1/2 )

    print(P_D)
    

