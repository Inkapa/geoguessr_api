from dataclasses import dataclass
from typing import Optional, Any
from dataclass_wizard import json_field, JSONWizard


@dataclass
class Ticket:
    is_ticket_active: bool
    active_ticket_ends_at: Any
    tickets_left: int
    duration_per_ticket: int
    ticket_wait_time: int
    next_ticket_unlocks_at: Any


@dataclass
class Allowance:
    gamesLeft: int
    interval: int
    next_ticket_unlocks_at: Any


@dataclass
class Restriction(JSONWizard):
    restriction: int
    can_play_game: bool
    description: str
    ticket: Optional[Ticket] = None
    allowance: Optional[Allowance] = json_field('periodicAllowanceMetadata', all=True, default=None)
