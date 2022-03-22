# Prototype
A MVP prototype for an antiques marketplace - part of a group project in Software Engineering and testing at HiØ, written with love in Python <3

## Authors
- Erik Teien Jarem [@eriktja](https://www.github.com/eriktja)
- Mujibullah Rahimi [@Mujibullah-Rahimi](https://www.github.com/Mujibullah-Rahimi)
- Ole-Jørgen Andersen [@olejorga](https://www.github.com/olejorga)
- Simen Jacobsen Øygard [@simenyo](https://www.github.com/simenyo)
- Sivert Østgård [@PerspectivCollection](https://www.github.com/PerspectivCollection)

## Installation
> You need the latest, "cutting edge", version of [Python](https://www.python.org) installed (3.8+)

To get the prototype set up, follow the instructions below

1: Clone and cd into the repository (if you don't have it already)

```bash
  git clone https://github.com/olejorga/prototype.git
  cd prototype
```

2: Install pipenv (if you don't have it already)

```bash
  pip install pipenv
```

3: Install the dependencies

```bash
  pipenv install
```

4: Enter the virtual environment

```bash
  pipenv shell
```

5: Run the protoype

```bash
  pipenv run app

  # ...or with reload on file change:
  pipenv run devmode
```

## Running tests

To run tests, run the following command

```bash
  pipenv run tests
```

...this will run all the unittests in the tests directory

## Dependencies
Runs primarily on [FastAPI](https://github.com/tiangolo/fastapi) with a little help from a couple of other modules 

See the `Pipfile` for a list of all dependencies
