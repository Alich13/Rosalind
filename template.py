from calendar import c
import os
import glob
from re import A
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
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
            if str(record.seq).startswith("NNNN") or str(record.seq).endswith("N") :
                sequences.append(record)
    return sequences



if __name__ == "__main__":

  # with open("/Users/achemkhi/Library/CloudStorage/OneDrive-Illumina,Inc/Desktop/rosalind/input_data.txt","r") as inputFile :
  #   lineNb=0
  #   for line in inputFile.readlines():
  #     lineNb=lineNb+1
  #     if lineNb%2==0 :
  #       print(line.strip("\n"))

  myString="When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
  myStringList=myString.split(" ")
  d={}
  for i in myStringList:
    if i in d.keys():
      d[i]+=1
    else:
      d[i]=1
  
  for k,v in d.items():
    print(k,v)
  

    

