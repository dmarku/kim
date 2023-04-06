# _Kim_ - A Kimai Commandline Client

## Requirements and Installation

At the moment, this project is not ready for a stable release and requires Python 3.x and [pipenv](https://pipenv.pypa.io/en/latest/) to run. Install pipenv with:

```sh
pip install --user pipenv
```

Then, run the main script with:

```sh
pipenv run kim --help
```

## Configuration

_kim_ reads its runtime configuration from a file. This file is `kim.toml` in the working directory by default and must be in the [TOML](https://toml.io) format. It looks like this:

```toml
# Send requests to this Kimai API instance.
api_url = "https://kimai.example.com/api"

# Authenticate as this user
user    = "tom.sample@example.com"

# Authenticate with this API Key. You can set one in the Kimai Web UI in your user profile.
api_key = "tH1sI5v3RyS4fE4nDs3CrE7"

[defaults]
# the default project ID when creating timesheets. override with `--project`/`-p` option.
project = 12
# the default activity ID when creating timesheets. override with `--activity`/`-a` option.
activity = 3
```

You can set another file with the `--config` option (or its shorthand `-c`):

```sh
pipenv run python main.py --config big-megacorp.toml
```

## Usage

### Add Timesheets

```
pipenv run python main.py add-timesheet --day 01-31 0930 1730 "did some things"
```
