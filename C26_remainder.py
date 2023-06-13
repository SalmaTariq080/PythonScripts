from Bio import SeqIO
from Bio.Seq import Seq
file1=open("/home/shiza-a/Desktop/Final_Project/Tajarbay/150K_END.csv","r")
file2=open("/home/shiza-a/Desktop/Final_Project/Tajarbay/genomeextract.csv","a")
a=file1.read().split("\n")
for i in range(-12,-1):
    b=a[i].split(",")
    search_string=b[2].strip()
    strand=b[8].strip()
    subject_start=int(b[11])
    subject_end=int(b[12])
    polyA_Site=int(b[13])
    #print b[0]
    for seq_record in SeqIO.parse("/home/shiza-a/Desktop/Final_Project/Phytozome_Smaller_dataset/"+search_string+".txt", "fasta"):
        k=seq_record.seq
    if strand=='Plus':
        if polyA_Site==subject_start:
            sequence=k[(polyA_Site)-5:(polyA_Site)+10]
            count=sequence.upper().count("T")
            count_percent=(count/float(15))*100
        if polyA_Site==subject_end:
            sequence=k[(polyA_Site)-5:(polyA_Site)+10]
            count=sequence.upper().count("A")
            count_percent=(count/float(15))*100
        if count_percent>=50:
            inter_Prim_Validity="Invalid"
        else:
            inter_Prim_Validity="Valid"
    if strand=='Minus':
        k=k.reverse_complement()
        if polyA_Site==subject_start:
            sequence=k[-(polyA_Site)-10:-(polyA_Site)+5]
            count=sequence.upper().count("T")
            count_percent=(count/float(15))*100
        if polyA_Site==subject_end:
            sequence=k[-(polyA_Site)-10:-(polyA_Site)+5]
            count=sequence.upper().count("A")
            count_percent=(count/float(15))*100
        if count_percent>=50:
            inter_Prim_Validity="Invalid"
        else:
            inter_Prim_Validity="Valid"
       
    file2.write(str(b[0])+","+str(b[1])+","+str(b[2])+","+str(b[3])+","+str(b[4])+","+str(b[5])+","+str(b[6])+","+str(b[7])+","+str(b[8])+\
                ","+str(b[9])+","+str(b[10])+","+str(b[11])+","+str(b[12])+","+str(b[13])+","+str(b[14])+","+str(b[15])+","+str(b[16])+","+str(b[17])+","+str(b[18])+","+str(sequence)+","+str(inter_Prim_Validity)+"\n")

file1.close()
file2.close()






    
