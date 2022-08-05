Python sphinx-autoapi example
=============================

Introduction
-------------

This example is for you if you have problems with the approach of Sphinx' own `autodoc` extension,
that requires to import all processed modules to extract the docstrings.
This approach is viable when you have a sphinx project that generates documentation for a single python package,
but can become an issue in large integration projects, where separate python projects,
which may run in separate virtual envs, are bundled in one documentation.

This is a minimal showcase how to include python API docstrings with the
`autoapi extension <https://sphinx-autoapi.readthedocs.io/en/latest/index.html>`_,
which provides "autodoc" style documentation for multiple programming languages
without needing to load, run, or import the project being documented.


Requirements and Traceability
-----------------------------

Sphinx-needs is used to provide application lifecycle management in code.

This example shows how to embed a SW specification in the code comments,
and link it to requirements specification in an rst document, i.e., here:

.. req::
   :id: R_PYIMPORT_1

   The Python API import shall support parsing sphinx-needs directives from code comments.

   The example shall also cover traceability (linkage).


.. req::
   :id: R_PYIMPORT_2

   The Python API import shall be able to parse google docstrings.


Manually included API documentation example
-------------------------------------------

This example shows API documentation included by some `autoapi...` directives:

.. toctree::
   :maxdepth: 2

   manualapi

Automatically generated API documentation example
-------------------------------------------------

To let sphinx-autoapi generate a full index of python symbols, set in conf.py::

   autoapi_generate_api_docs = True

And uncomment the following rst text::

   .. toctree::

      autoapi/index

.. note::

   This example cannot show both, because sphinx-needs does not support that directives are included twice.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

