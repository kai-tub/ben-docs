# BigEarthNet Documentation

A user-friendly introduction to the multi-spectral BigEarthNet dataset.

## Accessing the site
At the time of writing, the content is not allowed to be shared with the general public.
To still allow thesis students and other colleagues to take a look at the current progress, the content is manually hosted on our `erde` server.
The website is _manually_ hosted via port 28080.
Connect to the server with:
`ssh -L 28080:localhost:28080 USERNAME@erde.rsim.tu-berlin.de`

Then open the

## Usage

### Building the book

If you'd like to develop and/or build the BigEarthNet Documentation book, you should:

1. Clone this repository
2. Install the `lock` environment with `conda` or, better, [mamba](https://github.com/mamba-org/mamba).
   1. The installation can be run automatically by running `just install`.
3. (Optional) Edit the books source files located in the `bigearthnet_documentation/` directory
4. Run `just build` to build the new documentation and inspect the output in `bigearthnet_documentation/_build/html/`.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/kai-tub/bigearthnet_documentation/graphs/contributors).

### Speeding-Up PRs
If you do not want to wait for GitHub Actions to tell you if the PR will pass the online test, use [act](https://github.com/nektos/act) to test it locally first. ;)

## Credits

This project is created using the excellent open-source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).

## TODO:
- Use only a single reference; no need to provide the paper links on every page
- Update to use the updated code for the previewer
- Update to use the template from my cookiecutter template
- Check
