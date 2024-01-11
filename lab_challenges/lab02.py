import os
import time
from datetime import datetime
import platform
import smtplib
from email.mime.text import MIMEText

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

def send_email_notification(email_address, email_password, subject, message):
   """
   Sends an email notification using the provided credentials.
   """
   msg = MIMEText(message)
   msg['Subject'] = subject
   msg['From'] = email_address
   msg['To'] = email_address  # Send to the same address for simplicity

   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
       server.login(email_address, email_password)
       server.send_message(msg)

def uptime_sensor(ip_address, email_address, email_password):
   """
   Continuously monitors the uptime of a host and sends email notifications when status changes.
   """
   previous_status = None

   while True:
       timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       status = "Success" if ping(ip_address) else "Failure"

       if status != previous_status:
           subject = f"Host Status Change: {ip_address}"
           message = f"Host {ip_address} status changed from {previous_status} to {status} at {timestamp}."
           send_email_notification(email_address, email_password, subject, message)

       print(f"{timestamp} - {ip_address}: {status}")
       previous_status = status
       time.sleep(2)

if __name__ == "__main__":
   ip_to_monitor = input("Enter the IP address to monitor: ")
   email_address = input("Enter your email address for notifications: ")
   email_password = input("Enter your email password: ")
   uptime_sensor(ip_to_monitor, email_address, email_password)
