"""Main entry point for release-py"""


def main() -> None:
    """Main eintry point for release-py"""

    print("\n".join((
        "\n# Python template repo with test/release workflow\n",
        "The included workflow will...",
        "- perform the following checks on push to master branch",
        "    - code using `pylint` and `flake8`",
        "    - packaging using `setup.py sdist`",
        "    - deploy using `pipenv install <sdist>`",
        "- create a new release after pushing a tag starting with v*",
        "    - release name and version will be pulled from `setup.py`",
        "    - release body will be message from triggering git tag\n"
    )))


if __name__ == "__main__":
    main()
