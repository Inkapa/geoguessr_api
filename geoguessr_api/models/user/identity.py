from dataclasses import dataclass, field
from typing import Optional, List
from dataclass_wizard import JSONWizard, json_field
from .restriction import Restriction
from .progress import Progress, Medals, CompetitiveRank


@dataclass
class Br:
    level: int
    division: int
    streak: Optional[int]


@dataclass
class Pin:
    url: str
    anchor: str
    is_default: bool
    path: Optional[str] = None  # TODO: Remove?


@dataclass
class Onboarding:
    tutorial_token: Optional[str] = None
    tutorial_state: Optional[str] = None


@dataclass
class Email:
    address: str
    is_email_changeable: bool
    is_email_verified: bool

@dataclass
class UserMinified(JSONWizard):
    is_verified: bool = json_field('userIsVerified')
    id: str = json_field(('userId', 'playerId'))
    nick: str = json_field(('name', 'userNick'))
    url: str = json_field('userUrl', default=None)
    is_online: Optional[bool] = None
    pin: Optional[Pin] = None
    _image_url: Optional[str] = json_field(('imageUrl', 'userPin', 'avatarPath', 'avatar'), default=None)

    def __post_init__(self):
        if self.url is None:
            self.url = f'/user/{self.id}'
        if self._image_url and not self.pin:
            self.pin = Pin(url=self._image_url, anchor='center-center', is_default=False)
        elif not self._image_url and not self.pin:
            self.pin = Pin(url="", anchor='center-center', is_default=True)


# TODO: What was I trying to do here again?
# @dataclass
# class PlayerMinified(UserMinified):
#     level: int
#     title_tier_id: int
#     division: str
#     performance_streak: str
#     rank:
#     team: Optional[str] = None

@dataclass
class UserLeaderboardRanking(UserMinified):
    position: Optional[int] = 0
    rating: Optional[int] = 0

@dataclass
class UserSeasonRanking(UserMinified):
    position: Optional[int] = 0
    played: Optional[int] = 0
    points: Optional[int] = 0
    average_time: Optional[float] = 0.0
    first: Optional[int] = 0
    second: Optional[int] = 0
    third: Optional[int] = 0

@dataclass
class UserMinifiedHighScore(UserMinified):
    points: Optional[int] = 0
    total_time: Optional[int] = 0
    highlight: Optional[bool] = False
    on_highscore: Optional[bool] = False
    game_token: Optional[str] = None


@dataclass
class UserHighscores(JSONWizard):
    all: Optional[List[UserMinifiedHighScore]] = None
    friends: Optional[List[UserMinifiedHighScore]] = None


@dataclass
class BaseUser(JSONWizard):
    nick: str
    created: str
    is_pro_user: bool
    consumed_trial: bool
    is_verified: bool
    pin: Pin
    url: str
    id: str
    onboarding: Onboarding
    br: Br
    progress: Progress
    competitive: CompetitiveRank
    color: Optional[int] = 0
    country_code: Optional[str] = None
    streak_progress: Optional[Medals] = Medals()
    explorer_progress: Optional[Medals] = Medals()
    daily_challenge_progress: Optional[int] = None


@dataclass
class Me(BaseUser):
    email: Optional[Email] = None
    is_banned: Optional[bool] = None
    playing_restriction: Optional[Restriction] = None
