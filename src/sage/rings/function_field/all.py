from .constructor import FunctionField

from sage.misc.lazy_import import lazy_import

lazy_import("sage.rings.function_field.drinfeld_modules.drinfeld_module", "DrinfeldModule")

from sage.rings.function_field.drinfeld_modules.carlitz_lattice import CarlitzLattice
