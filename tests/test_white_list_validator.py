import ast

import pytest

import pix


def test_import_syntax():
    syntax = 'import os'
    with pytest.raises(ValueError):
        pix.white_list_validator(ast.parse(syntax))
