from dataclasses import dataclass
from typing import Optional, List, Any, Union
from dataclass_wizard import JSONWizard
from ..user.identity import BaseUser
from ..enums import GameType


@dataclass
class GameBase:
    round_time: int
    forbid_moving: bool
    forbid_zooming: bool
    forbid_rotating: bool
    map_slug: str


@dataclass
class GameDuels(GameBase):
    initial_health: int
    disable_multipliers: bool
    disable_healing: bool


@dataclass
class GameDistance(GameBase):
    initial_lives: int


@dataclass
class GameCountries(GameDistance):
    power_up_5050: bool
    power_up_spy: bool


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
    visibility: str  # TODO: Maybe Enum later
    timestamp: str
    owner: str
    is_auto_started: bool
    can_be_started_manually: bool
    is_rated: bool
    competition_id: str
    game_options: Union[GameDistance, GameCountries, GameDuels]
    created_at: str
    share_link: str
    host_participate: bool
    closing_time: Optional[str] = None
    host: Optional[Any] = None  # Probably BaseUser
    party_id: Optional[str] = None
    group_event_id: Optional[str] = None
    teams: Optional[List[Any]] = None
