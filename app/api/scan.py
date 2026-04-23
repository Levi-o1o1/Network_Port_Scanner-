from fastapi import APIRouter
import socket
from typing import List
from api.history import add_scan
router = APIRouter()
from core.scanner import PortScanner

scanner = PortScanner()
open_ports = scanner.scan_range(host, start_port, end_port)
def scan_port(host: str, port: int) -> bool:
    """
    Check if a single port is open
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False


def scan_ports(host: str, ports: List[int]) -> List[int]:
    """
    Scan multiple ports and return open ones
    """
    open_ports = []

    for port in ports:
        if scan_port(host, port):
            open_ports.append(port)

    return open_ports


@router.get("/scan")
def scan(host: str, start_port: int = 1, end_port: int = 1024):
    """
    API endpoint to scan ports
    Example: /scan?host=example.com&start_port=1&end_port=100
    """
    ports = list(range(start_port, end_port + 1))
    open_ports = scan_ports(host, ports)

    return {
        "host": host,
        "open_ports": open_ports,
        "total_scanned": len(ports)
    }