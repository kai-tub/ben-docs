# environment
env_name := "ben_docs"
env_run_cmd := "mamba run --live-stream --name " + env_name

# Build the book
build: clean
	{{env_run_cmd}} jupyter-book build bigearthnet_documentation

# Install and build environment
all: install build

clean:
	{{env_run_cmd}} jupyter-book clean bigearthnet_documentation

# Install all dependencies with mamba and install nbstripout filter to clean notebooks
install:
	mamba env create --file {{justfile_directory()}}/lock.yml --name {{env_name}} --force
	# {{env_run_cmd}} python -m ipykernel install --user
	{{env_run_cmd}} nbstripout --install

# Update dependencies by running a fresh install iva the unlocked environment
# and then exporting the updated locked environment to `lock.yml`
update-dependencies: install-no-lock write-lock

# Install from the general environment without locked dependencies
install-no-lock:
	mamba env create --file {{justfile_directory()}}/env.yml --name {{env_name}} --force
	# {{env_run_cmd}} python -m ipykernel install --user
	{{env_run_cmd}} nbstripout --install

# Requires the current environment to be activated!
write-lock:
	mamba env export > lock.yml

# Deploy to the hidden server
deploy: build
	scp -r {{justfile_directory()}}/bigearthnet_documentation/_build/html/* $USERNAME@$SERVER:ben-docs-server/
