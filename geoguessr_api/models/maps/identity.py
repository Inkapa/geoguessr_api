from dataclasses import dataclass
from typing import Any, Optional

from dataclass_wizard import JSONWizard

from models.user.identity import BaseUser
from models.utils import BoundsCoords


@dataclass
class Images:
    incomplete: bool
    background_large: Optional[str] = None


@dataclass
class Bounds:
    min: BoundsCoords
    max: BoundsCoords


@dataclass
class Avatar:
    background: str
    decoration: str
    ground: str
    landscape: str


@dataclass
class ExplorerMaps(JSONWizard):
    id: str
    slug: str
    name: str
    country_code: str


@dataclass
class ExploredMaps(ExplorerMaps):
    best_score: int
    medal: Optional[str] = None


@dataclass
class Map(JSONWizard):
    id: str
    name: str
    slug: str
    description: str
    url: str
    play_url: str
    published: bool
    banned: bool
    images: Images
    bounds: Bounds
    custom_coordinates: Any
    coordinate_count: str
    regions: Any
    created_at: str
    updated_at: str
    num_finished_games: int
    # liked_by_user: Optional[bool]
    average_score: int
    difficulty: str
    difficulty_level: int
    # highscore: None
    is_user_map: bool
    highlighted: bool
    free: bool
    in_explorer_mode: bool
    max_error_distance: int
    likes: int
    creator: Optional[BaseUser] = None
    avatar: Optional[Avatar] = None

