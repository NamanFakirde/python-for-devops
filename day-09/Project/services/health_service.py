import psutil


def get_system_meterics():
    """
    Function to fetch the system metrics such as CPU, memory, disk etc
    """    
    cpu_threshold = 80
    disk_threshold = 85
    memory_threshold = 75

    cpu_percent = psutil.cpu_percent(interval=1)
    disk_percent = psutil.disk_usage('/').percent
    memory_percent = psutil.virtual_memory().percent

    cpu_status = "High CPU" if cpu_percent>cpu_threshold else "Healthy"
    memory_status = "High MEMORY" if memory_percent>memory_threshold else "Healthy"
    disk_status = "High DISK USAGE" if disk_percent>disk_threshold else "Healthy"

    return{
        "CPU": f"{cpu_percent}%, {cpu_status}",
        "Disk": f"{disk_percent}%, {disk_status}",
        "Memory": f"{memory_percent}%, {memory_status}"
    }

