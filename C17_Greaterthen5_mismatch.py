import re
file1=open("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/xaa_info.csv")
pat1=re.compile("A*[^A]A*")
pat2=re.compile("T*[^T]T*")
pat3=re.compile("A*[^A]A*[^A]A*")
pat4=re.compile("T*[^T]T*[^T]T*")
Acount,Tcount,Acount_1,Tcount_1,Acount_2,Tcount_2=0,0,0,0,0,0
i=0
for line in file1:
    i=i+1
    a=line.replace("\n","").split(",")
    seq_after_alignment=a[-2]
    seq_before_alignment=a[-1]
    abb=re.search(pat1,seq_after_alignment)
    baa=re.search(pat2,seq_before_alignment)
    acc=re.search(pat3,seq_after_alignment)
    add=re.search(pat4,seq_before_alignment)
    if abb != None: 
        length_span_after_align=abb.end()-abb.start()
        if length_span_after_align == len(seq_after_alignment):
            Acount_1=Acount_1+1
            #print("line_after_align",i)
    if baa != None:
        length_span_before_align=baa.end()-baa.start()
        if length_span_before_align == len(seq_before_alignment):
            Tcount_1=Tcount_1+1
    if acc != None: 
        length_span_after_align=acc.end()-acc.start()
        if length_span_after_align == len(seq_after_alignment):
            Acount_2=Acount_2+1
    if add != None: 
        length_span_after_align=add.end()-add.start()
        if length_span_after_align == len(seq_after_alignment):
             Tcount_2=Tcount_2+1
    if seq_after_alignment == len(seq_after_alignment) * "A" and len(seq_after_alignment)>=5:
        Acount=Acount+1
        #print(i)
    if seq_before_alignment == len(seq_before_alignment) * "T" and len(seq_after_alignment)>=5:
        Tcount=Tcount+1       
            #print("line_before_align",i)
print("Poly(A) WITH NO MISMATCH: ",Acount)
print("Poly(T) WITH NO MISMATCH: ",Tcount)
print("Poly(A) WITH ONE MISMATCH: ",Acount_1)
print("Poly(T) WITH ONE MISMATCH: ",Tcount_1)
print("Poly(A) WITH TWO MISMATCH: ",Acount_2)
print("Poly(T) WITH TWO MISMATCH: ",Tcount_2)
