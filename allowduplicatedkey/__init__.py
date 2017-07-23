import json
from collections import UserDict


class Key(str):
    def __hash__(self):
        return id(self)

    @property
    def value(self):
        return str(self)


class AllowDuplicatedKey(UserDict):
    """
    dictionary object allow for duplicated keys.
    """
    def __setitem__(self, key, value, **kwargs):
        key = Key(key)
        super().__setitem__(key, value)

    def __missing__(self, key):
        for item in self:
            if key == item.value:
                return super().__getitem__(item)
        raise KeyError(key)

    def _gen_keys(self, key):
        keys = (item for item in self if item.value == key)
        return keys

    def values_per_key(self, key):
        """
        return duplicated keys and values as dict
        :param key: str
        :return: dict
        """
        return {key: self[key] for key in self._gen_keys(key)}

    def as_json(self, key):
        """
        json base on key
        :param key: str
        :return: json based on key
        """
        return json.dumps(self.values_per_key(key), sort_keys=True, indent=4)

    def all_as_json(self):
        """
        dump as json.
        :return: json
        """
        return json.dumps(dict(self), sort_keys=True, indent=4)
