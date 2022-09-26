import os
import time
import datetime
import subprocess


Current_time=datetime.datetime.now()
Full_name=str(input("Enter Full_name: "))
fo=open(f"{Full_name}.txt","w")
fo.write(f"{Full_name} \n{Current_time}")
fo.close()
time.sleep(3)

os.system(r"cd /d D:\Python_Ex\Working_Files\Working_Files\test-github")
os.system("git add .")
os.system("git commit -am \"finish-commit\" ")
os.system("git push origin main") 




'''
cmd=[r"cd /d D:\Python_Ex\Working_Files\Working_Files\test-github", "git add .", "git commit -am \"finish_commit\"","git push origin main"]
for i in cmd:
    print(i)
    sp=subprocess.Popen(i, shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True)   
    rc=sp.wait()
    out,err=sp.communicate()
    print(f'rc: {rc}\n')
    print(f"out: {out.splitlines()}\n")
    print(f"err: {err.splitlines()}")
'''

'''
sp1=subprocess.run(r"cd /d D:\Python_Ex\Working_Files\Working_Files\test-github", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp1.stderr)
sp2=subprocess.run("git add .", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp2.stderr)
sp3=subprocess.run("git commit -am \"finish_commit\"", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp3.stderr)
sp4=subprocess.run("git push origin main", shell= True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines= True) 
print(sp4.stderr)
'''

'''
os.system("git add .")
os.system("git commit -am \"finish-commit\" ")
os.system("git push origin main") 
'''