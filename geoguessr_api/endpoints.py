class API:
    def __init__(self, version: int = 3):
        self.ROOT = "https://www.geoguessr.com/api"
        self.GAME_BASE = "https://game-server.geoguessr.com/api"
        self.BASE = self.ROOT + f"/v{version}"
        self.BASEV4 = f"https://www.geoguessr.com/api/v4"  # Waiting for main version to go to 4

        self.ACCOUNTS = "/accounts"
        self.USERS = "/users"
        self.SOCIAL = "/social"
        self.SEARCH = "/search"
        self.SUBSCRIPTIONS = "/subscriptions"

        self.LOBBY = self.GAME_BASE + '/lobby'
        self.COUNTRY_MAPS = self.ROOT + "/maps"
        self.EXPLORED = self.BASE + "/explorer"
        self.LIKES = self.BASE + "/likes"
        self.PROFILES = self.BASE + "/profiles"
        self.SCORES = self.BASE + "/scores"
        self.CHALLENGES = self.BASE + "/challenges"
        self.EXTENDED_STATS = self.BASEV4 + "/stats"
        self.SEASONS = self.BASEV4 + "/seasons"

        self.JOIN_RANDOM = self.LOBBY + '/join-random'  # TODO: Duels
        self.EVENTS = self.BASE + "/competitions"
        self.EXPLORER = self.COUNTRY_MAPS + "/explorer"
        self.SIGNIN = self.BASE + self.ACCOUNTS + "/signin"
        self.FRIENDS = self.BASE + self.SOCIAL + "/friends"
        self.SEARCH_USER = self.BASE + self.SEARCH + "/user"
        self.SEARCH_MAP = self.BASE + self.SEARCH + "/map"
        self.SEARCH_ANY = self.BASE + self.SEARCH + "/any"
        self.MAPS = self.BASE + self.SOCIAL + "/maps"
        self.BADGES = self.BASE + self.SOCIAL + "/badges"
        self.INVOICES = self.BASE + self.SUBSCRIPTIONS + "/invoices"
        self.RATINGS = self.BASE + self.USERS + "/ratings"

        self.EXPLORED_BY_USER = self.EXPLORED + "/user"
        self.EXTENDED_STATS_USER = self.EXTENDED_STATS + self.USERS
        self.ME = self.PROFILES + "/me"
        self.STATS = self.PROFILES + "/stats"
        self.PENDING_FRIENDS = self.FRIENDS + "/received"
        self.RECENT_BADGES = self.PROFILES + "/achievements"
        self.MAPS_BROWSE = self.MAPS + "/browse"
        self.CREATED_MAPS = self.PROFILES + "/maps"

        self.MAPS_POPULAR = self.MAPS_BROWSE + "/popular"

