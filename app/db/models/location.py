from dataclasses import dataclass
from typing import Optional


@dataclass
class Location:
    id_location: str
    type: str
    level_risk: int
    name: Optional[str] = None