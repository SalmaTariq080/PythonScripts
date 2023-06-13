from Bio import SeqIO
from Bio.Seq import Seq
file1=open("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/xaa_info.csv","r")
file2=open("genomeextract","w")   
a={}
for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/PhytozomeV11/Zmays/assembly/Zmays_284_AGPv3.softmasked.fa", "fasta"):
    est_id = seq_record.id;
    est_seq = seq_record.seq;
    a[est_id]=est_seq
for line in file1:
    line=line.replace("\n","").split(",")
    search_string=line[2]
    strand=line[8].strip()
    subject_start=int(line[11])
    subject_end=int(line[12])
    b=a.get(search_string)
    if strand=='Plus':
        sequence=b[(subject_start)-21:(subject_end)+20]
        sequence_1=b[(subject_start)-21:(subject_start)-1]
        sequence_2=b[(subject_end)-5:(subject_end)+10]
        print("sequence before alignment :"+sequence_1)
        print("sequence after alignment :"+sequence_2)
    if strand=='Minus':
        b=b.reverse_complement()
        sequence_1=b[-(subject_start)-20:-(subject_start)-1]
        sequence_2=b[-(subject_end)+1:-(subject_end)+20]
        sequence=b[-(subject_start)-20:-(subject_end)+20]
        print("sequence before alignment :"+sequence_1)
        print("sequence after alignment :"+sequence_2)

