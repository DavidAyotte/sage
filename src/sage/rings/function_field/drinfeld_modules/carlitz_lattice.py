r"""
Lattice associated with the Carlitz module
"""
from sage.categories.modules import Modules

from sage.modules.free_module import FreeModule

from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from .drinfeld_module import DrinfeldModule
from .carlitz_lattice_element import CarlitzLatticeElement


class CarlitzLattice(Parent):

    Element = CarlitzLatticeElement

    def __init__(self, function_ring):
        self._function_ring = function_ring
        function_field = function_ring.fraction_field()
        self._carlitz_module = DrinfeldModule(function_ring, [function_field.gen(), 1])
        Parent.__init__(self, base=function_ring, category=Modules(function_ring))

    def _repr_(self):
        return "Lattice associated with the Carlitz module"  # Placeholder repr

    def carlitz_module(self):
        return self._carlitz_module

    def free_module(self):
        return FreeModule(self._function_ring, 1)

    def exponential(self, name='z'):
        return self._carlitz_module.exponential(name=name)

    def logarithm(self, name='z'):
        return self._carlitz_module.logarithm(name=name)

    def generator(self):
        return self.element_class(self, self._function_ring.one())

    def gen(self, n):
        if n != 0:
            raise ValueError
        return self.generator()

    basis = generator
