#This code was made using sections from C00_Matching_Ids.py C02_sequencing.py and C03_seq_blastn.py
import re
from Bio.Blast.Applications import NcbiblastpCommandline
from StringIO import StringIO
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from subprocess import call
file1= open('Est_Trace_Alignment.txt','w')
for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/test_file_est.fasta", "fasta"):#replace test_file_est.fasta with Zea_mays.txt
    
    est_id = seq_record.id;
    est_seq=str(seq_record.seq);
    est_id = est_id.split("|");
    est_id = est_id[0];
    est_seq = str(seq_record.seq);
    seq1 = SeqRecord(Seq(est_seq),
                   id=est_id)
    for i in range (1,3):
        for seq in SeqIO.parse("/home/salma/Desktop/Final_Project/Datasets/fasta.zea_mays."+"00"+str(i), "fasta"):# add ../Datasets/zea_mays_traces/fasta.zea_mays+i
            trace_id = seq.id;
            trace_seq=str(seq.seq).replace("\n",'')
            trace_id = trace_id.split("|");
            trace_id  = trace_id[3]
            seq2 = SeqRecord(Seq(trace_seq),
                   id=trace_id)
            if est_id == trace_id:
                SeqIO.write(seq1, "seq1.fasta", "fasta")
                SeqIO.write(seq2, "seq2.fasta", "fasta")
                output = NcbiblastpCommandline(query="seq1.fasta", subject="seq2.fasta", outfmt=5)()[0]
                blast_result_record = NCBIXML.read(StringIO(output))
                for alignment in blast_result_record.alignments:
                    for hsp in alignment.hsps:
                        file1.write('****Alignment****\n')
                        file1.write('Subjct Total Length: '+str(alignment.length)+'\n')
                        file1.write('Score'+str(hsp.score)+'\n')
                        file1.write('Query Start: '+str(hsp.query_start)+'\n') 
                        file1.write('Sbjct Start: '+str(hsp.sbjct_start)+'\n')
                        file1.write('Query End: '+str(hsp.query_end)+'\n')
                        file1.write('Sbjct End: '+str(hsp.sbjct_end)+'\n')
                        file1.write('Aligned Length: '+str(hsp.align_length)+'\n')
                        file1.write('Strand: '+str(hsp.strand)+'\n')
                        file1.write('Identity: '+str(hsp.identities)+'\n') 
                        file1.write('Bits: '+str(hsp.bits)+'\n\n')
                
file1.close()
