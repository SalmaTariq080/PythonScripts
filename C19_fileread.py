file1=open("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/Even_Smaller_10k/xaa_output.bls","r")
query_id=raw_input("enter query id here")
Query_list = file1.read().split('Query=')[1:]
for query in Query_list:
        Hit_list = query.split(">")
        count=1;
        for e in Hit_list[:2]:
            b = e.strip();
            c = b.split("\n");
            for i in c:
                if i=='':
                    c.remove('')
            t=c[0].split("|")
            if query_id == t[0]:
                    print(t[0])
                    print(Hit_list[1])
               
