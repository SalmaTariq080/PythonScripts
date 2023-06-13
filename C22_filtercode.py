file1=open("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/Even_Smaller_10k/full_blat_info.csv","r")
file2=open("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/Even_Smaller_10k/filtered_valid_tails.csv","w")
for i in file1:
    i=i.replace("\n","").split(",")
    if i[14]=='Valid':
        file2.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[7])+","+str(i[8])+\
                ","+str(i[9])+","+str(i[10])+","+str(i[11])+","+str(i[12])+","+str(i[13])+","+str(i[14])+","+str(i[15])+","+str(i[16])+","+str(i[17])+","+str(i[18])+"\n")
file1.close()
file2.close()
        
