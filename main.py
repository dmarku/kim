import argparse
from datetime import datetime
import requests
import tomllib
from dataclasses import dataclass

def create_parser():
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

    command_parsers = parser.add_subparsers(title='command', dest='command', metavar='command', required=True)

    ping_parser = command_parsers.add_parser('ping', help='check API availability')
    ping_parser.set_defaults(command_func=ping)

    add_timesheet_parser = command_parsers.add_parser('add-timesheet', help='add a timesheet')
    add_timesheet_parser.add_argument('--day', '-d', help="the date of the day")
    add_timesheet_parser.add_argument('--activity', '-a', type=int, help="the date of the day")
    add_timesheet_parser.add_argument('--project', '-p', type=int, help="the date of the day")
    add_timesheet_parser.add_argument('begin')
    add_timesheet_parser.add_argument('end')
    add_timesheet_parser.add_argument('description')
    add_timesheet_parser.set_defaults(command_func=add_timesheet)

    return parser

@dataclass
class Defaults:
    """Default parameters for 'kim'."""
    project: int
    activity: int

@dataclass
class Configuration:
    """Runtime configuration options for 'kim'."""
    api_url: str
    user: str
    api_key: str

    defaults: Defaults

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

            defaults = Defaults(
                project = config['defaults']['project'],
                activity = config['defaults']['activity'],
            ),
        )

def ping(args, config):
    url = config.api_url + '/ping'
    headers = {'x-auth-user': config.user, 'x-auth-token': config.api_key}

    response = requests.get(url, headers=headers)

    json = response.json()
    print(f'response body JSON is {json}')

def add_timesheet(args, config):
    url = config.api_url + '/timesheets'
    headers = {'x-auth-user': config.user, 'x-auth-token': config.api_key}

    now = datetime.now()

    if args.day is not None:
        parts = args.day.split('-')
        if len(parts) == 2:
            month, day = map(int, parts)
            date = now.replace(month=month, day=day)
        elif len(parts) == 3:
            year, month, day = map(int, parts)
            date = now.replace(year=year, month=month, day=day)
        else:
            # TODO: error
            pass

    bhour, bminute = int(args.begin[:2]), int(args.begin[2:])
    begin = date.replace(hour=bhour, minute=bminute)

    ehour, eminute = int(args.end[:2]), int(args.end[2:])
    end = date.replace(hour=ehour, minute=eminute)

    project = args.project or config.defaults.project
    activity = args.activity or config.defaults.activity

    data = {
        "begin": begin.isoformat(timespec='minutes'),
        "end": end.isoformat(timespec='minutes'),
        "project": project,
        "activity": activity,
        "description": args.description
    }

    response = requests.post(url, headers=headers, data=data)

    json = response.json()
    print(f'response body JSON is {json}')

def run():
    parser = create_parser()
    args = parser.parse_args()
    config = read_config(args.config_file)
    args.command_func(args, config)

if __name__ == "__main__":
    run()
