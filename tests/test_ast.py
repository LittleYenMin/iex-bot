import pytest

import ast_example


def test_get_operators_from_mult_syntax():
    assert 1 == len(ast_example.parse('a=b*3'))
    assert 3 == len(ast_example.parse('a=3*4*5*6'))
