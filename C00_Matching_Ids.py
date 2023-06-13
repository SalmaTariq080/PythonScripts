from Bio import SeqIO
import subprocess
for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/test_file_est.fasta", "fasta"):#replace test_file_est.fasta with Zea_mays.txt
    
    est_id = seq_record.id;
    est_seq=seq_record.seq;
    a = est_id.split("|");
    a = a[0];
    for i in range (1,3):
        for seq in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/fasta.zea_mays."+"00"+str(i), "fasta"):# add ../Datasets/zea_mays_traces/fasta.zea_mays+i
            trace_id = seq.id;
            trace_seq=seq.seq;
            c = trace_id.split("|");
            c = c[3]
            #print(c)
            if a==c:
                file1 = open('/home/salma/Desktop/Final_Project/matchedID_ourcode.txt','w')
                file1.write(">"+est_id+"\n")
                file1.write(str(est_seq)+"\n")
                file1.write(">"+trace_id+"\n")
                file1.write(str(trace_seq)+"\n")
                p=subprocess.Popen("clustalw matchedID_ourcode.txt >>tsar.txt",stdout=subprocess.PIPE,shell=True)
file1.close()
