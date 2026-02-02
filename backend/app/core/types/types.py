from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class RetrievedChunk:
    text: str
    metadata: Dict[str, Any]
    id: str
    distance: Optional[float]
    citation: str
