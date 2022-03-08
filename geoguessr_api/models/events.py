from dataclasses import dataclass
from typing import List, Optional
from dataclass_wizard import JSONWizard

from models.maps.identity import Map


@dataclass
class Settings:
    forbid_moving: bool
    forbid_zooming: bool
    forbid_rotating: bool
    initial_health: Optional[int] = None
    round_time: Optional[int] = None
    map_slug: Optional[str] = None
    duel_round_options: Optional[str] = None
    initial_lives: Optional[int] = None
    reservation_window_time: Optional[int] = None
    power_ups: Optional[List] = None
    reset_lives_each_round: Optional[bool] = None
    extra_lives_each_round: Optional[int] = None
    guess_cooldown: Optional[int] = None
    duration: Optional[int] = None
    round_interval: Optional[int] = None
    lives: Optional[int] = None
    max_lives: Optional[int] = None
    lifebonus_frequency: Optional[int] = None
    lifebonus_amount_min: Optional[int] = None
    lifebonus_amount_max: Optional[int] = None
    checkpoint_frequency: Optional[int] = None
    checkpoint_life_refill_amount: Optional[int] = None
    initial_alternatives: Optional[int] = None
    alternatives_increase_per_round: Optional[int] = None


@dataclass
class CompetitionResult(JSONWizard):
    user_medal: str
    position: int
    played_at: str
    competition_id: Optional[str] = None
    user_id: Optional[str] = None


@dataclass
class Event(JSONWizard):
    id: str
    name: str
    description: str
    type: str
    start_type: str
    start_date: str
    end_date: str
    is_published: bool
    difficulty: str
    did_participate: bool
    medal: str
    map: Map
    # competition_result: CompetitionResult
    # tags: Optional[List] = None
    settings: Optional[Settings] = None


