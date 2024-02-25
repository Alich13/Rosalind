import os
import glob
from turtle import pos
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import argparse


possibleRestrictionLen=[4,6,8,10,12]



def oneBased(baseId):
    return baseId+1

if __name__ == "__main__":
    file_path="/Users/achemkhi/Library/CloudStorage/OneDrive-Illumina,Inc/Desktop/rosalind/input_data.txt"
    
    with open(file_path, 'r') as fasta_file :
        RecordsRead=0
        for record in SeqIO.parse(fasta_file, 'fasta'):
            RecordsRead=RecordsRead+1
            
            mySequence=record.seq
            reverseSequence=record.reverse_complement().seq

            res=[]
            for i in range(0,len(mySequence)):
                for len in possibleRestrictionLen : 

                    if mySequence[i:i+int(len/2)]== (mySequence[i+int(len/2):i+len]).reverse_complement():
                        res.append((oneBased(i),len))

        for x,y in res:
            print(f"{x} {y}")

    assert RecordsRead==1
                