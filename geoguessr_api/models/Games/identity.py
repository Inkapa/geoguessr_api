from dataclasses import dataclass, field
from typing import Optional, List, Any
from dataclass_wizard import JSONWizard, json_field
from ..user.identity import BaseUser
from ..enums import GameType


@dataclass
class GameOptions:
    initial_health: int
    round_time: int
    forbid_moving: bool
    forbid_zooming: bool
    forbid_rotating: bool
    map_slug: str
    disable_multipliers: bool
    disable_healing: bool


@dataclass
class Game(JSONWizard):
    game_lobby_id: str
    title: str
    type: str
    game_type: GameType
    num_players_joined: int
    total_spots: int
    num_open_spots: int
    min_players_required: int
    player_ids: List[str]
    players: List[BaseUser]
    visibility: str  # Maybe Enum later
    time_stamp: str
    owner: str
    is_auto_started: bool
    can_be_started_manually: bool
    is_rated: bool
    competition_id: str
    game_options: GameOptions
    created_at: str
    share_link: str
    host_participate: bool
    closing_time: Optional[Any] = None
    host: Optional[Any] = None  # Probably BaseUser
    party_id: Optional[str] = None
    group_event_id: Optional[str] = None
    teams: Optional[List[Any]] = None
