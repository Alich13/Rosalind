import os
import glob
from turtle import pos
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import argparse


codonsStop=["TAA","TAG","TGA"]


def get_orf(Sequence):

    orf_candidates={}

    for i in range(0,len(Sequence)):

        if Sequence[i]=="A" and Sequence[i:i+3]=="ATG" :
            orf_candidates[i]=""
    
        
        if  (Sequence[i:i+3] in codonsStop) : 
            for orfPos,orfseq in orf_candidates.items():
                if (orfseq=="") and (i >= (orfPos+3)) and ((i-orfPos)%3==0):
                    orf_candidates[orfPos]=Sequence[orfPos:i+3] 


    return orf_candidates.copy() 



if __name__ == "__main__":
    file_path="/Users/achemkhi/Library/CloudStorage/OneDrive-Illumina,Inc/Desktop/rosalind/input_data.txt"
    
    with open(file_path, 'r') as fasta_file :
        RecordsRead=0
        for record in SeqIO.parse(fasta_file, 'fasta'):
            RecordsRead=RecordsRead+1
            
            mySequence=record.seq
            reverseSequence=record.reverse_complement().seq

            orf_candidates=get_orf(mySequence)
            orf_candidates_reverse=get_orf(reverseSequence)

           
            res=[]
            for orfPos,orfseq in orf_candidates.items():
                if (orfseq!="") and (orfseq.translate(to_stop=True) not in res):
                    res.append(orfseq.translate(to_stop=True))

            for orfPos,orfseq in orf_candidates_reverse.items():
                if (orfseq!="") and (orfseq.translate(to_stop=True) not in res):
                    res.append(orfseq.translate(to_stop=True))
            
            res.sort()
            for prot in res :
                print(prot) 



    assert RecordsRead==1
                