import os
#import time
import subprocess
import shutil
#start_time=time.time()
Full_name=str(input("Enter Full_name: "))
fo=open(f"{Full_name}.txt","w")
fo.write(Full_name+"\n")
fo.close()
src=os.path.join("D:\\Python_Ex\\Working_the_files\\Working_the_files\\",str(fo.name))
des="D:\\Python_Ex\\Working_the_files\\test-github\\"
shutil.move(src,des)

cmd=[r"cd /d D:\Python_Ex\Working_the_files\test-github", "git add .","git commit -am \"Finish_commit\"", "git push origin main"]
for i in cmd:
    print(i)
    sp=subprocess.Popen(i, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rc=sp.wait()
    out,err=sp.communicate()
    print(rc)
    print(out)
    print(err)

'''
sp=subprocess.Popen(r"cd /d D:\Python_Ex\Working_the_files\test-github", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
rc=sp.wait()
out,err=sp.communicate()
print(rc)
print(out)
print(err)
'''