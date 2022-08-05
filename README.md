# Sphinx-autoapi example project

## Overview

This example is for you if you have problems with the approach of Sphinx' own `autodoc` extension,
that requires to import all processed modules to extract the docstrings.

This is a minimal showcase how to include python API docstrings with the
[autoapi extension](https://sphinx-autoapi.readthedocs.io/en/latest/index.html),
which provides "autodoc" style documentation for multiple programming languages
without needing to load, run, or import the project being documented.

## How to setup and build this example

### Native python-only setup

This example requires Python (3.8 or newer), pip and - optionally - virtualenv.

You need the pip packages listed in the `requirements.in` file to build this example
(a minimal example needs just the sphinx packages `sphinx-autoapi` and `sphinxcontrib-needs`).
The `requirements.txt` file provides pinned versions (created via `pip-tools`) for everything you need.

To install the packages in a Python virtual environment, run, from this directory:

    virtualenv --python=python3.8 .sphinx-venv
    source .sphinx-venv/bin/activate  # run this every time to switch to the sphinx-venv
    pip3 install -r requirements.txt
    deactivate                        # run this to leave the virtual env

### Build the basic example

The [sphinx-build](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) command
should work on each machine where the above steps have been completed (e.g. native Linux, WSL, Windows).
The example does not provide a Makefile, but you can run sphinx directly like this to build the HTML documentation:

    cd autoapi-example
    sphinx-build -M html . ../_build

## License

This example is loosely based on an example/test of [sphinx-autoapi](https://github.com/readthedocs/sphinx-autoapi),
which was licensed under the MIT license at least at the time this example was forked.

Maintainer: [Arwed Starke](<70707249+arwedus@users.noreply.github.com>)
