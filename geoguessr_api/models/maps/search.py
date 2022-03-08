from dataclasses import dataclass
from typing import Optional
from .identity import Avatar
from dataclass_wizard import JSONWizard


@dataclass
class SearchMap(JSONWizard):
    id: str
    name: str
    url: str
    likes: int
    creator_id: str
    creator: str
    updated: str
    is_verified: bool
    map_avatar: Optional[Avatar] = None
    image_url: Optional[str] = None

