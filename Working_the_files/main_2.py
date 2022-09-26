import os
import shutil
import zipfile
def print_file():
    fo=open("file.txt","w")
    req_path=input("Enter your directory path: ")
    if os.path.isfile(req_path):
        print(f'The given path {req_path} is a file. Please pass only directory path')
    else:
        list_= os.listdir(req_path)
        if len(list_) ==0:
            print(f'The given  path {req_path} is an empty path')
        else:
            #print(list_)
            for r,d,f in os.walk(req_path):
                for each_file in f:
                   #print(r) 
                   fo.write(f'file names: {each_file} - file path : {os.path.join(r,each_file)}\n')
    return None

def Movefile():
    src1="./Exercise2/src/Module_A.h"
    src2="./Exercise2/src/Module_B.h"
    dest="./Exercise2/inc/"
    shutil.move(src1,dest)
    shutil.move(src2,dest)
    return None

def Delete_file():
    path="D:\Python_Ex\Working_the_files\Working_the_files\Exercise2\lib"
    for r,d,f in os.walk(path):
        for each_file in f:
            if each_file.endswith(".a"):
                os.remove(os.path.join(r,each_file))
    return None

def Zipfile():
    jungle_zip = zipfile.ZipFile('D:\\Python_Ex\\Working_the_files\\Working_the_files\\Exercise2\\bin.zip', 'w')
    jungle_zip.write('D:\\Python_Ex\\Working_the_files\\Working_the_files\\Exercise2\\bin.zip', compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()
def main():
    print_file()
    Movefile()
    Delete_file()
    Zipfile()   
main()