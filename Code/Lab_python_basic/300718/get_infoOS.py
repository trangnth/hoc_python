# Get info OS, RAM, CPU, trả về dạng json
# Sử dụng cho cả Windows và Ubuntu 

import platform
import psutil
import json

def info_os():
	data = {}
	# check_distro	
	data["platform"] = platform.platform()
	
	# check_cpu():
	data["cpu_count:"] = psutil.cpu_count()

	# check_ram():
	mem = psutil.virtual_memory().total / (1024**3)
	data["mem_total"] = round(mem,2)
	
	return data

### output file
#with open('infoOS.json', 'w') as f:
#	json.dump(data,f,indent=2)

#if __name__ == "__main__":
