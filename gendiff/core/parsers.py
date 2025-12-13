import json
from pathlib import Path

import yaml


def parse_file(filepath):
    path = Path(filepath)
    ext = path.suffix.lower()
    with path.open() as f:
        if ext in ('.yml', '.yaml'):
            return yaml.safe_load(f)
        if ext == '.json':
            return json.load(f)
