from dataclasses import dataclass


@dataclass
class Country:
    id: str
    slug: str
    name: str
    country_code: str
    medal: int
