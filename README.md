# Python template repo with test/release workflow ![](https://github.com/vlntnwbr/release-py/workflows/test/badge.svg)
The included workflow will...
- perform the following checks on push to master branch
    - code using `pylint` and `flake8`
    - packaging using `setup.py sdist`
    - deploy using `pip install <sdist>`
- create a new release after pushing a tag starting with v*
    - release name and version will be pulled from `setup.py`
    - release body will be message from triggering git tag

## Installation
Installing using `pipx` isolates packages in their own environment and
exposes their entry points on PATH.
```
pipx install https://github.com/vlntnwbr/release-py/releases/latest/download/release-py.tar.gz
```
Alternatively install using
```
pip install https://github.com/vlntnwbr/release-py/releases/latest/download/release-py.tar.gz
```
