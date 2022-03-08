import random
from typing import Union

from lxml import html
import orjson
from .models.user.identity import BaseUser, UserMinified


class Objectify(dict):
    """ Dictionary subclass whose entries can be accessed by attributes
        (as well as normally).
    """

    def __init__(self, *args, **kwargs):
        def from_nested_dict(data):
            """ Construct nested AttrDicts from nested dictionaries. """
            if not isinstance(data, dict):
                return data
            else:
                return Objectify({key: from_nested_dict(data[key])
                                 for key in data})

        super(Objectify, self).__init__(*args, **kwargs)
        self.__dict__ = self

        for key in self.keys():
            self[key] = from_nested_dict(self[key])


def get_json(webpage: str):
    root = html.fromstring(webpage)
    data = root.xpath('//*[@id="__NEXT_DATA__"]/text()')[0]
    return orjson.loads(data)



