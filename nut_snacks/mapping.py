import os
import shutil
files = [x for x in os.listdir("./dataset")]
mapping_file = open("map_data.txt","a")
# train_dir=os.path.join(os.getcwd(),"train")
# test_dir=os.path.join(os.getcwd(),"test")
#test_file = open("test_data.txt","a")
print (files)
d={}
for i,file in enumerate(files):
    d[i]=file
    mapping_file.write(str(i)+"~"+str(file)+"\n")

            
mapping_file.close()