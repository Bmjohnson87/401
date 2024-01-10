import os
import time
from datetime import datetime
import platform

def ping(host):
   """
   Sends a single ICMP ping to a host and returns True for success, False for failure.
   """
   # Use the appropriate ping command based on the operating system
   if platform.system().lower() == "windows":
       ping_command = f"ping -n 1 {host}"
   else:
       ping_command = f"ping -c 1 {host}"

   response = os.system(ping_command)
   return response == 0  # True if ping succeeded, False otherwise

def uptime_sensor(ip_address):
   """
   Continuously monitors the uptime of a host by sending ICMP pings every 2 seconds.
   """
   while True:
       timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       status = "Success" if ping(ip_address) else "Failure"
       print(f"{timestamp} - {ip_address}: {status}")
       time.sleep(2)

if __name__ == "__main__":
   ip_to_monitor = input("Enter the IP address to monitor: ")
   uptime_sensor(ip_to_monitor)
