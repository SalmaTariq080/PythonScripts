from Bio import SeqIO
import re

for seq_record in SeqIO.parse("test_file_est.fasta", "fasta"):
    
    a = seq_record.id;
    a = a.split("|");
    a = a[0];
    b = str(seq_record.seq);
    reg=re.compile(b)
    #print(type(b))
    #print(a);
    #print(b);
    #add a for loop for all 5 fasta files
    for seq in SeqIO.parse("test_file_trace.fasta", "fasta"):
        c = seq.id;
        c = c.split("|");
        c = c[3]
        #print(c)
        d = str(seq.seq).replace("\n",'')
        #print(d)
        if a==c:
            result=reg.search(d)
            #print(result)
            if result is not None:
                print("matched ID:"+a)
                print("Length of seq: "+str(len(d)))
                print("Seq: "+result.group())
                print("Start: "+str(result.start()))
                print("End: "+str(result.end()))
                print("End sequence not matched: "+d[result.end():]) 
            else:
                print("no Pattern")
            print("\n")
                
  ##TT+ then calculate span       
