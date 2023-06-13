from Bio import SeqIO
for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/PhytozomeV11/Zmays/assembly/Zmays_284_AGPv3.softmasked.fa",'fasta'):
    a=seq_record.id
    #print(a)
    file1=open("/home/salma/Desktop/Final_Project/Phytozome_Smaller_dataset/"+str(a)+".txt",'w')
    file1.write(">"+str(seq_record.id)+"\n"+str(seq_record.seq)+"\n")
    file1.close()
    
    
