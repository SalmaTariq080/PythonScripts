from Bio import SeqIO
from Bio.Seq import Seq
file1=open("/home/shiza-a/Desktop/Final_Project/Tajarbay/150K_END.csv","r")
file2=open("/home/shiza-a/Desktop/Final_Project/Tajarbay/genomeextract.csv","a")
for i in file1:
    i=i.replace("\n","").split(",")
    search_string=i[2].strip()
    strand=i[8].strip()
    subject_start=int(i[11])
    subject_end=int(i[12])
    polyA_Site=int(i[13])
    for seq_record in SeqIO.parse("/home/shiza-a/Desktop/Final_Project/Phytozome_Smaller_dataset/"+search_string+".txt", "fasta"):
        b=seq_record.seq
    if strand=='Plus':
        if polyA_Site==subject_start:
            sequence=b[(polyA_Site)-5:(polyA_Site)+10]
            count=sequence.upper().count("T")
            count_percent=(count/float(15))*100
        if polyA_Site==subject_end:
            sequence=b[(polyA_Site)-5:(polyA_Site)+10]
            count=sequence.upper().count("A")
            count_percent=(count/float(15))*100
        if count_percent>=50:
            inter_Prim_Validity="Invalid"
        else:
            inter_Prim_Validity="Valid"
    if strand=='Minus':
        b=b.reverse_complement()
        if polyA_Site==subject_start:
            sequence=b[-(polyA_Site)-10:-(polyA_Site)+5]
            count=sequence.upper().count("T")
            count_percent=(count/float(15))*100
        if polyA_Site==subject_end:
            sequence=b[-(polyA_Site)-10:-(polyA_Site)+5]
            count=sequence.upper().count("A")
            count_percent=(count/float(15))*100
        if count_percent>=50:
            inter_Prim_Validity="Invalid"
        else:
            inter_Prim_Validity="Valid"
       
    file2.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[7])+","+str(i[8])+\
                ","+str(i[9])+","+str(i[10])+","+str(i[11])+","+str(i[12])+","+str(i[13])+","+str(i[14])+","+str(i[15])+","+str(i[16])+","+str(i[17])+","+str(i[18])+","+str(sequence)+","+str(inter_Prim_Validity)+"\n")

