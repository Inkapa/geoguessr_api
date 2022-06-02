import random
from typing import Union

import httpx

from models.achievements import Achievements, Badge
from models.events import Event, CompetitionResult
from models.maps.identity import Map, ExplorerMaps, ExploredMaps
from models.maps.search import SearchMap
from models.subscription import Subscription, Invoice
from models.user.identity import Me, BaseUser, UserMinified, UserHighscores
from models.user.stats import UserExtendedStats
from models.enums import Method, FriendStatus, SearchOption, MapBrowseOption, BadgeFetchType
from .exceptions import Forbidden, NotFound, GeoguessrException, BadRequest
from .endpoints import API


class AsyncClient:
    """
    An async/sync client for geoguessr that lets you access the private web api
    """

    def __init__(
            self,
            email: str,
            password: str,
            token: str = None,
            timeout: float = 30.0,
            **options
    ):
        # self.loop = options.get('loop', asyncio.get_event_loop()) if self.is_async else None
        # self.connector = options.get('connector')

        self.me = None
        self.debug = options.get('debug', False)

        self.timeout = timeout
        self.api = API()
        self.email = email
        self.password = password
        self.token = token

        # Request/response headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'www.geoguessr.com',
            'Origin': 'https://www.geoguessr.com',
            'X-Client': 'web'
        }
        # TODO: Make sure accepted encodings are safe.

    async def __aenter__(self):
        self.session = httpx.AsyncClient(headers=self.headers)
        if self.token is None:
            await self.__login()
        await self.refresh_profile()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.aclose()

    @staticmethod
    async def get_profile_url(user: Union[BaseUser, UserMinified], w: int = 144, h: int = 144):
        if user.pin.is_default:
            colour = random.choice(['pink', 'yellow', 'light-blue', 'brown', 'purple', 'orange', 'blue', 'green'])
            return f"https://www.geoguessr.com/static/avatars/images/{colour}.svg"
        else:
            return f"https://www.geoguessr.com/images/auto/{w}/{h}/ce/0/plain/{user.pin.url}"

    async def __login(self):
        login = await self.session.post(url=self.api.SIGNIN, json={'email': self.email, 'password': self.password})
        if login.status_code == 200:
            self.token = login.cookies.get('_ncfa')
        elif login.status_code == 401:
            raise Forbidden(401, login.url, login.json().get('message'))

    async def request(self,
                      method: Method,
                      first_try: bool = True,
                      exception: GeoguessrException = None,
                      return_json: bool = True,
                      **kwargs) -> Union[httpx.Response, dict, list[dict]]:
        request = await self.session.request(
            method=method,
            timeout=self.timeout,
            cookies={'_ncfa': self.token},
            **kwargs)

        if exception and exception.code == request.status_code:
            raise exception
        elif request.status_code == 401 and first_try:
            await self.__login()
            await self.request(method=method, first_try=False, **kwargs)
        elif request.status_code == 401 and not first_try:
            raise Forbidden(401, request.url, request.json().get('message'))
        elif request.status_code == 404:
            raise NotFound(404, request.url, request.json().get('message'))
        else:
            return request.json() if return_json else request  # TODO: Handle 5xx and other 4xx

    async def refresh_profile(self):
        profile_info = await self.request(method=Method.GET, url=self.api.PROFILES)
        updated_data = {
            **profile_info.get('user'),
            'playingRestriction': profile_info.get('playingRestriction'),
            'email': {
                'address': profile_info.get('email'),
                'isEmailChangeable': profile_info.get('isEmailChangeable'),
                'isEmailVerified': profile_info.get('isEmailVerified')
            },
            'isBanned': profile_info.get('isBanned')
        }
        self.me = Me.from_dict(updated_data)
        return self.me

    async def get_stats(self, user: Union[str, BaseUser, UserMinified] = None):
        if user:
            slug = user if isinstance(user, str) else user.id
            stats = await self.request(method=Method.GET, url=f"{self.api.BASE}{self.api.USERS}/{slug}/stats")
            extended_stats = await self.request(method=Method.GET, url=f"{self.api.EXTENDED_STATS_USER}/{slug}")
        else:
            stats = await self.request(method=Method.GET, url=self.api.STATS)
            extended_stats = await self.request(method=Method.GET, url=f"{self.api.EXTENDED_STATS}/me")
        return UserExtendedStats.from_dict({**stats, **extended_stats})

    async def friendship_status(self, user: Union[str, BaseUser, UserMinified]):
        slug = user if isinstance(user, str) else user.id
        friend_stats = await self.request(method=Method.GET, url=f"{self.api.FRIENDS}/{slug}")
        return FriendStatus(friend_stats)

    async def add_friend(self, user: Union[str, BaseUser, UserMinified]):
        slug = user if isinstance(user, str) else user.id
        exception = BadRequest(400, f"{self.api.FRIENDS}/{slug}", "The requested user is invalid or already has a "
                                                                  "pending friend request from your account.")
        await self.request(method=Method.POST, exception=exception, url=f"{self.api.FRIENDS}/{slug}")

    async def accept_friend(self, user: Union[str, BaseUser, UserMinified]):
        slug = user if isinstance(user, str) else user.id
        await self.request(method=Method.PUT, url=f"{self.api.FRIENDS}/{slug}")

    async def remove_friend(self, user: Union[str, BaseUser, UserMinified]):
        slug = user if isinstance(user, str) else user.id
        await self.request(method=Method.DELETE, url=f"{self.api.FRIENDS}/{slug}")

    async def list_friends(self, count: int = None, page: int = None):
        query = {'count': count, 'page': page}
        friends = await self.request(method=Method.GET, url=self.api.FRIENDS, params=query)
        return UserMinified.from_list(friends)

    async def pending_friend_requests(self):
        friends = await self.request(method=Method.GET, url=self.api.PENDING_FRIENDS)
        return UserMinified.from_list(friends)

    async def search(self, query: str, search_type: SearchOption, count: int = None, page: int = None):
        query = {'q': query, 'count': count, 'page': page}
        if search_type == SearchOption.USER:
            users = await self.request(method=Method.GET, url=self.api.SEARCH_USER, params=query)
            users_sorted = sorted(users, key=lambda user: user.get('id'))
            return UserMinified.from_list(users_sorted)
        elif search_type == SearchOption.MAP:
            maps = await self.request(method=Method.GET, url=self.api.SEARCH_MAP, params=query)
            maps_sorted = sorted(maps, key=lambda map_item: map_item.get('id'))
            return SearchMap.from_list(maps_sorted)
        elif search_type == SearchOption.ANY:  # TODO: Differentiate UserMinified from Map
            data = await self.request(method=Method.GET, url=self.api.SEARCH_ANY, params=query)
            data_sorted = sorted(data, key=lambda item: item.get('id'))
            result_list = []
            for result in data_sorted:
                if result.get('type') == 1:
                    result_list.append(SearchMap.from_dict(result))
                else:
                    result_list.append(UserMinified.from_dict(result))
            return result_list

    async def get_user(self, user: Union[str, UserMinified]):
        slug = user if isinstance(user, str) else user.id
        profile = await self.request(method=Method.GET, url=f"{self.api.BASE}{self.api.USERS}/{slug}")
        return BaseUser.from_dict(profile)

    async def get_subscription(self):
        try:
            subscription = await self.request(method=Method.GET, url=f"{self.api.BASE}{self.api.SUBSCRIPTIONS}")
        except NotFound:
            return None
        return Subscription.from_dict(subscription)

    async def get_badges(self,
                         type: BadgeFetchType = BadgeFetchType.OBTAINED,
                         user: Union[str, BaseUser, UserMinified] = None):
        if type == BadgeFetchType.CLIENT_RECENT:
            badges = await self.request(method=Method.GET, url=self.api.RECENT_BADGES)
            return Achievements.from_dict(badges)
        elif user and type == BadgeFetchType.OBTAINED:
            slug = user if isinstance(user, str) else user.id
            all_badges = await self.request(method=Method.GET, url=f"{self.api.BADGES}/{slug}")
            obtained_badges = []
            for badge in all_badges:
                if badge.get('awarded') != "0001-01-01T00:00:00":
                    obtained_badges.append(Badge.from_dict(badge))
            return obtained_badges
        elif user and type == BadgeFetchType.ALL:
            slug = user if isinstance(user, str) else user.id
            all_badges = await self.request(method=Method.GET, url=f"{self.api.BADGES}/{slug}")
            return Badge.from_list(all_badges)
        else:
            raise ValueError(
                "When fetching OBTAINED or ALL badges you must also declare a `user` argument corresponding to the "
                "user from whom you want to fetch the badges."
            )

    async def get_map(self, map: Union[str, SearchMap, Map, ExplorerMaps]):
        slug = map if isinstance(map, str) else map.slug
        map_info = await self.request(method=Method.GET, url=f"{self.api.COUNTRY_MAPS}/{slug}")
        return Map.from_dict(map_info)

    async def browse_maps(self,
                          browse_type: MapBrowseOption = MapBrowseOption.PERSONALIZED,
                          reference_map_id: Union[str, SearchMap, Map, ExplorerMaps] = None,
                          count: int = None,
                          page: int = None):
        query = {'count': count, 'page': page}
        if reference_map_id:
            slug = reference_map_id if isinstance(reference_map_id, str) else reference_map_id.id

            query['mapId'] = slug
            maps = await self.request(method=Method.GET, url=f"{self.api.MAPS_BROWSE}/recommended", params=query)

        elif browse_type == MapBrowseOption.OFFICIAL:
            maps = await self.request(method=Method.GET, url=f"{self.api.MAPS_POPULAR}/official", params=query)

        elif browse_type == MapBrowseOption.PERSONALIZED:
            map = await self.request(method=Method.GET, url=f"{self.api.MAPS_BROWSE}/personalized", params=query)
            return Map.from_dict(map)

        elif browse_type == MapBrowseOption.POPULAR_MONTH:
            maps = await self.request(method=Method.GET, url=f"{self.api.MAPS_POPULAR}/month", params=query)

        elif browse_type == MapBrowseOption.POPULAR_RANDOM:
            maps = await self.request(method=Method.GET, url=f"{self.api.MAPS_POPULAR}/random", params=query)

        elif browse_type == MapBrowseOption.POPULAR_ALL_TIME:
            maps = await self.request(method=Method.GET, url=f"{self.api.MAPS_POPULAR}/all", params=query)

        elif browse_type == MapBrowseOption.FEATURED:
            maps = await self.request(method=Method.GET, url=f"{self.api.MAPS_BROWSE}/featured", params=query)

        elif browse_type == MapBrowseOption.LIKED:
            maps = await self.request(method=Method.GET, url=self.api.LIKES, params=query)

        elif browse_type == MapBrowseOption.CREATED:
            maps = await self.request(method=Method.GET, url=self.api.CREATED_MAPS, params=query)

        elif browse_type == MapBrowseOption.NEW:
            maps = await self.request(method=Method.GET, url=f"{self.api.MAPS_BROWSE}/new", params=query)

        elif browse_type == MapBrowseOption.ALL_COUNTRIES:
            maps = await self.request(method=Method.GET, url=self.api.COUNTRY_MAPS)

        else:
            # TODO: Handle impossible event through exception?
            return None
        return Map.from_list(maps) if maps else None

    async def browse_maps_by_user(self,
                                  user: Union[str, BaseUser, UserMinified],
                                  count: int = None,
                                  page: int = None):
        slug = user if isinstance(user, str) else user.id
        query = {'createdBy': slug, 'count': count, 'page': page}
        maps = await self.request(method=Method.GET, url=self.api.COUNTRY_MAPS, params=query)
        return Map.from_list(maps) if maps else None

    async def is_map_liked(self, map: Union[str, SearchMap, Map, ExplorerMaps]):
        slug = map if isinstance(map, str) else map.id
        exception = BadRequest(400, f"{self.api.LIKES}/{slug}", "The requested map is invalid and could not be found.")
        is_liked = await self.request(method=Method.GET, url=f"{self.api.LIKES}/{slug}", exception=exception)
        return bool(is_liked)

    async def like_map(self, map: Union[str, SearchMap, Map, ExplorerMaps]):
        slug = map if isinstance(map, str) else map.id
        exception = BadRequest(400, f"{self.api.LIKES}/{slug}", "The requested map is invalid and could not be found.")
        like_message = await self.request(method=Method.POST, url=f"{self.api.LIKES}/{slug}", exception=exception)
        return like_message.get('message')

    async def unlike_map(self, map: Union[str, SearchMap, Map, ExplorerMaps]):
        slug = map if isinstance(map, str) else map.id
        exception = BadRequest(400, f"{self.api.LIKES}/{slug}", "The requested map is invalid and could not be found.")
        await self.request(method=Method.DELETE, url=f"{self.api.LIKES}/{slug}", exception=exception)

    async def get_map_highscores(self, map: Union[str, SearchMap, Map, ExplorerMaps]):
        slug = map if isinstance(map, str) else map.id
        highscores = await self.request(method=Method.GET, url=f"{self.api.SCORES}/{slug}")
        return UserHighscores.from_dict(highscores)

    async def get_explorer(self):
        maps = await self.request(method=Method.GET, url=self.api.EXPLORER)
        return ExplorerMaps.from_list(maps)

    async def get_explored_countries(self, user: Union[str, BaseUser, UserMinified] = None):
        all_countries = await self.request(method=Method.GET, url=self.api.EXPLORER)
        if not user:
            maps = await self.request(method=Method.GET, url=self.api.EXPLORED)
        else:
            slug = user if isinstance(user, str) else user.id
            maps = await self.request(method=Method.GET, url=f"{self.api.EXPLORED_BY_USER}/{slug}")
        explored_countries = []
        for country, value in maps.items():
            matching_country = next(obj for obj in all_countries if obj.get('slug') == country)
            explored_country = ExploredMaps.from_dict({**matching_country, **value})
            explored_countries.append(explored_country)
        return explored_countries if explored_countries else None

    async def publish_map(self, map: Union[str, SearchMap, Map, ExplorerMaps]):
        slug = map if isinstance(map, str) else map.slug
        map = await self.request(method=Method.POST, url=f"{self.api.CREATED_MAPS}/{slug}", json={'published': True})
        return Map.from_dict(map)

    async def unpublish_map(self, map: Union[str, SearchMap, Map, ExplorerMaps]):
        slug = map if isinstance(map, str) else map.slug
        map = await self.request(method=Method.POST, url=f"{self.api.CREATED_MAPS}/{slug}", json={'published': False})
        return Map.from_dict(map)

    async def get_invoices(self):
        invoices = await self.request(method=Method.GET, url=self.api.INVOICES)
        return Invoice.from_list(invoices) if invoices else None

    async def get_events(self):
        competitions = await self.request(method=Method.GET, url=self.api.EVENTS)
        return Event.from_list(competitions.get('competitions'))

    async def get_event_results(self, event: Union[str, Event]):
        slug = event if isinstance(event, str) else event.id
        results = await self.request(method=Method.GET, url=f"{self.api.EVENTS}/{slug}")
        return CompetitionResult.from_dict(results.get('competitionResult'))

