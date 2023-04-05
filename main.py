import argparse
import requests
import tomllib

def require_string(dict_, name):
  assert(name in dict_ and type(dict_[name]) == str)
  return dict_[name]

parser = argparse.ArgumentParser(
  prog="kimai API client",
  description="makes API calls to the Kimai API",
)

parser.add_argument('--config', '-c', metavar='configuration file', dest='config_file', default='kim.toml')

args = parser.parse_args()

with open(args.config_file, 'rb') as f:
  config = tomllib.load(f)

  api_url = require_string(config, 'api_url')
  api_key = require_string(config, 'api_key')
  user    = require_string(config, 'user')

url = api_url + '/ping'
print(headers)
response = requests.get(url, headers=headers)
json = response.json()
print(f'response body JSON is {json}')

