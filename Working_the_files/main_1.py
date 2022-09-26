import subprocess
print("Inside Python file.");
subprocess.call(["gcc","main.c"])
subprocess.call("./a.exe");
print("Task is done.")