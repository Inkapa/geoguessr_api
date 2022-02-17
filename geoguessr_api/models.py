from pydantic import BaseModel, Field, Extra
from typing import Optional, Any, List, Union
from enum import Enum


class Requests(Enum):
    GET = 1
    POST = 2
    HEAD = 3


class Pin(BaseModel):
    url: str
    anchor: str
    path: Optional[str]
    is_default: bool = Field(..., alias='isDefault')


class Onboarding(BaseModel):
    tutorial_token: Optional[str] = Field(None, alias='tutorialToken')
    tutorial_state: Optional[str] = Field(None, alias='tutorialState')


class Br(BaseModel):
    level: int
    division: int
    streak: Optional[int]


class Title(BaseModel):
    id: int
    tier_id: int = Field(..., alias='tierId')
    minimum_level: Optional[int] = Field(None, alias='minimumLevel')
    name: Optional[str]


class Division(BaseModel):
    id: int
    division_id: int = Field(..., alias='divisionId')
    tier_id: int = Field(..., alias='tierId')
    name: Optional[str]
    minimum_rank: Optional[int] = Field(None, alias='minimumRank')


class Rank(BaseModel):
    rank: Optional[int]
    rating: int
    games_left_before_ranked: int = Field(..., alias='gamesLeftBeforeRanked')
    division: Division


class Medals(BaseModel):
    bronze: Optional[int] = 0
    silver: Optional[int] = 0
    gold: Optional[int] = 0
    platinum: Optional[int] = 0


class Streaks(BaseModel):
    br_countries: int = Field(..., alias='brCountries')
    br_distance: int = Field(..., alias='brDistance')
    cs_cities: int = Field(..., alias='csCities')
    duels: int


class Progress(BaseModel):
    xp: int
    level: int
    level_xp: int = Field(..., alias='levelXp')
    next_level: int = Field(..., alias='nextLevel')
    next_level_xp: int = Field(..., alias='nextLevelXp')
    title: Title
    br_rank: Rank = Field(..., alias='brRank')
    cs_rank: Rank = Field(..., alias='csRank')
    duels_rank: Rank = Field(..., alias='duelsRank')
    competition_medals: Medals = Field(..., alias='competitionMedals')
    streaks: Streaks


class User(BaseModel):
    nick: str
    created: Optional[str]
    is_pro_user: bool = Field(..., alias='isProUser')
    consumed_trial: bool = Field(..., alias='consumedTrial')
    is_verified: bool = Field(..., alias='isVerified')
    pin: Pin
    color: Optional[int]
    url: str
    id: str = Field(..., alias='userId')
    country_code: Optional[str] = Field(None, alias='countryCode')
    onboarding: Onboarding
    br: Br
    streak_medals: Optional[Medals] = Field(Medals(), alias='streakMedals')  # TODO
    explorer_medals: Optional[Medals] = Field(Medals(), alias='explorerMedals')  # TODO
    daily_medal: Optional[str] = Field(None, alias='dailyMedal')  # TODO
    streak_progress: Optional[str] = Field(None, alias='streakProgress')
    explorer_progress: Optional[str] = Field(None, alias='explorerProgress')
    daily_challenge_progress: Optional[int] = Field(None, alias='dailyChallengeProgress')
    progress: Progress

    class Config:
        allow_population_by_field_name = True
        extra = Extra.allow


class BattleRoyaleStat(BaseModel):
    game_type: str = Field(..., alias='gameType')
    battle_royale_games_played: int = Field(..., alias='battleRoyaleGamesPlayed')
    battle_royale_wins: int = Field(..., alias='battleRoyaleWins')
    battle_royale_average: Union[int, float] = Field(..., alias='battleRoyaleAverage')


class StreakMedal(BaseModel):
    name: str
    medal: str


class StreakRecord(BaseModel):
    streak_type: str = Field(..., alias='streakType')
    max_streak: int = Field(..., alias='maxStreak')
    max_streak_date: str = Field(..., alias='maxStreakDate')


class UserStats(BaseModel):
    games_played: int = Field(..., alias='gamesPlayed')
    rounds_played: int = Field(..., alias='roundsPlayed')
    max_round_score: int = Field(..., alias='maxRoundScore')
    average_game_score: int = Field(..., alias='averageGameScore')
    max_game_score: int = Field(..., alias='maxGameScore')
    battle_royale_stats: List[BattleRoyaleStat] = Field(..., alias='battleRoyaleStats')
    daily_challenge_medal: str = Field(..., alias='dailyChallengeMedal')
    daily_challenge_streak: int = Field(..., alias='dailyChallengeStreak')
    daily_challenge_current_streak: int = Field(
        ..., alias='dailyChallengeCurrentStreak'
    )
    daily_challenge_games: List = Field(..., alias='dailyChallengeGames')
    daily_challenge_average: int = Field(..., alias='dailyChallengeAverage')
    streak_games_played: int = Field(..., alias='streakGamesPlayed')
    streak_medals: List[Optional[StreakMedal]] = Field(None, alias='streakMedals')
    streak_records: List[Optional[StreakRecord]] = Field(None, alias='streakRecords')


class GameStats(BaseModel):
    num_games_played: int = Field(..., alias='numGamesPlayed')
    avg_position: Union[int, float] = Field(..., alias='avgPosition')
    num_wins: int = Field(..., alias='numWins')
    win_ratio: Union[int, float] = Field(..., alias='winRatio')
    num_guesses: int = Field(..., alias='numGuesses')
    avg_correct_guesses: Optional[Union[int, float]] = Field(None, alias='avgCorrectGuesses')
    avg_guess_distance: Optional[int] = Field(None, alias='avgGuessDistance')
    streak: int


class MedalCount(BaseModel):
    medal_count_gold: int = Field(..., alias='medalCountGold')
    medal_count_silver: int = Field(..., alias='medalCountSilver')
    medal_count_bronze: int = Field(..., alias='medalCountBronze')


class Level(BaseModel):
    level: int
    xp_start: int = Field(..., alias='xpStart')


class LifeTimeXpProgression(BaseModel):
    xp: int
    current_level: Level = Field(..., alias='currentLevel')
    next_level: Level = Field(..., alias='nextLevel')
    current_title: Title = Field(..., alias='currentTitle')


class UserExtendedStats(BaseModel):
    battle_royale_rank: Rank = Field(..., alias='battleRoyaleRank')
    battle_royale_distance: GameStats = Field(
        ..., alias='battleRoyaleDistance'
    )
    battle_royale_country: GameStats = Field(..., alias='battleRoyaleCountry')
    battle_royale_medals: MedalCount = Field(..., alias='battleRoyaleMedals')
    competitive_city_streaks: GameStats = Field(
        ..., alias='competitiveCityStreaks'
    )
    competitive_streaks_rank: Rank = Field(
        ..., alias='competitiveStreaksRank'
    )
    competitive_streaks_medals: MedalCount = Field(
        ..., alias='competitiveStreaksMedals'
    )
    duels: GameStats
    duels_rank: Rank = Field(..., alias='duelsRank')
    duels_medals: MedalCount = Field(..., alias='duelsMedals')
    life_time_xp_progression: LifeTimeXpProgression = Field(
        ..., alias='lifeTimeXpProgression'
    )
    total_medals: MedalCount = Field(..., alias='totalMedals')


class Country(BaseModel):
    id: str
    slug: str
    name: str
    country_code: str = Field(..., alias='countryCode')
    medal: int
