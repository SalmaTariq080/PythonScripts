from Bio import SeqIO
from Bio.Seq import Seq
rever_seq=''
Input=raw_input("you want to search for: \na)scaffold\nb)Pt\nc)Mt\nd)Chromosome\n")
if Input=="a" or Input=="d":
    num=raw_input("enter chromosome no or scaffold no: ")
    if Input=='a':
        search_string=">scaffold_"+str(num)
    else:
        search_string=">"+str(num)
elif Input=="b":
    search_string=">Pt"
else:
    search_string=">Mt"
strand=raw_input("enter strand 1)Plus or 2)Minus: ")
subject_start=int(raw_input("enter the start index: "))
subject_end=int(raw_input("enter the end index: "))
for seq_record in SeqIO.parse(R"/home/salma/Desktop/Final_Project/Datasets/PhytozomeV11/Zmays/assembly/Zmays_284_AGPv3.softmasked.fa", "fasta"):
    a = seq_record.id;
    a = a.split(" ");
    a = ">"+a[0];
    if(a==search_string):
        b=seq_record.seq
        if strand=='1':
            sequence=b[(subject_start)-20:(subject_end)+21]
            sequence1=b[(subject_start)-1:(subject_end)]
            sequence_1=b[(subject_start)-20:(subject_start)]
            sequence_2=b[(subject_end)+1:(subject_end)+21]
            print(sequence)
            print(sequence1)
            print(sequence_1)
            print(sequence_2)
        if strand=='2':
            b=b.reverse_complement()
            print(type(b))
            #sequence=b[-(subject_start):-(subject_end-1)]
            sequence_1=b[-(subject_start)-20:-(subject_start)-1]
            sequence_2=b[-(subject_end)+1:-(subject_end)+20]
            #sequence=b[-(subject_start)-20:-(subject_end)+20]
            print(sequence_1)
            print(sequence_2)

       
