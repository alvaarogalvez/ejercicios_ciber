import subprocess
import sys

def send_pings(ip_address, count):
    command = ["ping", "-c", str(count), ip_address]
    subprocess.run(command)

    ip_address = sys.argv[1]
    count = int(sys.argv[2])

    send_pings(ip_address, count)

