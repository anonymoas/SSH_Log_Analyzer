import csv

def analyze_log():

    attempts = {}               # Its a dictonary , where the Failed attempts get stored
    success = []                # its a list where the success ip's get stored 

    with open("brute2.txt", "r") as files:         # used to open and read the 'brute2.txt file' : brute2.txt is a log file which --
                                               # we are using for this demo
        for line in files:                         # read each and every single line in the log file 
            if "Failed password" in line:             # if the line contains "failed password" here it will be captured.
                parts = line.strip().split()          # here the line will be splitted in the oder like : 0 1 2 3 4 5 etc...
                ip = parts[parts.index("from") + 1]   # here we seperate IP from the line , in the log file , ip address occurs after the word "from" , so .inder from + 1 , which will assign the ip to variable 
                username = parts[parts.index("for") + 1 ] # same procedure goes to here , but here we are finding usename.
                timestamp = ' '.join(parts[0:3])          #  we are assigning the timestamp of failed attempts
                key = (ip,username)                       # assigning the find ip and username to key variable

                if key in attempts:                       # loop for checking the items in attempts:
                    attempts[key]['count'] += 1           # if the ip is already there , it will add as count + 1
                else:                                     # else add the ip and timestamp as a new item and count as 1
                    attempts[key] = {'count' : 1, 'timestamp' : timestamp}

            if "Accepted password" in line:               # same steps repeated for the "Accepted password", which are successed attempts.
                parts = line.strip().split()              
                ip = parts[parts.index("from") + 1]
                username = parts[parts.index("for") + 1]
                success.append((ip,username))

    print (f"Log analyzer report !!")

    for (ip,username), info in attempts.items():          # Here , checking the items in attempts {} 
        count = info['count']                             # and the rest of the steps is to print the Results
        timestamp = info['timestamp']

        if (ip,username) in success:
            print(f"IP {ip} had eventually succeed after {count} failure attempt at {timestamp}")
        elif count >=3 :
            print(f"Alert ! user {username} from IP {ip} had {count} failed attempts")
        else:
            print(f"safe ! user {username} from IP {ip} had only {count} failures")

### These steps are used to generate a .CSV file which contain the result information

    with open("log_report.csv", "w", newline="") as csvfile:
        Heading = ["IP address", "Username", "failed attempts", "Successfull", "Failure time" ]
        writer = csv.DictWriter(csvfile , fieldnames=Heading)
        writer.writeheader()

        for (ip,username), info in attempts.items():
            writer.writerow({
                "IP address" : ip,
                "Username" : username,
                "failed attempts" : info['count'],
                "Successfull" : "yes" if (ip,username) in success else "No",
                "Failure time" : info['timestamp']
            })


if __name__ == "__main__" :
    analyze_log()