import os
import shutil
files = [x for x in os.listdir("./dataset")]
train_file = open("train_data.txt","a")
train_dir=os.path.join(os.getcwd(),"train")
test_dir=os.path.join(os.getcwd(),"test")
test_file = open("test_data.txt","a")
print (files)
for file in files:
    img_list = [x for x in os.listdir("./dataset/"+str(file)) if x.endswith(".jpg")]
    for i, img_name in enumerate(img_list):
        txt = str(img_name)+"~"+str(file)
        if i%4==0:
            shutil.copy("./dataset/{}/{}".format(file,img_name),test_dir)
            test_file.write(txt+"\n")
        else:
            shutil.copy("./dataset/{}/{}".format(file,img_name),train_dir)

            train_file.write(txt+"\n")
            
train_file.close()
test_file.close()