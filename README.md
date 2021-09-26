# Prototype

A MVP prototype for a antiques marketplace - part of a group project in SE and testing at HiØ.

## Authors

- Erik Teien Jarem [@eriktja](https://www.github.com/eriktja)
- Mujibullah Rahimi [@Mujibullah-Rahimi](https://www.github.com/Mujibullah-Rahimi)
- Ole-Jørgen Andersen [@olejorga](https://www.github.com/olejorga)
- Simen Jacobsen Øygard [@simenyo](https://www.github.com/simenyo)
- Sivert Østgård [@PerspectivCollection](https://www.github.com/PerspectivCollection)

## Installation

> You need the latest, "cutting edge", version of [Python](https://www.python.org) installed

To get the prototype set up, follow the instructions below

1: Clone and cd into the repository

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

## Running Tests

To run tests, run the following command

```bash
  pipenv run tests
```

...this will run all the unittests in the tests directory
