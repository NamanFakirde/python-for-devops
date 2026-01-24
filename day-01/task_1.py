# You will create a Python script that:

# 1. Takes threshold values (CPU, disk, memory) from user input
# 2. Also fetches system metrics using a Python library (example: psutil)
# 3. Compares metrics against thresholds
# 4. Prints the result to the terminal

import psutil

def threshold_values():

    print("THRESHOLD VALUES:")
    cpu_threshold = int(input("Enter threshold value of CPU: "))
    disk_threshold = int(input("Enter threshold value of DISK: "))
    memory_threshold = int(input("Enter threshold value of MEMORY: "))

    print("\nCURRENT VALUES:")
    current_cpu = psutil.cpu_percent(interval=1)
    print(f"current CPU usage: {current_cpu} %")
    current_disk = psutil.disk_usage('/')
    print(f"current DISK usage: {current_disk.percent} %")
    current_memory = psutil.virtual_memory() 
    print(f"current MEMORY usage: {current_memory.percent} %\n")

    print("FINAL OUTPUTS:")

    if current_cpu > cpu_threshold:
        print("send CPU ALERT Mail")
    else:
        print("CPU is safe")
        
    if current_disk.percent > disk_threshold:
        print("send DISK ALERT Mail")
    else:
        print("DISK is SAFE")

    if current_memory.percent > memory_threshold:
        print("send MEMORY ALERT Mail")
    else:
        print("MEMORY is SAFE")
        

threshold_values()