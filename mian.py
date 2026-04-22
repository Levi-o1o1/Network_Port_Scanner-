from fastapi import FastAPI
import socket

app = FastAPI()
def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip,port))
    sock.close()
    return result == 0
@app.get("/scan")
def scan(ip: str):
    ports =[21,22,80,443]
    results = {}
    for port in ports:
        results[port] = "OPEN" if scan_port(ip,port) else "CLOSED"
    return{"ip": ip, "scan_results": results}