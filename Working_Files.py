import os
import time
import datetime
import subprocess


Current_time=datetime.datetime.now()
Full_name=str(input("Enter Full_name: "))
fo=open(f"{Full_name}.txt","w")
fo.write(f"{Full_name} \n{Current_time}")
fo.close()

'''
cmd=[r"cd /d D:\Python_Ex\Working_Files\Working_Files\test-github", "git add .", "git commit -am \"finish_commit\"",
     "git remote add origin \"https://github.com/trankhai677/test-github.git\"","git push origin main"]

for i in cmd:
    print(i)
    sp=subprocess.Popen(i, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True)   
    rc=sp.wait()
    out,err=sp.communicate(input=sp,timeout= 5000)
    print(f'rc: {rc}\n')
    print(f"out: {out.splitlines()}\n")
    print(f"err: {err.splitlines()}")
'''
'''
sp1=subprocess.run(r"cd /d D:\Python_Ex\Working_Files\Working_Files\test-github", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp1.stderr)
sp2=subprocess.run("git add .", shell= True,stdin=sp1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp2.stderr)
sp3=subprocess.run("git commit -am \"finish_commit\"", shell= True,stdin=sp2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp3.stderr)
#sp4=subprocess.run("git remote add origin \"https://github.com/trankhai677/test-github.git \"", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
#print(sp4.stderr)
sp5=subprocess.run("git push origin main", shell= True, stdout=subprocess.PIPE,stdin=sp3.stdout, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp5.stderr)
'''
os.system("git add . \n git commit -am \"Finish-commit\" \n git push origin main ")