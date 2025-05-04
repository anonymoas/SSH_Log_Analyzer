# SSH Log Analyzer 

This Python tool analyzes SSH log files to detect suspicious login activity such as brute-force attempts and successful logins. It summarizes the findings and exports them into a CSV report.


##  Features

- Detects failed SSH login attempts from IPs and usernames
- Identifies successful logins after failed attempts
- Flags IPs with 3 or more failed login attempts
- Generates a detailed CSV report (`log_report.csv`)


##  How It Works

1. Reads an SSH log file (e.g., `brute2.txt`)
2. Extracts:
    IP address
    Username
    Timestamp
3. Tracks both failed and successful login attempts
4. Outputs alerts and safe login details
5. Exports results to a CSV file


##  Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/anonymoas/SSH_Log_Analyzer.git
   cd ssh-log-analyzer
