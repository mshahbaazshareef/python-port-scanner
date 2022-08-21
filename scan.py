import time
import socket
import pyfiglet
import sys
from datetime import datetime
 
ascii_banner = pyfiglet.figlet_format("Dynamic PORT SCANNER")
print(ascii_banner)
start = time.time()  
# Defining a target
if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number Argument")
 
# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

def ScanNow(target):

    try:
        
        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()
            
    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()

ScanNow(target)
end = time.time()
total_time = end - start
print("-" * 50)
print("Script Scan complete for: " + target)
print("Scanning ended at: " + str(datetime.now()))
print("Total time for scan: {}" .format(str(total_time)) + "seconds" )
print("-" * 50)


# commands to check 
# use lsof -i :<port number> to check details of the process running on the port
# use ps -p <process id> to get details of the process