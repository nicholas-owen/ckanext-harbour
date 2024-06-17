"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.harbour.logic import validators


def test_harbour_reauired_with_valid_value():
    assert validators.harbour_required("value") == "value"


def test_harbour_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.harbour_required(None)
