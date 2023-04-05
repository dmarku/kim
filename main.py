import argparse
import requests
import tomllib
from dataclasses import dataclass

@dataclass
class Configuration:
    """Runtime configuration options for 'kim'."""
    api_url: str
    user: str
    api_key: str

def require_string(dict_, name):
    assert(name in dict_ and type(dict_[name]) == str)
    return dict_[name]

def read_config(filename):
    with open(filename, 'rb') as f:
        config = tomllib.load(f)

        return Configuration(
            api_url = require_string(config, 'api_url'),
            user    = require_string(config, 'user'),
            api_key = require_string(config, 'api_key'),
        )
    
def run():
    parser = argparse.ArgumentParser(
      prog="kimai API client",
      description="makes API calls to the Kimai API",
    )

    parser.add_argument(
        '--config',
        '-c',
        metavar='configuration file',
        dest='config_file',
        default='kim.toml',
    )

    args = parser.parse_args()
    config = read_config(args.config_file)

    url = config.api_url + '/ping'
    headers = {'x-auth-user': config.user, 'x-auth-token': config.api_key}
    response = requests.get(url, headers=headers)
    json = response.json()
    print(f'response body JSON is {json}')

if __name__ == "__main__":
    run()
