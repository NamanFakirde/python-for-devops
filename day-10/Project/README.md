# Internal DevOps Utilities API

## Aim

Internal DevOps API tool for Internal team which help in: 

- AWS Resources APIs (s3, ec2)
- System Metrics (CPU, Disk, Memory)
- Log Analysis

## Usage

```bash
git clone <repo-url>
cd day-09
cd project
```

### Setup python environment (for windows)
```bash
python -m venv venv 
venv\scripts\activate
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Run application
```bash
python main.py
```
<br>
<br>

---

# CAPSTONE PROJECT (STAR explanation)

### SITUATION

- In cloud-based environments, monitoring required significant manual effort.
- Checking AWS EC2 instances and S3 buckets involved logging into the console repeatedly.
- Monitoring system health metrics (CPU, memory, disk usage) required running multiple commands.
- Application log files were growing daily, and manually identifying error patterns was time-consuming and inefficient.

### TASK

- To automate AWS resource monitoring to reduce manual dependency.
- To build a centralized solution to fetch real-time system metrics in one place.
- To develop an automated log analysis mechanism to quickly detect and count error-level logs.
- to integrate all three into a unified API-based reporting system.

### ACTION

- Used Boto3 to programmatically fetch EC2 instance details and S3 bucket information from AWS.
- Used psutil to collect real-time CPU, memory, and disk usage metrics.
- Developed a Python-based log analyzer to parse log files and count error-level entries.
- Built REST APIs using FastAPI to expose all monitoring data in structured JSON format.
- Deployed the application using Uvicorn as the ASGI server to handle API requests efficiently.
- Designed the project in a modular way to ensure scalability and maintainability using proper folder structure.

### Result

- Reduced manual monitoring effort significantly.
- Provided real-time visibility into AWS infrastructure and system performance.
- Improved issue detection speed through automated log analysis.
- Centralized cloud, system, and log monitoring into a single lightweight API service.
- Created a scalable DevOps-style automation solution suitable for production environments.
- Eventually this made the work of internal team more realiable and time saving.