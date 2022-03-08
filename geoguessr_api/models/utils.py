from dataclasses import dataclass


@dataclass
class Unit:
    amount: float
    unit: str


@dataclass
class Distance:
    meters: Unit
    miles: Unit


@dataclass
class BoundsCoords:
    lat: float
    lng: float
