"""Setup script"""

import os
import subprocess

from typing import List, TextIO
from setuptools import find_packages, setup

HEREDIR = os.path.abspath(os.path.dirname(__file__))
REQUIREMENTS_TXT = "requirements.txt"
VERSION = "0.1.0"


def open_local(filename: str, mode: str = "r") -> TextIO:
    """Open file in this directory."""

    return open(os.path.join(HEREDIR, filename), mode)


def execute_command(args: List[str]) -> List[str]:
    """Execute external command and return stdout"""

    try:
        process = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=True
        )
        return [line.strip() for line in process.stdout.splitlines()]
    except subprocess.CalledProcessError:
        return []


def create_requirements_txt() -> None:
    """Create file 'requirements.txt' from 'Pipfile.lock'."""

    try:
        with open_local("Pipfile.lock"):
            pass
    except FileNotFoundError:
        return

    pipenv_lines = execute_command(["pipenv", "lock", "-r"])
    if not pipenv_lines:
        return

    reqs = [line for line in pipenv_lines[1:] if line]
    with open_local(REQUIREMENTS_TXT, "w") as req_file:
        req_file.write("\n".join(reqs) + "\n")


def read_requirements() -> List[str]:
    """Read lines of requirements.txt and return them as list"""

    with open_local(REQUIREMENTS_TXT) as req_file:
        return [line.strip() for line in req_file.readlines() if line.strip()]


if __name__ == '__main__':
    create_requirements_txt()
    README = open_local("README.md").read()
    REQUIREMENTS = read_requirements()
    INSTALL_REQUIRES = REQUIREMENTS if REQUIREMENTS else None
    setup(
        name="release-py",
        description="Python template repo with test/release workflow",
        version=VERSION,
        long_description=README,
        install_requires=REQUIREMENTS,
        packages=find_packages(),
        include_package_data=True,
        entry_points={"console_scripts": [
            "release-py = release_py.main:main"
        ]})
