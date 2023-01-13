alias s := serve-sphinx-docs
# prefix is required to ensure that the justfile script works
# even if `poetry shell` wasn't activated.
cmd_prefix := "poetry run"

# Build HTML documentation
build-docs:
	{{cmd_prefix}} sphinx-build docs docs/_build/

# Continuously build documentation and serve them via browser
serve-sphinx-docs:
	{{cmd_prefix}} sphinx-autobuild docs docs/_build --open-browser


