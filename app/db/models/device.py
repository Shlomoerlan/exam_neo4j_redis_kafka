from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Device:
    id_device: str
    name_owner: str
    type: str
    status: str
    seen_first: Optional[datetime] = None
    seen_last: Optional[datetime] = None