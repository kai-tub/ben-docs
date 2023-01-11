(contributing)=
# Contributing
This project is a community effort, and everyone is welcome to contribute!

Thank you for taking a look at how you can contribute to the project! 💚
There are many different ways to help this documentation grow.
In the following, we will list a couple of ways on how you can contribute to this project, or more generally, to the broader community 😎.

## Give feedback
The easiest way to improve the documentation is to highlight mistakes or areas that need further refinement.

<!-- hypothesis-pitch-start -->
The current design makes it easy to quickly provide feedback and highlight issues by utilizing the {{hypothesis}} library.
On the right-hand side, you can access a bar to see comments for the current page and create your annotations by highlighting text and clicking on the `annotate` selection.
If you have annotated something on the website, please make sure to set it to _public_ so that we can read it as well 😉.
As we aren't notified about annotations to the website, please inform us via {{issues}} or via [e-mail](mailto::k.clasen@protonmail.com) that you added suggestions.
<!-- hypothesis-pitch-end -->
You are required to register/log-in to use {{hypothesis}} (see [the official documentation for more details](https://web.hypothes.is/start/)) but you will only be required to do so once and can use it on any other website!

If you would like to provide more in-depth feedback and/or discuss something in more detail, feel free to open a _issue_ on the {{issues}} page.


## Increasing visibility
- Tell others about this interactive dataset website!
- [Star 🌟 the project on GitHub](https://github.com/kai-tub/ben-docs/)
- Create a custom interactive website for a different dataset to make it easier for others to get started with it!

## Directly update source code or notebooks

To guarantee identical, working development environments, this project utilizes {{nix}}.
{{nix}} is used to manage all of the _heavy_ project dependencies and _guarantees_ that the _same_ versions are used, (hopefully) eliminating the sentence: _"But it works on my machine"_.
The current project uses {{nix}} to manage the following dependencies:
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [just](https://github.com/casey/just)

[Poetry](https://python-poetry.org/) is then used to manage all of the direct Python dependencies.

To further simplify the setup, the (currently still unstable) {{devshell}} tool is used to quickly and easily create a `nix development` environment that prepares a managed shell environment.

This simplifies the entire set up the development environment to:
1. [Download and install the nix package manager](https://nixos.org/download.html#)
2. Clone this repository with `git clone https://github.com/kai-tub/ben-docs.git`
3. Change to the downloaded directory with `cd ben-docs`
4. Replicate the development environment with `nix development` (this may take some time depending on your download speed)
5. Start hacking 😁

If you create a [PR](https://docs.github.com/en/get-started/quickstart/hello-world#opening-a-pull-request), an automatic test suite will check if the documentation can be successfully regenerated (using {{nix}}).
After all tests pass, we will try our best to get back to you as quickly as possible!

Thanks for your hard work and for sticking around until
the end of the guide! 🎉🎉🎉
