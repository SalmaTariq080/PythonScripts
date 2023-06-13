from Bio import SeqIO
from Bio.Seq import Seq
Input=raw_input("you want to search for: \na)scaffold\nb)Pt\nc)Mt\nd)Chromosome\n")
if Input=="a" or Input=="d":
    num=raw_input("enter chromosome no or scaffold no: ")
    if Input=='a':
        search_string="scaffold_"+str(num)
    else:
        search_string=str(num)
elif Input=="b":
    search_string="Pt"
else:
    search_string="Mt"
strand=raw_input("enter strand 1)Plus or 2)Minus: ")
subject_start=int(raw_input("enter the start index: "))
subject_end=int(raw_input("enter the end index: "))
for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Phytozome_Smaller_dataset/"+search_string+".txt", "fasta"):
    b=seq_record.seq
if strand=='1':
    sequence=b[(subject_start)-21:(subject_end)+20]
    sequence_1=b[(subject_start)-21:(subject_start)-1]
    sequence_2=b[(subject_end)-5:(subject_end)+10]
    print(sequence)
    print("sequence before alignment :"+sequence_1)
    print("sequence after alignment :"+sequence_2)
if strand=='2':
    b=b.reverse_complement()
    sequence_1=b[-(subject_start)-20:-(subject_start)-1]                                      
    sequence_2=b[-(subject_end)-10:-(subject_end)+5]
    sequence=b[-(subject_start)-20:-(subject_end)+20]
    print(sequence)
    print(sequence_1)
    print(sequence_2)

       
