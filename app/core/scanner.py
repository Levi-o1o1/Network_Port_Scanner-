import socket
from typing import List


class PortScanner:
    def __init__(self, timeout: float = 1.0):
        self.timeout = timeout

    def scan_port(self, host: str, port: int) -> bool:
        """
        Scan a single port
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((host, port))
                return result == 0
        except Exception:
            return False

    def scan_range(self, host: str, start_port: int, end_port: int) -> List[int]:
        """
        Scan a range of ports
        """
        open_ports = []

        for port in range(start_port, end_port + 1):
            if self.scan_port(host, port):
                open_ports.append(port)

        return open_ports

    def scan_list(self, host: str, ports: List[int]) -> List[int]:
        """
        Scan a custom list of ports
        """
        open_ports = []

        for port in ports:
            if self.scan_port(host, port):
                open_ports.append(port)

        return open_ports