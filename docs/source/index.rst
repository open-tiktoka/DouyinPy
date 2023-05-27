.. rst-class:: center-title

====================================
Welcome to DouyinPy's Documentation!
====================================

.. rst-class:: center

|PyPIBadge|_ |PythonBadge|_ |BuildBadge|_

**Extract data from Douyin without needing any login information or API keys.**

Getting Started
---------------

:doc:`Installation <users/installation>`
    How to install DouyinPy in your project.
:doc:`How It Works <users/explanation>`
    How does DouyinPy work? What **can't** you do with it?
:doc:`How to Use DouyinPy <users/usage>`
    How to use DouyinPy to grab data from Douyin.

If all you want to do is download videos from Douyin, check out the example: :ref:`Download Videos and Slideshows`

Reference
-------------

:doc:`API Reference <reference/api_reference>`
    API reference information about library content.

.. Hidden TOCs

.. toctree::
    :maxdepth: 2
    :caption: Getting Started
    :hidden:

    users/installation
    users/explanation
    users/usage

.. toctree::
    :maxdepth: 4
    :caption: Reference
    :hidden:

    reference/api_reference

.. |PyPIBadge| image:: https://img.shields.io/pypi/v/douyinapipy?style=flat-square&logo=pypi
    :height: 1.5em
.. _PyPIBadge: https://pypi.org/project/douyinapipy/

.. |PythonBadge| image:: https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square&logo=python
    :height: 1.5em
.. _PythonBadge: https://www.python.org

.. |BuildBadge| image:: https://img.shields.io/github/actions/workflow/status/Russell-Newton/DouyinPy/tox.yml?branch=main&label=Unit%20Tests&logo=github&style=flat-square
    :height: 1.5em
.. _BuildBadge: https://github.com/Russell-Newton/DouyinPy/actions/workflows/tox.yml
