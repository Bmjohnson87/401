import subprocess
import shlex

def banner_grabbing_netcat(target, port):
    try:
        # Using Netcat for banner grabbing
        command = f"echo '' | nc {target} {port}"
        process = subprocess.run(shlex.split(command), capture_output=True, timeout=10)
        result = process.stdout.decode().strip()
        print(f"Netcat banner grabbing results for {target}:{port}:\n{result}")
    except subprocess.TimeoutExpired:
        print("Netcat banner grabbing timed out.")
    except Exception as e:
        print(f"An error occurred with Netcat banner grabbing: {e}")

def banner_grabbing_telnet(target, port):
    try:
        # Using Telnet for banner grabbing
        command = f"echo 'QUIT' | telnet {target} {port}"
        process = subprocess.run(shlex.split(command), capture_output=True, timeout=10)
        result = process.stdout.decode().strip()
        print(f"Telnet banner grabbing results for {target}:{port}:\n{result}")
    except subprocess.TimeoutExpired:
        print("Telnet banner grabbing timed out.")
    except Exception as e:
        print(f"An error occurred with Telnet banner grabbing: {e}")

def banner_grabbing_nmap(target):
    try:
        # Using Nmap for banner grabbing on well-known ports
        command = f"nmap -sV {target}"
        process = subprocess.run(shlex.split(command), capture_output=True, timeout=60)
        result = process.stdout.decode().strip()
        print(f"Nmap banner grabbing results for {target}:\n{result}")
    except subprocess.TimeoutExpired:
        print("Nmap banner grabbing timed out.")
    except Exception as e:
        print(f"An error occurred with Nmap banner grabbing: {e}")

if __name__ == "__main__":
    target = input("Type a URL or IP address: ")
    port = input("Type a port number: ")
    
    print("\nPerforming banner grabbing using Netcat...")
    banner_grabbing_netcat(target, port)
    
    print("\nPerforming banner grabbing using Telnet...")
    banner_grabbing_telnet(target, port)
    
    print("\nPerforming banner grabbing using Nmap on well-known ports...")
    banner_grabbing_nmap(target)
