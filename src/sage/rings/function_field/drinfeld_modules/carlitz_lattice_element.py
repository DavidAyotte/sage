from sage.structure.element import ModuleElement
from sage.structure.richcmp import richcmp, op_NE, op_EQ

from sage.rings.laurent_series_ring import LaurentSeriesRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

from sage.misc.misc_c import prod

class CarlitzLatticeElement(ModuleElement):
    def __init__(self, parent, polynomial):
        self.polynomial = polynomial
        ModuleElement.__init__(self, parent)

    def _repr_(self):
        if self.polynomial.is_one():
            return "wI"
        if self.polynomial.is_zero():
            return "0"
        if self.polynomial.is_monomial():
            return f"{self.polynomial}*wI"
        else:
            return f"({self.polynomial})*wI"

    def _add_(self, other):
        return self.__class__(self.parent(), self.polynomial + other.polynomial)

    def _lmul_(self, c):
        return self.__class__(self.parent(), c*self.polynomial)

    def __neg__(self):
        return self.__class__(self.parent(), -self.polynomial)

    def __bool__(self):
        return bool(self.polynomial)

    def is_zero(self):
        return not bool(self)

    def richcmp(self, other, op):
        if op != op_EQ and op != op_NE:
            raise TypeError('invalid comparison between Carlitz lattice elements')
        return richcmp(self._polynomial, other._polynomial, op)

    def _varpi(self, n):
        A = self.base_ring()
        T = A.gen()
        q = A.base().cardinality()
        p_i = [1 - (T**(q**i) - T)/(T**(q**(i+1)) - T) for i in range(1, n)]
        return prod(p_i)

    def approx(self, n, name='s'): # placeholder
        A = self.base_ring()
        L = LaurentSeriesRing(A.fraction_field(), names=name)
        s = L.gen()
        varpi_n = self._varpi(n).subs(T=1/s)
        P = PolynomialRing(L, names='I')
        I = P.gen()
        return self.polynomial * varpi_n * I
