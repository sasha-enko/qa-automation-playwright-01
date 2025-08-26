# src/utils/storage_state_args.py
from dataclasses import dataclass
from pathlib import Path



@dataclass
class StateArgs:
    storage_state: Path
    file_exists: bool = False


    def as_kwargs(self):
        if self.file_exists:
            return  {"storage_state": str(self.storage_state)}
        else:
            return {}
