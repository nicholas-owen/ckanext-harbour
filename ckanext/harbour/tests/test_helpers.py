"""Tests for helpers.py."""

import ckanext.harbour.helpers as helpers


def test_harbour_hello():
    assert helpers.harbour_hello() == "Hello, harbour!"
