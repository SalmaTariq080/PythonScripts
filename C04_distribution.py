from Bio import SeqIO
import re
file1=open("distribution_est.txt","a")
Acount,Tcount=0,0;
totalseq=0
for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/Zea_mays.txt", "fasta"):
    a = str(seq_record.seq);
    b=a[-11:]
    c=a[0:11]
    if b=="AAAAAAAAAAA":
        Acount=Acount+1;
    if c=="TTTTTTTTTTT":
        Tcount=Tcount+1;
    totalseq=totalseq+1
#file1.write("\t\tA"+"\t\tT\n")
#file1.write("11\t\t"+str(Acount)+"\t\t"+str(Tcount)+"\n")
file1.write("Total no. of sequences: "+str(totalseq))
file1.close()

