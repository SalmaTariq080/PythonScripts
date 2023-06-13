#This file contains 1 function "Extract_Blat_Output". It takes input from any file (given as path). Extracts info from the file and writes the extracted information to a csv file "blat_info.csv"
#file1=open("/home/salma/Desktop/Final_Project/est_tail_greaterthan5.txt","r")
import re
from Bio import SeqIO
def Extract_Blat_Output(input_file):
    output_file = open("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/xaa_2_info.csv","w")
    output_file.write("Query_ID,Query_length,chromosome_no,chr_length,alig_Score,expected_value,identity,Que_strand,sub_strand,Query_Start,Query_end,Sub_Start,Sub_end,validity_polyat,seq_after_alignment,seq_before_alignment\n")
    count,score_count=0,0;
    Query_list = input_file.read().split('Query=')[1:] #splitting on the base of "query" so that each index of the list contains a query and all the hits for that particular query
    for query in Query_list:
        Hit_list = query.split(">") #in each iteration getting a list by splitting on the basis of ">" to separate all the hits for a particular query each string in "Hit_list" is a different hit
        count=1;
        for e in Hit_list[:2]:#first two indexes of the hit_list contains the hit with the best e_value(first index has the query id of the hit and second index has all info relating that hit )
            b = e.strip();
            c = b.split("\n");
            for i in c:
                if i=='':#removing empty strings from the list "c"
                    c.remove('')
            if count==1:
                t=c[0].split("|")
                #print(t)
                Query_ID=t[0]
                Query_length=c[1].strip().replace("(","").split();
                Query_length=Query_length[0]
                count=count+1;
            elif count==2:
                count=0
                score_count=0;
                for i in range(0,len(c)):
                    if "Score" in c[i]:
                        score_count=score_count+1;
                        if score_count==2:
                            end=i;
                if score_count==1:
                    chromosome_no=c[0]
                    for l in range(1,5):    
                        b=re.split("=|,",c[l])
                        if l==1:             
                            chr_length=b[1]
                        if l==2:
                             alig_Score=b[1]
                             expected_value=b[3]
                        if l==3:
                            identity=b[1]
                        if l==4:
                            strand=b[1].split("/")
                            Que_strand=strand[0]
                            sub_strand=strand[1]
                    Get_Que_St_end=[]
                    Get_Sub_St_end=[]
                    for j in range(0,len(c)):
                        if c[j].startswith("Query:"):
                            m=re.split(': |\\s+',c[j])
                            Get_Que_St_end.append(m[1])
                            Get_Que_St_end.append(m[3])
                        if c[j].startswith("Sbjct:"):
                            n=re.split(': |\\s+',c[j])
                            Get_Sub_St_end.append(n[1])
                            Get_Sub_St_end.append(n[3])
                    Query_Start=Get_Que_St_end[0]
                    Query_end=Get_Que_St_end[-1]
                    Sub_Start=Get_Sub_St_end[0]
                    Sub_end=Get_Sub_St_end[-1]
                if score_count>=2:
                    for k in range(0,end):
                        if k==0:
                           chromosome_no=c[k]
                           #print("Chromosome: "+c[k]+"\n")
                        else:
                            for l in range(1,5):    
                                b=re.split("=|,",c[l])
                                if l==1:             
                                    chr_length=b[1]
                                if l==2:
                                    alig_Score=b[1]
                                    expected_value=b[3]
                                if l==3:
                                    identity=b[1]
                                if l==4:
                                    strand=b[1].split("/")
                                    Que_strand=strand[0]
                                    sub_strand=strand[1]
                            Get_Que_St_end=[]
                            Get_Sub_St_end=[]
                            for j in range(0,end):
                                if c[j].startswith("Query:"):
                                    m=re.split(': |\\s+',c[j])
                                    Get_Que_St_end.append(m[1])
                                    Get_Que_St_end.append(m[3])
                                if c[j].startswith("Sbjct:"):
                                    n=re.split(': |\\s+',c[j])
                                    Get_Sub_St_end.append(n[1])
                                    Get_Sub_St_end.append(n[3])
                            Query_Start=Get_Que_St_end[0]
                            Query_end=Get_Que_St_end[-1]
                            Sub_Start=Get_Sub_St_end[0]
                            Sub_end=Get_Sub_St_end[-1]
        for seq_record in SeqIO.parse("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/xaa", "fasta"):
            est_id = seq_record.id;
            est_seq=seq_record.seq;
            a = est_id.split("|");
            a = a[0];
            cHECK_vALID_pOLYt=False
            cHECK_vALID_pOLYa=False
            if Query_ID==a:
                seq_before_alignment = est_seq[:int(Query_Start)] # Gives sequence from 0th index to the Query_Start index.
                seq_after_alignment = est_seq[int(Query_end)+1:]    # Gives sequence from the Query_End index till the end of the query sequence.
            if(len(seq_before_alignment)>0):
                s=seq_before_alignment
                cHECK_vALID_pOLYt=(s == len(s) * "T")
            if(len(seq_after_alignment)>0):
                t=seq_after_alignment
                cHECK_vALID_pOLYa=(t==len(t) * "A")
            if cHECK_vALID_pOLYt==True or cHECK_vALID_pOLYa==True:
                VALIDITY_CHECK="Valid"
            else:
                VALIDITY_CHECK="Invalid"
      
        #print("PolyAcheck: "+str(seq_after_alignment)+"\nPolyTcheck: "+str(seq_before_alignment))
        output_file.write(Query_ID +","+ Query_length +","+ chromosome_no+"," + chr_length+"," + alig_Score+"," + \
                          expected_value+"," + identity+"," + Que_strand+","+sub_strand+"," + Query_Start+"," + Query_end+"," + Sub_Start+"," + Sub_end+","+VALIDITY_CHECK+","+str(seq_after_alignment)+","+str(seq_before_alignment)+"\n")

    input_file.close()
    output_file.close()
    
Extract_Blat_Output (open(input("enter the file path :"),"r"))

