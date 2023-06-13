from Bio import SeqIO
import re
file1=open("dynamic_distribution_est.txt","a")
Astring,Tstring,Acount,Tcount,i,j,totalseq='A','T',0,0,-1,1,0;

file1.write("\t\tA"+"\t\tT\n")

for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/Zea_mays.txt", "fasta"):
    totalseq=totalseq+1;
    a = str(seq_record.seq);
    b = a[-1:]
    c = a[0]
    if b!=Astring:
        Acount=Acount+1;
    if c!=Tstring:
        Tcount=Tcount+1;
file1.write('0'+"\t\t"+str(Acount)+"\t\t"+str(Tcount)+"\n")

for x in range(0,11):
    Acount,Tcount=0,0;
    for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/Zea_mays.txt", "fasta"):
        a = str(seq_record.seq);
        b=a[i:]
        c=a[0:j]
        if b==Astring:
            Acount=Acount+1;
        if c==Tstring:
            Tcount=Tcount+1;
            
    Astring=Astring+'A';
    Tstring=Tstring+'T';
    i=i-1;
    j=j+1;
    file1.write(str(x+1)+"\t\t"+str(Acount)+"\t\t"+str(Tcount)+"\n")

file1.write("Total no. of sequences: "+str(totalseq))
file1.close()
