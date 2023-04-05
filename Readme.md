## Requirements and Installation

At the moment, this project is not ready for a stable release and requires Python 3.x and [pipenv](https://pipenv.pypa.io/en/latest/) to run. Install pipenv with:

```sh
pip install --user pipenv
```

Then, run the main script with:

```sh
pipenv run python main.py --help
```

## Configuration

_kim_ is configured with a TOML configuration file, `kim.toml` in the current directory.

It looks like this:

```toml
api_url = "https://kimai.example.com/api"
user    = "tom.sample@example.com"
api_key = "tH1sI5v3RyS4fE4nDs3CrE7"

[defaults]
# the default project when creating timesheets. override with `--project`/`-p` option.
project = 12
# the default activity when creating timesheets. override with `--activity`/`-a` option.
activity = 3
```

You can set another file with the `--config` option (or its shorthand `-c`):

```sh
pipenv run python main.py --config big-megacorp.toml
```

## Usage

### `add-timesheets`

```
pipenv run python main.py add-timesheet --day 01-31 0930 1730 "did some things"
```
