from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "issues.json"


def load_data():
    """Load persisted issues; return an empty list if nothing is stored yet."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if content.strip():  # non-empty file
                return json.loads(content)
    # File missing or empty
    return []


def save_data(data):
    """Create a storage if it doesnt exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
