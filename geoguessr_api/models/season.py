from dataclasses import dataclass
from typing import List, Optional
from dataclass_wizard import JSONWizard


@dataclass
class Trophies:
    type: int  # TODO: possible enum
    context: int
    threshold_type: int  # TODO: possible enum
    threshold: int
    image_path: str


@dataclass
class Season(JSONWizard):
    id: str
    number: int
    name: str
    start_date: str
    end_date: str
    duration: int
    entry_cost: int
    minimum_number_of_duels: int
    minimum_number_of_br: int
    active_week: int
    active_day: int
    is_weekend: bool
    weekend_league_start: str
    weekend_league_end: str
    trophies: List[Trophies]
