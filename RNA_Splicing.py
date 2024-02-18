import os
import glob
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import pysam
import argparse


def getArgs():
  """Return the parsed arguments."""
  parser = argparse.ArgumentParser( description="" )
  parser.add_argument( "-i"   ,  "--input"             ,  help="Input File"                                                          ,  default="/dev/stdin")
  args = parser.parse_args()
  return args


def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as fasta_file:
        for record in SeqIO.parse(fasta_file, 'fasta'):
            print(record.seq.translate(to_stop=True))
    return sequences



if __name__ == "__main__":
    file_path="/home/achemkhi/Projects/test_ggp/rosalind/input_data.txt"
    
    with open(file_path, 'r') as fasta_file :
        readFirstRecord=False
        for record in SeqIO.parse(fasta_file, 'fasta'):
            if not(readFirstRecord):
                firstSeq=record
                readFirstRecord=True
                continue

            if (readFirstRecord) and (firstSeq.seq.find(record.seq)>-1):
                firstSeq.seq=firstSeq.seq.replace(str(record.seq),"")
                
    
    print(firstSeq.seq.translate(to_stop=True))
                
        
        #print(firstSeq.next())

