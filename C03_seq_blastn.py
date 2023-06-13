from Bio import SeqIO
import re
from Bio.Blast.Applications import NcbiblastpCommandline
from StringIO import StringIO
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from subprocess import call
import os

for seq_record in SeqIO.parse("test_file_est.fasta", "fasta"):
    
    a = seq_record.id;
    a = a.split("|");
    a = a[0];
   
    b = str(seq_record.seq);
    seq1 = SeqRecord(Seq(b),
                   id=a)
    
    for seq in SeqIO.parse("test_file_trace.fasta", "fasta"):
        c = seq.id;
        c = c.split("|");
        c = c[3]
        d = str(seq.seq).replace("\n",'')
        seq2 = SeqRecord(Seq(d),
                   id=c)
        
        if a==c:
                 
            SeqIO.write(seq1, "seq1.fasta", "fasta")
            SeqIO.write(seq2, "seq2.fasta", "fasta")
            output = NcbiblastpCommandline(query="seq1.fasta", subject="seq2.fasta", outfmt=5)()[0]
            blast_result_record = NCBIXML.read(StringIO(output))
            for alignment in blast_result_record.alignments:
                for hsp in alignment.hsps:
                    print '****Alignment****'
                    print 'sequence:', alignment.title
                    print 'length:', alignment.length
                    print 'e value:', hsp.expect
                    #print hsp.query
                    #print hsp.match
                    #print hsp.sbjct
                    #print hsp.align_length
                    print hsp.sbjct_start
        
