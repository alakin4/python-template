# python-template
This is a boiler plate setup for python projects. It shows how I like to structure my
python projects.

This template can be used to inform you of where the most important pieces should be and
how to keep things organized. This template, for the most part follows the [Python
Packaging Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
which is intended to be followed by the larger community.

1. All the project code goes in the sub directory called `src` (read as source, at least by
me and it can also be referred to as the library folder) folder. This `src` directory
can be sub directories for the sake of structure, as you see fit.
    - The `__init__.py` files. It indicates to python that this is a library. This can
      be left blank or can be used to import things from files inside the `src`
      file––for ease.
    - 
2. A directory for `tests`. This starts with a `__main__.py` module so that you can run
   all tests.
3. There are files in the root of the directory:
   1. `pyproject.toml`. A file format used to store python specific metadata about the
      project and the library dependencies.
   2. `setup.py`. Most of what is currently put `pyproject.toml` used to be put in
      `setup.py`. This is what is run when your project is run with pip. It can for
      example contain code to compile the project. This file may not be needed for some
      projects.
   3. `.gitignore`. keep files from being checked into version control. For example, you
      do not want to check in the `.venv`, `.egg-info`, `.env`, `.credentials`, and `__pychache__/` files.
   4. `README.md`. The main documentation file for the project. Documentation is key.
      What you don't document now come back to bite you later.
   5. `LICENSE`. A license for you code even if you do not plan to package it for distribution.
   6. `main.py`. A way to run your source code. In this file, You basically import the
      src file items and also can have the argument parser set up for users.

## Cloning the repo

### VS code setup
### creating directory
If I am starting from scratch on my computer I do the following
1. `mkdir <python-project-name>`. then `cd <python-project-name>`
2. initialize git `git init`. This would give you a `.git` file where your code
   versioning meta data would be stored. 

But normaly, I start by creating a remote repository on github then I go to my computer
and clone that repository

### Package management
The project uses `uv` to manage python dependencies. If you do not have it yet, check out [the official site for
installation
steps](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

### Auto formatter
I use [`ruff`](https://docs.astral.sh/ruff/installation/) for auto formatting. if using
VS code, you could simply install the ruff extension: it comes with a bundled ruff
version so you do not need to install it separately.

### VS code Extensions and settings

create a `.vscode` directory and add two `json` files:
- `settings.json`
- `extensions.json`

### Init project with pyproject.toml
```sh
   cd my_project
   uv init --bare
```

python project structure. `--bare` is used to skip creating a README file.

### Add src file 
with a main.py file
add a `__init__.py` to make this into a package

to run this with uv, you do `uv run src/main.py`

requesting a python version usinfg uv `uv venv --python 3.11.6`. You can also install
version of python for example by doing `uv python install 3.12.3` or `uv python install
'>=3.8,<3.10'` or `uv python install 3.9 3.10 3.11`

check [here](https://docs.astral.sh/uv/pip/environments/) to know more about how to use
environments with uv. Here is a summary:
1. `uv venv` to create a virtual env and activate it with `source .venv/bin/activate`.
   To deactivate it, do `deactivate`

### tests
Add a tests folder

### Add Dependencies

use `uv add --dev pytest`. You can also add other dependencies like `pandas`, `numpy`.

> If you modify the toml file directly (not recommended), the lock file is out of sync
> so it needs to be updated. We can verify of the lock file is out os synce using  `uv
> lock --locked`.




### CI pipeline
https://www.youtube.com/watch?v=Y6D2XaFV3Cc

- create a github action file under `.github/workflows/code-quality.yaml`
- to have the code checks running in parallel, abstract away the installation of uv to a
  composite action. This allows me to refer to the action as part of the steps within a
  job.
- add a linter to make sure everyone uses the same coding standards
  - To check if the code is up to par, we can run `uvx ruff check .` and it would report
    all ines that violate a rule.
- add a formater. Checks how your code is visually structured, such as sorting of
  imports, double quotes or single quotes, line-length, back slash, etc. we can use `uvx
  ruff format .` to format all our commit code to the same configuration. Note that this
  may not take into account the import formating, however, the fix flag of the ruff
  check command can help:  `ruff check
  --select I --fix .` 
    - to check if all files are formated corectly, run `uvx ruff format --check .`
- Type checking. As a dynamic languange, python can use type hints to write consistent
  code. Unfortunately, `ruff` does not fix or catch type hints mistakes. It is good to
  make sure that the documented types are consitent with the use, we can use pyright.
  Ofcourse this needs to be added to the dev dependencies with `uv add --dev pyright`
  then we can always use it by running `uv run pyright .`
- testing 
  - to check for the validity of the implementation. this can be done by running
  `uv run pytest tests -v` or `uv run pytest -v`. The `-v` adds a bit more structured
  output
  - instead of just running unit tests, we can also track the test coverage by using
    `pytest-cov` then run `uv run pytest -v --cov`. If you need to generate an xml file,
    `uv run pytest -v --cov --cov-report=xml`. The coverage.xml file can be uploaded to
    [codecov.io](https://about.codecov.io/). I prefer not to run coverage in production.



### Pre-commit config
This would help with reducing iterations in the CI pipeline
