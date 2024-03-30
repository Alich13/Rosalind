
from calendar import c
from curses import keyname
import os
import glob
from re import A
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import argparse


transition_probability = {
'A' : {'A':0.459,'B':0.343,'C':0.197},
'B' : {'A':0.031,'B':0.497,'C':0.472},
'C' : {'A':0.208,'B':429,'C':0.364}	
}


emission_probability = {
'A' : {'x': 0.195, 'y': 0.632, 'z': 0.173},
'B' : {'x': 0.361, 'y':  0.26, 'z': 0.379},
'C' : {'x': 0.358, 'y':  0.325, 'z': 0.316}
}


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
 
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
    n = 0           # if only one element is observed max is sought in the initialization values
    if len(obs) != 1:
        n = t
    # print_dptable(V)
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])



if __name__ == "__main__":



    
    states = ('A', 'B')
    observations_str="zxxxyxzzzzxyzzyzyxyyyyzzyyzzyzzxzxzyyxxyxyzyxxyxzyyzyyyzyzzzzyxzyyzzxzxyxxxyxzxyxzzxzyxyyyzzyyzxyxxy"
    observations = tuple([x for x in observations_str])
    start_probability = {'A': 0.5, 'B': 0.5}
    

    transition_probability = {
    'A' : {'A':0.784,'B':0.216},
    'B' : {'A':0.788,'B':0.212}
    }
    emission_probability = {
    'A' : {'x': 0.428, 'y': 0.558,"z":0.014},
    'B' : {'x': 0.702, 'y':  0.254,"z":0.044}
    }
    a=viterbi(observations, states, start_probability, transition_probability, emission_probability)
    print("".join(a[1]))

    

