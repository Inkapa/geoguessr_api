from enum import Enum


class Method(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    HEAD = 'HEAD'
    DELETE = 'DELETE'

    def __str__(self):
        return self.value

    def upper(self):
        return self.value.upper()


class FriendStatus(Enum):
    NOT_FRIENDS = 0
    REQUEST_SENT = 1
    PENDING_APPROVAL = 2
    FRIENDS = 3


class SearchOption(Enum):
    MAP = 1
    USER = 2
    ANY = 3


class MapBrowseOption(Enum):
    OFFICIAL = 1
    PERSONALIZED = 2
    POPULAR_MONTH = 3
    POPULAR_RANDOM = 4
    POPULAR_ALL_TIME = 5
    FEATURED = 6
    LIKED = 7
    CREATED = 8
    NEW = 9
    ALL_COUNTRIES = 10


class BadgeFetchType(Enum):
    CLIENT_RECENT = 1
    OBTAINED = 2
    ALL = 3


class GameType(Enum):
    BATTLE_ROYALE__COUNTRIES = "BattleRoyaleCountries"
    BATTLE_ROYALE_DISTANCE = "BattleRoyaleDistance"
    DUELS = "Duels"
