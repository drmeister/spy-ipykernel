from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

# Register nbextension


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'nglview-js-widgets',
        'require': 'nglview-js-widgets/extension'
    }]


def _jupyter_labextension_paths():
    return [{
        'name': 'nglview-js-widgets',
        'src': 'staticlab',
    }]


# TODO: do not use import *
# interface
from .config import BACKENDS
from .widget import NGLWidget
from .base_adaptor import *
from .adaptor import *
from .show import *
from . import datafiles

# utils
from .utils import widget_utils, js_utils

# for doc
from . import widget_box, widget, adaptor, show

__all__ = ['NGLWidget'] + widget.__all__ + adaptor.__all__ + show.__all__
