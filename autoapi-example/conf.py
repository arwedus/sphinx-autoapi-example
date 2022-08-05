#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "Python sphinx-autoapi example"
copyright = "2015, readthedocs"
author = "readthedocs"
version = "0.1"
release = "0.1"

# -- General configuration ---------------------------------------------------

needs_sphinx = "4.0"

# We have to add sphinx.ext.autodoc extension even though we want to replace it
# for importing the python code. This is required because sphinx-autoapi depends
# on the autodoc extension for the following features:
# - autodoc-style directives (e.g. .. autoapiclass::)
# - rendering type annotations
extensions = ["sphinx.ext.autodoc", "autoapi.extension", "sphinxcontrib.needs"]

master_doc = "index"

exclude_patterns = ["_build"]

templates_path = ["_templates"]

source_suffix = ".rst"

language = "en"

pygments_style = "sphinx"

todo_include_todos = False

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"

htmlhelp_basename = "pyexampledoc"

# -- Options for autoapi.extension -------------------------------------------
# Overview of configuration options:
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html

autoapi_type = "python"

# this can also be a path up (e.g. "../src")
autoapi_dirs = ["src"]

autoapi_file_pattern = "*.py"

autoapi_python_class_content = "both"

# The autoapi_root configuration option defines where generated documentation is output.
# To change where documentation is output, simply change this option to another directory
# relative to the documentation source directory
# autoapi_root = 'example/api'

# Set to false to turn off the automatic documentation generation:
# Only Python elements included with autodoc-style directives are included.
autoapi_generate_api_docs = False

# Since v3.0, sphinx has included an sphinx.ext.autodoc.typehints extension
# that is capable of rendering type annotations as parameter types and return types.
# AutoAPI is capable of the same thing.
# To enable this behaviour, load the sphinx.ext.autodoc.typehints (or sphinx.ext.autodoc)
# extension in Sphinx’s conf.py file and set autodoc_typehints to description as normal:
autodoc_typehints = "description"


# -- Needs: Plugin to manage requirements ------------------------------------
# https://sphinxcontrib-needs.readthedocs.io/en/latest

# Forces the user to set an ID for each need, which gets defined.
# needs_id_required = True

needs_title_optional = True
