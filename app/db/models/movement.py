from dataclasses import dataclass
from datetime import datetime


@dataclass
class Movement:
    timestamp: datetime
    duration: float
    level_confidence: float
    type_movement: str
