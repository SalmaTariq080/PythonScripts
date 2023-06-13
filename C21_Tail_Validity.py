import re
file1=open("/home/salma/Desktop/Final_Project/NCBI_Smaller_est_greaterthan5_dataset/xaa_info.csv")
i=0
for line in file1:
     a=line.replace("\n","").split(",")
     seq_after_alignment=a[-2]
     seq_before_alignment=a[-1]
     
     countA=seq_after_alignment.count("A")
     countA_mismatch = len(seq_after_alignment) - countA;
     countT = seq_before_alignment.count("T")
     countT_mismatch = len(seq_before_alignment) - countT;
     
     if len(seq_after_alignment)>0:
          polyA_matched_percentage = countA/float(len(seq_after_alignment)) * 100
          polyA_mismatched_percentage = countA_mismatch/float(len(seq_after_alignment)) * 100
          print("polyA_matched_percentage for entry #"+str(i)+" : "+str(float(polyA_matched_percentage))+" %")
          print("polyA_mismatched_percentage for entry #"+str(i)+" : "+str(float(polyA_mismatched_percentage))+" %")
     if len(seq_before_alignment)>0:
          polyT_matched_percentage = countT/float(len(seq_before_alignment)) * 100
          polyT_mismatched_percentage = countT_mismatch/float(len(seq_before_alignment)) * 100
          print("polyT_matched_percentage for entry #"+str(i)+" : "+str(float(polyT_matched_percentage))+" %")
          print("polyT_mismatched_percentage for entry #"+str(i)+" : "+str(float(polyT_mismatched_percentage))+" %")
     i=i+1
          
