import os
import shutil
files = [x for x in os.listdir("./dataset")]
train_file = open("train_data.txt","w")
train_dir=os.path.join(os.getcwd(),"train")
test_dir=os.path.join(os.getcwd(),"test")
test_file = open("test_data.txt","w")
print (files)
for j,file in enumerate(sorted(files)):
    img_list = [x for x in os.listdir("./dataset/"+str(file)) if x.endswith(".jpg")]
    for i, img_name in enumerate(sorted(img_list)):
        txt = str(img_name)+"~"+str(j)
        if i%4==0:
            shutil.copy("./dataset/{}/{}".format(file,img_name),test_dir)
            test_file.write(txt+"\n")
        else:
            shutil.copy("./dataset/{}/{}".format(file,img_name),train_dir)

            train_file.write(txt+"\n")
            
train_file.close()
test_file.close()