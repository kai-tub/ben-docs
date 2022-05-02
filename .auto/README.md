# Auto scripts

These scripts are used to build the release automatically.
The [auto](https://intuit.github.io/auto/) tool bumps the tag version and publishes the release on GitHub.
The configuration file is the [.autorc](../.autorc) file in the root project folder.
During the release process, `auto` will trigger the [update_version](update_version.sh) script.
This script replaces the version specification in the `pyproject.toml` file with the newest release.
It will use poetry to bump the version inside the `pyproject.toml` file.
