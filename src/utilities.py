import json


def load_json_file(filepath: str) -> tuple:
    with open(filepath) as json_file:
        data = json.load(json_file)

    required = ['n', 'flights', 'src', 'dst', 'k']

    for key in required:
        if key not in data:
            raise KeyError(f'Required key {key} not found in {filepath}')
    return (
        data['n'],
        data['flights'],
        data['src'],
        data['dst'],
        data['k']
    )
