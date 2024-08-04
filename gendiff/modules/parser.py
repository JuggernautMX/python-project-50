import json
import yaml


def get_dict(string, extension):
    if extension == '.json':
        return json.loads(string)
    elif extension in ['.yaml', '.yml']:
        return yaml.safe_load(string)
    else:
        raise TypeError('Wrong extension!')
