import os
import shutil
files = [x for x in os.listdir("./nut_snacks/dataset")]
train_file = open("./nut_snacks/train_data.txt","w")
test_file = open("./nut_snacks/test_data.txt","w")

if os.path.isdir(os.path.join(os.getcwd(),"nut_snacks/train")):
    train_dir=os.path.join(os.getcwd(),"nut_snacks/train")
else:
    os.mkdir(os.path.join(os.getcwd(),"nut_snacks/train"))
    train_dir=os.path.join(os.getcwd(),"nut_snacks/train")

if os.path.isdir(os.path.join(os.getcwd(),"nut_snacks/test")):
    test_dir=os.path.join(os.getcwd(),"nut_snacks/test")
else:
    os.mkdir(os.path.join(os.getcwd(),"nut_snacks/test"))
    test_dir=os.path.join(os.getcwd(),"nut_snacks/test")

print (files)
for j,file in enumerate(files):
    img_list = [x for x in os.listdir("./nut_snacks/dataset/"+str(file)) if x.endswith(".jpg")]
    for i, img_name in enumerate(img_list):
        txt = str(img_name)+"~"+str(j)
        if len(img_list)==1:
            shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),test_dir)
            test_file.write(txt+"\n")
            shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),train_dir)
            train_file.write(txt+"\n")
        elif i%4==0:
            shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),test_dir)
            test_file.write(txt+"\n")
        else:
            shutil.copy("./nut_snacks/dataset/{}/{}".format(file,img_name),train_dir)

            train_file.write(txt+"\n")
            
train_file.close()
test_file.close()