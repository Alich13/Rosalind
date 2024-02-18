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
            if str(record.seq).startswith("NNNN") or str(record.seq).endswith("N") :
                sequences.append(record)
    return sequences



sequences=read_fasta("/illumina-isi07/scratch/dragen_team_share5/users/grizk/HT_test/2024_hg38_HapDB_candidate/phased_alts.fasta")
print("length", len(sequences))

# for seq in sequences :
#     print (str(seq.seq))

if __name__ == "__main__":
    print("running ...")
