from Bio import SeqIO
import re

file1=open("est_tail_greaterthan3.txt","a")
seq_3A_3T=0
seq_5A_5T=0


for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/Zea_mays.txt", "fasta"):
    sequence = str(seq_record.seq);
    seq_3A_end=sequence[-3:]
    seq_3T_start=sequence[:3]
    seq_5A_end=sequence[-5:]
    seq_5T_start=sequence[:5]
    if seq_3A_end=='AAA' or seq_3T_start=='TTT' :
       seq_3A_3T=seq_3A_3T+1
    if seq_5A_end=='AAAAA' or seq_5T_start=='TTTTT':
       seq_5A_5T=seq_5A_5T+1
print("sequences with 3 A's at the end or 3T's at the start:",seq_3A_3T)
print("sequences with 5 A's at the end or 5T's at the start:",seq_5A_5T)
    
file1.close()
