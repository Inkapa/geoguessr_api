from dataclasses import dataclass
from dataclass_wizard import JSONWizard

from models.maps.identity import Map
from models.user.identity import BaseUser


@dataclass
class ChallengeGame(JSONWizard):
    token: str
    map_slug: str
    round_count: int
    time_limit: int
    forbid_moving: bool
    forbid_zooming: bool
    forbid_rotating: bool
    number_of_participants: int
    game_mode: str  # TODO: possible enum
    challenge_type: int
    streak_type: str  # TODO: possible enum

@dataclass
class Challenge(ChallengeGame):
    map: Map
    creator: BaseUser
