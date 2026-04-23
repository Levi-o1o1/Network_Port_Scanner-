from fastapi import APIRouter
from datetime import datetime
import json
import os

router = APIRouter()

HISTORY_FILE = "scan_history.json"


def load_history():
    """
    Load scan history from file
    """
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_history(data):
    """
    Save scan history to file
    """
    with open(HISTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_scan(host: str, open_ports: list, total_scanned: int):
    """
    Add a new scan record
    """
    history = load_history()

    record = {
        "host": host,
        "open_ports": open_ports,
        "total_scanned": total_scanned,
        "timestamp": datetime.now().isoformat()
    }

    history.append(record)
    save_history(history)


@router.get("/history")
def get_history():
    """
    Get all scan history
    """
    return {
        "history": load_history()
    }


@router.delete("/history")
def clear_history():
    """
    Clear all history
    """
    save_history([])
    return {"message": "History cleared"}