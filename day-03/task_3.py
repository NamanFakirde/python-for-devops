# You will take any one script from:

# Day 01 (System Health Script), or
# Day 02 (API & JSON Script)
# And enhance it by:

# Organizing the code into functions
# Adding basic exception handling (try / except)
# Improving variable names and readability
# Ensuring the script does not crash on common errors
# This task focuses on writing cleaner and safer Python code, which is critical for DevOps automation.

import psutil

def threshold_values():
    while True:
            try:
                print("THRESHOLD VALUES:")
                cpu_threshold = int(input("Enter threshold value of CPU: "))
                disk_threshold = int(input("Enter threshold value of DISK: "))
                memory_threshold = int(input("Enter threshold value of MEMORY: "))
                if cpu_threshold or disk_threshold or memory_threshold > 90:
                    raise ValueError("Enter valid number")
                else:
                    pass

                break

            except ValueError:
                print("Enter the valid threshold input value")

    try:
        print("\nCURRENT VALUES:")
        current_cpu = psutil.cpu_percent(interval=1)
        print(f"current CPU usage: {current_cpu} %")
        current_disk = psutil.disk_usage('/')
        print(f"current DISK usage: {current_disk.percent} %")
        current_memory = psutil.virtual_memory() 
        print(f"current MEMORY usage: {current_memory.percent} %\n")
    except OSError as error:
        print(f"System error {error}")
        return

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