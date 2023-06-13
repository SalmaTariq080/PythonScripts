import fileinput
for i in range(1,19):
      for line in fileinput.input("/home/salma/Desktop/Final_Project/Datasets/zea_mays_traces/fasta.zea_mays."+"00"+str(i), inplace=True):
            if line.startswith(">"):
                  print (line.replace(' ', '|').replace('\n',''))
            else:
                  print(line.replace('\n',''))
      
