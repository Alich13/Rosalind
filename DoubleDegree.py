import os
import glob
import pandas as pd
import math
import numpy as np
import datetime
from Bio import SeqIO
import argparse

graph={}
if __name__ == "__main__":
    firstLine=True
    with open("/Users/achemkhi/Library/CloudStorage/OneDrive-Illumina,Inc/Desktop/rosalind/input_data.txt","r") as inputFile: 
        count_dict={}

        for line in inputFile.readlines():
            edge= tuple([int(x) for x in line.split(" ")])

            if (firstLine):
                totalNumberOfNodes=edge[0]
                firstLine=False
                # init graph nodes 
                for i in range(1,totalNumberOfNodes+1):
                    graph[i]=[]
                continue

                
                
            
            # construct non directional graph 
            graph[edge[0]]+= [edge[1]]
            graph[edge[1]]+= [edge[0]]

            # count 
            
            if edge[0] in count_dict.keys():
                count_dict[edge[0]]+=1
            else : 
                count_dict[edge[0]]=1

            if edge[1] in count_dict.keys():
                count_dict[edge[1]]+=1
            else : 
                count_dict[edge[1]]=1

    
    sorted_count = dict(sorted(count_dict.items()))
    sorted_graph = dict(sorted(graph.items()))

    output=""

    print(sorted_graph)
    print(sorted_count)

    for k,v in graph.items():
        output+=f"{sum ([ sorted_count[i]  if (len(v) >0) else 0 for i in v   ])} "
    
    print(output)


                
