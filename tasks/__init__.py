# -*- coding: UTF-8 -*-
"""
Invoke build script.
Show all tasks with::

    invoke -l

.. seealso::

    * http://pyinvoke.org
    * https://github.com/pyinvoke/invoke
"""

from __future__ import absolute_import

# -----------------------------------------------------------------------------
# BOOTSTRAP PATH: Use provided vendor bundle if "invoke" is not installed
# -----------------------------------------------------------------------------
INVOKE_MINVERSION = "0.13.0"
from . import _setup
_setup.setup_path()
_setup.require_invoke_minversion(INVOKE_MINVERSION)

# -----------------------------------------------------------------------------
# IMPORTS:
# -----------------------------------------------------------------------------
from invoke import Collection

# -- TASK-LIBRARY:
from . import clean
from . import docs
from . import test

# -----------------------------------------------------------------------------
# TASKS:
# -----------------------------------------------------------------------------
# None


# -----------------------------------------------------------------------------
# TASK CONFIGURATION:
# -----------------------------------------------------------------------------
namespace = Collection()
namespace.add_task(clean.clean)
namespace.add_task(clean.clean_all)
namespace.add_task(test.behave, "behave_test")
namespace.add_collection(Collection.from_module(docs))
namespace.add_collection(Collection.from_module(test))

# -- INJECT: clean configuration into this namespace
namespace.configure(clean.namespace.configuration())
namespace.configure(test.namespace.configuration())

