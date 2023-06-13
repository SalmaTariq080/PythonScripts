from Bio import SeqIO
import re

file1=open("mismatch_distribution_est.txt","w")
Acount,Tcount,i,j=0,0,-4,4;

file1.write("\t\t\t***Accomodating ONE mismatch***\nLength\t\tA"+"\t\tT\n")
pat1=re.compile("A+[^A]AA+"); #changed the regex a bit.
pat2=re.compile("T+[^T]TT+"); #here too.

for x in range(0,10):
    for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/Zea_mays.txt", "fasta"):
        a = str(seq_record.seq);
        b=a[i:]
        #print(b)
        c=a[0:j]
        #print(c)
        if pat1.search(b):
            Acount=Acount+1;
        if pat2.search(c):
            Tcount=Tcount+1; 
    file1.write(str(j)+"\t\t"+str(Acount)+"\t\t"+str(Tcount)+"\n")       
    i=i-1;
    j=j+1;
    
file1.close()
