from operator import itemgetter
file1=open("/home/salma/Desktop/Final_Project/filtered_valid_tails.csv","r")
file2=open("/home/salma/Desktop/Final_Project/sort_filtered_valid_tails.csv","w")
a=[]
for line in file1:
    line=line.replace("\n","").split(",")
    line[11]=int(line[11])
    line[12]=int(line[12])
    a.append(line)
b=sorted(a,key=itemgetter(2,8,11,12))
for i in b:
    file2.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[7])+","+str(i[8])+\
                ","+str(i[9])+","+str(i[10])+","+str(i[11])+","+str(i[12])+","+str(i[13])+","+str(i[14])+","+str(i[15])+"\n")
file1.close()
file2.close()
