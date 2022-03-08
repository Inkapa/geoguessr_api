from dataclasses import dataclass
from typing import List, Optional
from dataclass_wizard import JSONWizard


@dataclass
class Badge(JSONWizard):
    id: str
    name: str
    hint: str
    image_path: str
    has_levels: bool
    level: int
    awarded: str
    description: Optional[str] = None


@dataclass
class Achievements(JSONWizard):
    totalMedals: int
    recentBadges: Optional[List[Badge]] = None
