from dataclasses import dataclass
from typing import Optional

from dataclass_wizard import JSONWizard


@dataclass
class Streaks:
    br_countries: int
    br_distance: int
    cs_cities: int
    duels: int


@dataclass
class Division:
    id: int
    division_id: int
    tier_id: int
    name: Optional[str] = None
    minimum_rank: Optional[int] = None


@dataclass
class CompetitiveDivision:
    type: int
    start_rating: int
    end_rating: int


@dataclass
class Medals:
    bronze: Optional[int] = 0
    silver: Optional[int] = 0
    gold: Optional[int] = 0
    platinum: Optional[int] = 0


@dataclass
class Title:
    id: int
    tier_id: int
    name: Optional[str] = None
    minimum_level: Optional[int] = None


@dataclass
class Rank(JSONWizard):
    rating: int
    games_left_before_ranked: int
    division: Division
    rank: Optional[int] = None


@dataclass
class CompetitiveRank:
    elo: Optional[int] = None
    rating: Optional[int] = None
    last_ranking_change: Optional[int] = None
    division: Optional[CompetitiveDivision] = None


@dataclass
class Level:
    level: int
    xp_start: int


@dataclass
class Progress(JSONWizard):
    xp: int
    level: int
    level_xp: int
    next_level: int
    next_level_xp: int
    title: Title
    br_rank: Rank
    cs_rank: Rank
    duels_rank: Rank
    competition_medals: Medals
    streaks: Streaks


@dataclass
class LifeTimeXpProgression(JSONWizard):
    xp: int
    current_level: Level
    next_level: Level
    current_title: Title
