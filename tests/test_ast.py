import pytest

import pil


def test_get_operators_from_mult_syntax():
    assert 1 == len(pil.parse('a=b*3'))
    assert 3 == len(pil.parse('a=3*4*5*6'))
