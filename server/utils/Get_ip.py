import socket
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def get_hostname() -> str:
    """Return system hostname."""
    return socket.gethostname()


def get_local_ip() -> str:
    """
    Return the primary local (LAN) IP address.
    Uses a UDP socket to determine the active interface.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No packets are actually sent
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "unknown"
    finally:
        s.close()


def get_public_ip(timeout: int = 5) -> str:
    """
    Return the public (WAN) IP address.
    Requires external connectivity.
    """
    try:
        return (
            urlopen("https://api.ipify.org", timeout=timeout)
            .read()
            .decode()
            .strip()
        )
    except (URLError, HTTPError, TimeoutError):
        return "unknown"


def get_ip_info() -> dict:
    """
    Aggregate IP-related information.
    This is the primary function to import elsewhere.
    """
    return {
        "hostname": get_hostname(),
        "local_ip": get_local_ip(),
        "public_ip": get_public_ip(),
    }


# Allow standalone execution for debugging
if __name__ == "__main__":
    info = get_ip_info()
    print(f"Hostname   : {info['hostname']}")
    print(f"Local IP   : {info['local_ip']}")
    print(f"Public IP  : {info['public_ip']}")
