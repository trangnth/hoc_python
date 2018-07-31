# Get info OS, RAM, CPU. print json 

import platform, psutil
import json

data = {}
_os = {}
_cpu = {}
_ram = {}

def check_os():
# check_distro	
	data["distro"] = platform.platform()

# check_cpu():
	data["cpu_count:"] = psutil.cpu_count()

# check_ram():
	mem = psutil.virtual_memory().total / (1024**3)
	data["mem_total"] = round(mem,2)

check_os()
print(data)

#if __name__ == "__main__":
### output file
with open('infoOS.json', 'w') as f:
	json.dump(data,f,indent=2)
