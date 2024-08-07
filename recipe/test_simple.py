import os
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_array_less
import pytest

from phreeqcrm import BMIPhreeqcRM, IRM_OK, State

def test_dtor():
    model = BMIPhreeqcRM()
    del model

def test_initialized():
    model = BMIPhreeqcRM()
    assert model._state == State.UNINITIALIZED

def test_finalize_not_initialized():
    model = BMIPhreeqcRM()

    assert model._state == State.UNINITIALIZED
    model.finalize()
    assert model._state == State.UNINITIALIZED
