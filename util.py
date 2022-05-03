from pathlib import Path
from json import dumps, loads
from typing import Any

class JSONDatabase():
    def __init__(self, name):
        self.name = name
        self.path = Path(name)

        if not self.path.exists():
            self.path.touch()

    def truncate(self):
        self.path.unlink()
        self.path.touch()

    def read(self) -> dict[str, Any]:
        return loads(self.path.read_text())

    def write(self, data):
        self.path.write_text(dumps(data))
