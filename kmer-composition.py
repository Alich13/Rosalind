import os
import glob
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import pysam
import argparse





def concatAllPosibilities(mainString,kmerdict,possibilties,n):
    if len(mainString)==n:
        kmerdict[mainString]=0

    for i in  possibilties:
        if len(mainString) < n :
            concatAllPosibilities(mainString+i,kmerdict,possibilties,n)


def gen_kmer_dict(n:int)->dict: 
    alphabet="A T G C"
    alphabetList=alphabet.split(" ")
    alphabetList.sort()
    kmerdict={} # all possible kmers , will be passed by reference (not copied)
    concatAllPosibilities("",kmerdict,alphabetList,n)

    return kmerdict.copy()


if __name__ == "__main__":

    print("running ...")
    k=4
    kmer_dict=gen_kmer_dict(k)


    with open("/home/achemkhi/Projects/test_ggp/rosalind/input_data.txt", 'r') as fasta_file:
        seq_count=0

        for record in SeqIO.parse(fasta_file, 'fasta'):
          seq_count+=1
        
          for k_pos in range(0,len(record.seq)):
            if ( (k_pos+k) <= len(record.seq)):
              kmer=record.seq[k_pos:k_pos+k]
              assert kmer in kmer_dict.keys()
              kmer_dict[kmer]+=1


        sorted_kmer_dict = dict(sorted(kmer_dict.items()))
        kmer_list=[str(x) for x in sorted_kmer_dict.values()]
        print(" ".join(kmer_list))
        assert seq_count==1

