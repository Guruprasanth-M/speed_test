import socket
from urllib.request import urlopen

def get_hostname():
    return socket.gethostname()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_public_ip():
    return urlopen("https://api.ipify.org").read().decode().strip()

if __name__ == "__main__":
    print("Hostname     :", get_hostname())
    print("Local IP     :", get_local_ip())
    print("Public IP    :", get_public_ip())
