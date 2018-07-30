# Get info OS, RAM, CPU. print json 

import platform, os, psutil
import json

data = {}
os = {}
cpu = {}
ram = {}

def check_os():
	os["platform"] = platform.platform()
	os["system"] = platform.system()
	os["node"] = platform.node()
	os["release"] = platform.release()
	os["version"] = platform.version()

def check_cpu():
	cpu["machine"] = platform.machine()
	cpu["processor"] = platform.processor()
	cpu["cpu_count:"] = psutil.cpu_count()

def check_ram():
	ram["mem_total"] = psutil.virtual_memory().total

	
print("haha")

#if __name__ == "__main__":
#json_parse()
check_os()
check_ram()
check_cpu()
data["os"] = os
data["cpu"] = cpu
data["ram"] = ram
print(data)
