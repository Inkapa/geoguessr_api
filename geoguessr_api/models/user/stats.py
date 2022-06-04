from dataclasses import dataclass
from typing import Optional, List, Union
from dataclass_wizard import JSONWizard
from .progress import Rank, LifeTimeXpProgression
from ..utils import Distance


@dataclass
class StreakRecord:
    max_streak: int
    max_streak_date: str
    streak_type: Optional[str] = None


@dataclass
class GameStats:
    streak: int
    num_games_played: int
    avg_position: Union[int, float]
    num_wins: int
    win_ratio: Union[int, float]
    num_guesses: int
    avg_correct_guesses: Optional[Union[int, float]] = None
    avg_guess_distance: Optional[int] = None


@dataclass
class GameScore:
    amount: int
    unit: str
    percentage: float


@dataclass
class MedalCount:
    medal_count_gold: int
    medal_count_silver: int
    medal_count_bronze: int


@dataclass
class BattleRoyaleStats:
    games_played: int
    wins: int
    average_position: float


@dataclass
class ListBase(JSONWizard):
    key: str
    value: int


@dataclass
class BattleRoyaleList(ListBase):
    value: BattleRoyaleStats


@dataclass
class StreakRecordList(ListBase):
    value: StreakRecord


@dataclass
class UserStats(JSONWizard):
    games_played: int
    rounds_played: int
    max_game_score: GameScore
    average_game_score: GameScore
    max_round_score: GameScore
    streak_games_played: int
    closest_distance: Distance
    average_distance: Distance
    average_time: str
    timed_out_guesses: int
    battle_royale_stats: List[BattleRoyaleList]
    daily_challenge_streak: int
    daily_challenge_current_streak: int
    daily_challenge_medal: int
    daily_challenges_rolling_7_days: Optional[List] = None
    streak_medals: Optional[List[ListBase]] = None
    streak_records: Optional[List[StreakRecordList]] = None


@dataclass
class UserExtendedStats(UserStats):
    battle_royale_rank: Optional[Rank] = None
    battle_royale_distance: Optional[GameStats] = None
    battle_royale_country: Optional[GameStats] = None
    battle_royale_medals: Optional[MedalCount] = None
    competitive_city_streaks: Optional[GameStats] = None
    competitive_streaks_rank: Optional[Rank] = None
    competitive_streaks_medals: Optional[MedalCount] = None
    duels: Optional[GameStats] = None
    duels_rank: Optional[Rank] = None
    duels_medals: Optional[MedalCount] = None
    life_time_xp_progression: Optional[LifeTimeXpProgression] = None
    total_medals: Optional[MedalCount] = None
