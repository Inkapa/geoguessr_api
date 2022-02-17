import httpx

from .models import User, Requests
from .exceptions import Forbidden
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
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.aclose()

    async def __login(self):
        login = await self.session.post(url=self.api.SIGNIN, json={'email': self.email, 'password': self.password})
        if login.status_code == 200:
            self.me = User(**login.json())
            self.token = login.cookies.get('_ncfa')
        elif login.status_code == 401:
            raise Forbidden(401, login.url, login.json()['message'])

    async def request(self, rtype: Requests, retry=False, **kwargs):
        if rtype == Requests.GET:
            request = await self.session.get(timeout=self.timeout, cookies={'_ncfa': self.token}, **kwargs)
        elif rtype == Requests.POST:
            request = await self.session.post(timeout=self.timeout, cookies={'_ncfa': self.token}, **kwargs)
        else:
            request = await self.session.head(timeout=self.timeout, cookies={'_ncfa': self.token}, **kwargs)

        if request.status_code == 401 and not retry:
            await self.__login()
            await self.request(rtype=rtype, retry=True, **kwargs)
        elif request.status_code == 401 and retry:
            raise Forbidden(401, request.url, request.json()['message'])
        else:
            return request  # TODO: Handle 5xx and other 4xx

    async def refresh_profile(self):
        profile_info = await self.request(rtype=Requests.GET, url=self.api.ME)
        self.me = User(**profile_info.json())
        return self.me
