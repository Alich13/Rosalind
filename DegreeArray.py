import os
import glob
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import argparse


if __name__ == "__main__":
    with open("/Users/achemkhi/Library/CloudStorage/OneDrive-Illumina,Inc/Desktop/rosalind/input_data.txt","r") as inputFile: 
        count_dict={}
        for line in inputFile.readlines():
            edge= tuple([int(x) for x in line.split(" ")])
            
            if edge[0] in count_dict.keys():
                count_dict[edge[0]]+=1
            else : 
                count_dict[edge[0]]=1

            if edge[1] in count_dict.keys():
                count_dict[edge[1]]+=1
            else : 
                count_dict[edge[1]]=1
    sorted_dict = dict(sorted(count_dict.items()))
    output=""
    for k,v in sorted_dict.items():
        output+=f"{v} "
    print(output)
    print(sorted_dict)


                
