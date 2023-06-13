file1 = open("/home/salma/Desktop/Final_Project/output.bls","r")
file2 = open("blat_info.txt","w")
count,scount=0,0;

sequences = file1.read().split('Query=')[1:]
for ele in sequences:
    file2.write("##################################################\n")
    a = ele.split(">")
    count=1;
    for e in a[:2]:
        b = e.strip();
        c = b.split("\n");
        for i in c:
            if i=='':
                c.remove('')
        if count==1:
            file2.write("Query ID = "+c[0]+"\n")
            count=count+1;
        elif count==2:
            count=0
            scount=0;
            for i in range(0,len(c)):
                if "Score" in c[i]:
                    scount=scount+1;
                    if scount==2:
                        end=i;
            if scount==1:
                file2.write("Chromosome: "+c[0]+"\n"+c[1]+"\n"+c[2]+"\n"+c[3]+"\n"+c[4]+"\n")
                for j in range(0,len(c)):
                    if c[j].startswith("Query:") or c[j].startswith("Sbjct:"):
                        file2.write(c[j]+"\n")
            if scount>=2:
                for k in range(0,end):
                    if k==0:
                        file2.write("Chromosome: "+c[k]+"\n")
                    else:
                        file2.write(c[k]+"\n")
        
                
file1.close()
file2.close()
