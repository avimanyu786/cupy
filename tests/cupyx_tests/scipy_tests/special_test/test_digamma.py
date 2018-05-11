import unittest

import cupy
from cupy import testing
import numpy
import cupyx.scipy.special

import scipy.special


@testing.gpu
@testing.with_requires('scipy')
class TestDigamma(unittest.TestCase):

    def _get_xp_func(self, xp):
        if xp is cupy:
            return cupyx.scipy.special
        else:
            return scipy.special

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-5)
    def test_arange(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        return self._get_xp_func(xp).digamma(a)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-5, rtol=1e-6)
    def test_linspace_positive(self, xp, dtype):
        a = numpy.linspace(0, 30, 1000, dtype=dtype)
        a = xp.asarray(a)
        return self._get_xp_func(xp).digamma(a)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-2, rtol=1e-3)
    def test_linspace_negative(self, xp, dtype):
        a = numpy.linspace(-30, 0, 1000, dtype=dtype)
        a = xp.asarray(a)
        return self._get_xp_func(xp).digamma(a)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-2, rtol=1e-3)
    def test_scalar(self, xp, dtype):
        return self._get_xp_func(xp).digamma(dtype(1.5))

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_allclose(atol=1e-2, rtol=1e-3)
    def test_inf_and_nan(self, xp, dtype):
        a = numpy.array([-numpy.inf, numpy.nan, numpy.inf]).astype(dtype)
        a = xp.asarray(a)
        return self._get_xp_func(xp).digamma(a)
