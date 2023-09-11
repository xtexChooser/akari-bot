import os
from os.path import abspath

import toml

from core.exceptions import ConfigFileNotFound

config_filename = 'config.toml'
config_path = abspath('./config/' + config_filename)

old_cfg_file_path = abspath('./config/config.cfg')


def convert_cfg_to_toml():
    import configparser
    config = configparser.ConfigParser()
    config.read(old_cfg_file_path)
    config_dict = {}
    for section in config.sections():
        config_dict[section] = dict(config[section])

    for x in config_dict:
        for y in config_dict[x]:
            if config_dict[x][y] == "True":
                config_dict[x][y] = True
            elif config_dict[x][y] == "False":
                config_dict[x][y] = False
            elif config_dict[x][y].isdigit():
                config_dict[x][y] = int(config_dict[x][y])

    with open(config_path, 'w') as f:
        f.write(toml.dumps(config_dict))
    os.remove(old_cfg_file_path)


class CFG:
    value = None
    _ts = None

    @classmethod
    def load(cls):
        if not os.path.exists(config_path):
            if os.path.exists(old_cfg_file_path):
                convert_cfg_to_toml()
            else:
                raise ConfigFileNotFound(config_path) from None
        cls.value = toml.loads(open(config_path, 'r', encoding='utf-8').read())
        cls._ts = os.path.getmtime(config_path)

    @classmethod
    def get(cls, q):
        q = q.lower()
        if os.path.getmtime(config_path) != cls._ts:
            cls.load()
        value_s = cls.value.get('secret')
        value_n = cls.value.get('cfg')
        value = value_s.get(q)
        if value is None:
            value = value_n.get(q)
        return value

    @classmethod
    def write(cls, q, value, secret=False):
        q = q.lower()
        if os.path.getmtime(config_path) != cls._ts:
            cls.load()
        value_s = cls.value.get('secret')
        value_n = cls.value.get('cfg')
        if q in value_s:
            value_s[q] = value
        elif q in value_n:
            value_n[q] = value
        else:
            if secret:
                value_s[q] = value
            else:
                value_n[q] = value
        cls.value['secret'] = value_s
        cls.value['cfg'] = value_n
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(toml.dumps(cls.value))
        cls.load()

    @classmethod
    def delete(cls, q):
        q = q.lower()
        if os.path.getmtime(config_path) != cls._ts:
            cls.load()
        value_s = cls.value.get('secret')
        value_n = cls.value.get('cfg')
        if q in value_s:
            del value_s[q]
        elif q in value_n:
            del value_n[q]
        else:
            return False
        cls.value['secret'] = value_s
        cls.value['cfg'] = value_n
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(toml.dumps(cls.value))
        cls.load()
        return True

    @classmethod
    def get_url(cls, q):
        q = cls.get(q)
        if q:
            if q[-1] != '/':
                q += '/'
        return q


CFG.load()
Config = CFG.get
